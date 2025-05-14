
from typing import Any

import pytest

from orchestrator.router import ModelEndpoint, WeightedRouter


class DummyEndpoint(ModelEndpoint):
    pass

@pytest.mark.asyncio
async def test_weight_cache_init(monkeypatch: Any) -> None:
    ep = [DummyEndpoint(name="test", url="http://x")]
    r = WeightedRouter(ep, "http://prom")
    # monkeypatch cache to avoid prometheus call
    r.cache = {"test": 1.0}
    best = await r.get_best_endpoint()
    assert best is not None
    assert best.name == "test"
