import logging
import gunicorn.glogging


filtered_routes = [
    "/healthz",
    "/livez",
    "/readyz",
]


class HealthzFilter(logging.Filter):
    def filter(self, record):
        return not any(route in record.getMessage() for route in filtered_routes)


class Logger(gunicorn.glogging.Logger):
    def setup(self, cfg):
        super().setup(cfg)
        logger = logging.getLogger("gunicorn.access")
        logger.addFilter(HealthzFilter())
