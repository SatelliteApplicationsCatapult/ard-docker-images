# Docker images to deploy ARD workflows with Docker and docker-compose

Docker images to deploy ARD workflows. Clone this repository using the `--recurse-submodules` flag in order to recurse into the workflow submodules.

:warning: For large scale deployments (i.e. *campaigns*), please visit the [Helm Charts repo](https://github.com/SatelliteApplicationsCatapult/helm-charts) instead. :warning:

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
VERSION=1.2.4

cd landsat
docker build . -f Dockerfile.dist -t satapps/ard-workflow-ls:${VERSION}
docker push satapps/ard-workflow-ls:${VERSION}

cd ../sentinel-1
docker build . -f Dockerfile.dist -t satapps/ard-workflow-s1:${VERSION}
docker push satapps/ard-workflow-s1:${VERSION}

cd ../sentinel-2
docker build . -f Dockerfile.dist -t satapps/ard-workflow-s2:${VERSION}
docker push satapps/ard-workflow-s2:${VERSION}

cd ../sentinel-2-l1c
docker build . -f Dockerfile -t satapps/ard-workflow-s2-l1c:${VERSION}
docker push satapps/ard-workflow-s2-l1c:${VERSION}

cd ../water-classification
docker build . -f Dockerfile.dist -t satapps/ard-workflow-water-classification:${VERSION}
docker push satapps/ard-workflow-water-classification:${VERSION}
```
