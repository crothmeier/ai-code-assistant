from unittest.mock import MagicMock

from src.router.weighted_router import GPUInfo, WeightedRouter


def test_weighted_router_gpu_name_case_insensitive() -> None:
    router = WeightedRouter(preferred_gpu_type="NVIDIA-A100")

    gpu1 = MagicMock(spec=GPUInfo)
    gpu1.name = "NVIDIA-A100"
    assert router.select_gpu(gpu1)

    gpu2 = MagicMock(spec=GPUInfo)
    gpu2.name = "nvidia-a100"
    assert router.select_gpu(gpu2)
