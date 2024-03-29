from setuptools import setup

setup(
    name="gunicorn-healthz-filter",
    version="1.0",
    description="Filter /healthz endpoint access from your gunicorn logs.",
    author="backwardspy",
    author_email="backwardspy@pigeon.life",
    packages=["gunicorn_healthz_filter"],
    install_requires=["gunicorn"],
)
