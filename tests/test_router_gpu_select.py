from unittest.mock import MagicMock
from src.router.weighted_router import WeightedRouter


def test_weighted_router_gpu_name_case_insensitive():
    router = WeightedRouter(preferred_gpu_type="NVIDIA-A100")

    gpu1 = MagicMock()
    gpu1.name = "NVIDIA-A100"
    assert router.select_gpu(gpu1)

    gpu2 = MagicMock()
    gpu2.name = "nvidia-a100"
    assert router.select_gpu(gpu2)