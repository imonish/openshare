## Health Check

This project exposes a `/health/` endpoint used by Docker healthcheck
to automatically monitor the application status.

Docker periodically checks this endpoint and marks the container as
healthy or unhealthy without manual intervention.
