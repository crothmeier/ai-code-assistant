"""Shim module that re-exports the production `WeightedRouter` implementation
from `src.router.weighted_router`.

This keeps legacy imports like
    from orchestrator import router as router_mod
working while ensuring there is only ONE authoritative WeightedRouter class.
"""

from src.router.weighted_router import WeightedRouter, ModelEndpoint  # noqa: F401

__all__ = ["WeightedRouter", "ModelEndpoint"]