from fastapi import Request
from prometheus_client import Counter
import time

# Create Prometheus metrics
REQUEST_COUNT = Counter("request_count", "Total count of requests", ["method", "endpoint", "http_status"])
REQUEST_LATENCY = Counter("request_latency_seconds", "Request latency in seconds", ["method", "endpoint"])
FAILURE_COUNT = Counter("failure_count", "Total count of failures", ["method", "endpoint"])


async def monitor_requests(request: Request, call_next):
    """
        Middleware for monitoring requests and collecting metrics.

        This middleware measures the latency of each request, increments request counts, records request latency,
        and tracks failures if any occur.

        Args:
            request (Request): The request object.
            call_next (callable): A callable to proceed with the request handling.

        Returns:
            Response: The response to the request.

        Raises:
            Exception: If an error occurs during request handling.
    """
    start_time = time.time()
    try:
        response = await call_next(request)
        request_latency = time.time() - start_time
        REQUEST_COUNT.labels(request.method, request.url.path, response.status_code).inc()
        REQUEST_LATENCY.labels(request.method, request.url.path).inc(request_latency)
        return response
    except Exception as e:
        FAILURE_COUNT.labels(request.method, request.url.path).inc()
        raise e
