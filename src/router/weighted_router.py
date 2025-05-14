class ModelEndpoint:
    """Represents a model endpoint for routing."""
    def __init__(self, name, url):
        self.name = name
        self.url = url


class WeightedRouter:
    def __init__(self, endpoints=None, prom_url=None, preferred_gpu_type=None):
        self.endpoints = endpoints or []
        self.prom_url = prom_url
        self.preferred_gpu_type = preferred_gpu_type
        self.cache = {}

    def select_gpu(self, gpu_info):
        if self.preferred_gpu_type and gpu_info.name:
            return self.preferred_gpu_type.lower() in gpu_info.name.lower()
        return True

    def calculate_gpu_metrics(self, gpu_info):
        # Correct MiB → GiB conversion
        gpu_memory_gib = gpu_info.total_memory_mib / 1024
        return gpu_memory_gib
    
    def build_worker_config(self, gpu_info):
        config = {"gpu_id": gpu_info.id}
        # Tune settings for NVIDIA T4 GPUs to curb PagedAttention fragmentation
        if gpu_info.name and "t4" in gpu_info.name.lower():
            config["block_size"] = 8
            config["gpu_memory_utilization"] = 0.85
        return config
        
    async def get_best_endpoint(self):
        """Returns the best endpoint based on weights."""
        # In a real implementation, this would use the cache and weights
        # For now, we just return the first endpoint if available
        return self.endpoints[0] if self.endpoints else None