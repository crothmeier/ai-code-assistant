from setuptools import setup, find_packages

setup(
    name="ai-code-assistant",
    version="0.1.0",
    packages=find_packages(),
    extras_require={
        "dev": [
            "pytest",
            "pytest-asyncio",
            "ruff",
            "mypy",
        ],
    },
)