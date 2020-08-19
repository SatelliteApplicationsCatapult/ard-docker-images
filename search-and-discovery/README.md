# Search & Discovery Container for creation of Jobs to submit to ARD Workflow Containers

## Docker Hub images
Pre-built Docker images for production use can be pulled from [our Docker Hub repo](https://hub.docker.com/r/satapps/).

## Dockerfile for development
The provided [Dockerfile](Dockerfile-devel) creates a Docker image with necessary packages for querying APIs associated with each dataset, set up by means of Miniconda v4.7.10. [Jupyter Notebook](https://jupyter.org/) is included for interactive development and started once the Docker image is run.

## Docker Compose
A [Docker Compose](docker-compose.yml) example file is provided to set up an interactive environment for development purposes.

### Environment variables for Docker Compose
Environment variables should be set in a `.env` file for Docker Compose. You might use [.env.example](./.env.example) as a starting point. The [.gitignore](../.gitignore) file contains an entry for `.env` in order to avoid it from being accidentally added to this repository, so the `.env` file is suitable for storing sensitive information.

### Building and running a development platform
Set up an ARD workflow instance by issuing:

```
docker-compose up -d
```

### Jupyter Notebook
Jupyter Notebook can be accessed at the URL: http://{Serve's IP Address}:8866.\
The access token is `secretpassword`, which is set by means of the CMD statement within the [Dockerfile](Dockerfile).

### Amending the workflow
The actual search and discovery notebooks can be expanded within the [ard-workflows](https://github.com/SatelliteApplicationsCatapult/ard-workflows) submodule at workflows directory.
