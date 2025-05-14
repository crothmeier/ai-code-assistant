from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union, TypedDict, Sequence


@dataclass
class ModelEndpoint:
    """Represents a model endpoint for routing."""
    name: str
    url: str


class GPUInfo:
    """GPU information provided by external systems."""
    id: str
    name: Optional[str]
    total_memory_mib: float


class WorkerConfig(TypedDict, total=False):
    """Configuration for worker instances."""
    gpu_id: str
    block_size: int
    gpu_memory_utilization: float


class WeightedRouter:
    def __init__(
        self, 
        endpoints: Optional[Sequence[ModelEndpoint]] = None, 
        prom_url: Optional[str] = None, 
        preferred_gpu_type: Optional[str] = None
    ) -> None:
        self.endpoints: List[ModelEndpoint] = list(endpoints) if endpoints else []
        self.prom_url = prom_url
        self.preferred_gpu_type = preferred_gpu_type
        self.cache: Dict[str, float] = {}

    def select_gpu(self, gpu_info: GPUInfo) -> bool:
        if self.preferred_gpu_type and gpu_info.name:
            return self.preferred_gpu_type.lower() in gpu_info.name.lower()
        return True

    def calculate_gpu_metrics(self, gpu_info: GPUInfo) -> float:
        # Correct MiB → GiB conversion
        gpu_memory_gib = gpu_info.total_memory_mib / 1024
        return gpu_memory_gib
    
    def build_worker_config(self, gpu_info: GPUInfo) -> WorkerConfig:
        config: WorkerConfig = {"gpu_id": gpu_info.id}
        # Tune settings for NVIDIA T4 GPUs to curb PagedAttention fragmentation
        if gpu_info.name and "t4" in gpu_info.name.lower():
            config["block_size"] = 8
            config["gpu_memory_utilization"] = 0.85
        return config
        
    async def get_best_endpoint(self) -> Optional[ModelEndpoint]:
        """Returns the best endpoint based on weights."""
        # In a real implementation, this would use the cache and weights
        # For now, we just return the first endpoint if available
        return self.endpoints[0] if self.endpoints else None