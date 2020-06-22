# Docker images to deploy ARD workflows

Docker images to deploy ARD workflows. Clone this repository using the `--recurse-submodules` flag in order to recurse into the workflow submodules. If you missed that bit, you can pull submodules after the facts with `git submodule update --init`.

:warning: For production deployments (i.e. *campaigns*), please visit the [Helm Charts repo](https://github.com/SatelliteApplicationsCatapult/helm-charts) instead :warning:

## Building and pushing to Docker Hub

### Automated builds

Docker images are automatically built and published to [Docker Hub](https://hub.docker.com/u/satapps) from this repo when a release tag, x.y.z, is created.

### Manual builds

Login to docker.io:

```
docker login docker.io
```

Build and upload:

```
VERSION=1.2.7

cd landsat
docker build . -f Dockerfile -t satapps/ard-workflow-ls:${VERSION}
docker push satapps/ard-workflow-ls:${VERSION}

cd ../sentinel-1
docker build . -f Dockerfile -t satapps/ard-workflow-s1:${VERSION}
docker push satapps/ard-workflow-s1:${VERSION}

cd ../sentinel-2
docker build . -f Dockerfile -t satapps/ard-workflow-s2:${VERSION}
docker push satapps/ard-workflow-s2:${VERSION}

cd ../sentinel-2-l1c
docker build . -f Dockerfile -t satapps/ard-workflow-s2-l1c:${VERSION}
docker push satapps/ard-workflow-s2-l1c:${VERSION}

cd ../water-classification
docker build . -f Dockerfile -t satapps/ard-workflow-water-classification:${VERSION}
docker push satapps/ard-workflow-water-classification:${VERSION}

cd ../ml-water-classification
docker build . -f Dockerfile -t satapps/ard-workflow-ml-water-classification:${VERSION}
docker push satapps/ard-workflow-ml-water-classification:${VERSION}
```

## TODO

- Define the `PLATFORM` and `QUEUE_NAME` environment variables, so these can be set to e.g. `SENTINEL_2` and `jobS2` respectively, making the worker code agnostic of the satellite/platform to work on
- Define the `LEASE_SECS` and `TIMEOUT` environment variables, so these can be set according to what is appropriate for the satellite/platform to work on; alternatively read defaults from a configuration file that can be provided as a `ConfigMap` in Kubernetes
- Evaluate the use of [RQ](https://python-rq.org/), [Celery](http://www.celeryproject.org/), or [pyres](https://github.com/binarydud/pyres) for implementing a more resilient work queue
