# Docker images to deploy ARD workflows

Docker images to deploy ARD workflows. 

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
VERSION=1.3.1

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

cd ../mlwater-classification
docker build . -f Dockerfile -t satapps/ard-workflow-ml-water-classification:${VERSION}
docker push satapps/ard-workflow-ml-water-classification:${VERSION}
```