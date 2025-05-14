import asyncio, time, httpx, logging
from typing import List, Optional
from pydantic import BaseModel

class ModelEndpoint(BaseModel):
    name: str
    url: str
    gpu: Optional[str] = None

class WeightedRouter:
    def __init__(self, endpoints: List[ModelEndpoint], prometheus_url: str):
        self.endpoints = endpoints
        self.prometheus_url = prometheus_url
        self.cache = {}
        self.cache_ttl = 15
        self.last_update = 0

    async def _query(self, client, q):
        r = await client.get(f"{self.prometheus_url}/api/v1/query", params={"query": q})
        r.raise_for_status()
        return r.json()["data"]["result"]

    async def update_weights(self):
        if time.time() - self.last_update < self.cache_ttl:
            return
        async with httpx.AsyncClient() as c:
            mem, gfree, gutil, lat = await asyncio.gather(
                *[self._query(c, q) for q in (
                    'node_memory_MemAvailable_bytes/1024/1024',
                    'DCGM_FI_DEV_FB_FREE',
                    'DCGM_FI_DEV_GPU_UTIL',
                    'inference_request_latency_seconds{quantile="0.95"} * 1000'
                )]
            )
        weights = {}
        for ep in self.endpoints:
            node = ep.url.split("://")[1].split(":")[0]
            free_mb = next((float(m['value'][1]) for m in mem if m['metric']['instance'].startswith(node)), 4096)
            lat_ms = max(next((float(l['value'][1]) for l in lat if l['metric']['instance'].startswith(node)), 100), 50)
            score = (free_mb / 1024) * (1 / lat_ms)
            if ep.gpu:
                gpu_free_gb = next((float(g['value'][1]) / 1024 / 1024 / 1024 for g in gfree if g['metric']['instance'].startswith(node)), 1)
                util_pct = next((float(u['value'][1]) for u in gutil if u['metric']['instance'].startswith(node)), 50)
                score *= gpu_free_gb * (100 / max(util_pct, 1))
            weights[ep.name] = score
        self.cache, self.last_update = weights, time.time()
