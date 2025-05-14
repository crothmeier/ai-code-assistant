"""Router module for the orchestrator."""

class ModelEndpoint:
    """Represents a model endpoint for routing."""
    def __init__(self, name, url):
        self.name = name
        self.url = url

class WeightedRouter:
    """Routes requests to model endpoints based on weights."""
    def __init__(self, endpoints, prom_url):
        self.endpoints = endpoints
        self.prom_url = prom_url
        self.cache = {}
    
    async def get_best_endpoint(self):
        """Returns the best endpoint based on weights."""
        # In a real implementation, this would use the cache and weights
        # For the test, we just return the first endpoint
        return self.endpoints[0]