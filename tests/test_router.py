
import pytest

from orchestrator import router as router_mod


class DummyEndpoint(router_mod.ModelEndpoint):
    pass

@pytest.mark.asyncio
async def test_weight_cache_init(monkeypatch):
    ep = [DummyEndpoint(name="test", url="http://x")]
    r = router_mod.WeightedRouter(ep, "http://prom")
    # monkeypatch cache to avoid prometheus call
    r.cache = {"test": 1.0}
    best = await r.get_best_endpoint()
    assert best.name == "test"
