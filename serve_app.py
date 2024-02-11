from fastapi import FastAPI, Response
from prometheus_client import generate_latest
from app.api import serve_router
from app.middleware.prometheus import monitor_requests
from app.startup import on_startup


def create_app():
    """
        Creates a FastAPI application with specified configurations.

        This function sets up a FastAPI application instance, configures middleware, includes routers, and defines
        endpoints for serving Prometheus metrics.

        Returns:
            fast_app (FastAPI): The configured FastAPI application instance.
    """
    fast_app = FastAPI()
    on_startup(fast_app)
    # Add middleware to the FastAPI application
    fast_app.middleware('http')(monitor_requests)
    fast_app.include_router(serve_router)

    # Endpoint for exposing Prometheus metrics
    @fast_app.get("/metrics")
    async def metrics():
        return Response(generate_latest(), media_type="text/plain")

    return fast_app


app = create_app()
