# ARD Workflow Container for Sentinel-2 Datasets

## Docker Hub images
Pre-built Docker images for production use can be pulled from [our Docker Hub repo](https://hub.docker.com/r/satapps/).

## TODO
- Define the `PLATFORM` and `QUEUE_NAME` environment variables, so these can be set to `SENTINEL_2` and `jobS2` respectively, making the worker code agnostic of the satellite/platform to work on
- Define the `LEASE_SECS` and `TIMEOUT` environment variables, so these can be set according to what is appropriate for the satellite/platform to work on; alternatively read defaults from a configuration file that can be provided as an `env_file` in Docker Compose or as a `ConfigMap` in Kubernetes
- Generate a single Docker image: Jupyter Notebook could be optionally installed upon deployment, based on an environment variable, e.g. `JUPYTER_NOTEBOOK` set to `YES`; the main drawback of doing so (compared to building separate Docker images) is that dependencies might fail to support the installation of Jupyter Notebook 
- Evaluate the use of [RQ](https://python-rq.org/), [Celery](http://www.celeryproject.org/), or [pyres](https://github.com/binarydud/pyres) for implementing a more resilient work queue
