# ARD Workflow Container for Sentinel-2 Datasets

## Base image
The provided [Dockerfile](Dockerfile) creates a Docker image with an ARD workflow for Sentinel-2 datasets set up by means of Miniconda v4.7.10.
[Jupyter Notebook](https://jupyter.org/) can be optionally included and started once the Docker image is run.

## Docker Hub images
Pre-built Docker images can be pulled from [our Docker Hub repo](https://hub.docker.com/r/satapps/).

## Docker Compose
A [Docker Compose](docker-compose.yml) example file is provided to set up a fully functional ARD workflow instance.\
To use it you can issue, for example for 3 worker containers:

```docker-compose up --scale jupyter-worker=3 -d```

Once the above completes, the job queue is ready to be filled in with work items by issuing:

```bash
docker exec -it redis-master /bin/bash
redis-cli -h redis-master
rpush jobS2 '{"in_scene": "S2A_MSIL2A_20190812T235741_N0213_R030_T56LRR_20190813T014708", "s3_bucket": "pds-satapps", "s3_dir": "fiji/Sentinel_2/"}'
...
lrange jobS2 0 -1
```

For [mass insertion](https://redis.io/topics/mass-insert) you can use e.g.:

```bash
docker exec -it redis-master /bin/bash
cat <<EOF | redis-cli -h redis-master --pipe
rpush jobS2 '{"in_scene": "S2A_MSIL2A_20190812T235741_N0213_R030_T56LRR_20190813T014708", "s3_bucket": "pds-satapps", "s3_dir": "fiji/Sentinel_2/"}'
...
EOF
```

At any time afterwards, the queue can be processed interactively by running the [worker](worker.ipynb) Jupyter Notebook.

## Environment variables for Docker Compose
Environment variables can be set in a `.env` file for Docker Compose. You might use [.env.example](./.env.example) as a starting point. The [.gitignore](../.gitignore) file contains an entry for `.env` in order to avoid it from being accidentally added to this repository, so the `.env` file is suitable for storing sensitive information.

## AWS access
In order to be able to get/put data from/to S3, you need to ensure that the environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are set.

## Jupyter Notebook
Jupyter Notebook can be accessed at the URL: http://{Serve's IP Address}:8888 for the first replica, 8889 for the second one if present, and so on.\
For the access token, check the CMD statement within the [Dockerfile](Dockerfile).

## TODO
- Define the `PLATFORM` and `QUEUE_NAME` environment variables, so these can be set to `SENTINEL_2` and `jobS2` respectively, making the worker code agnostic of the satellite/platform to work on
- Define the `LEASE_SECS` and `TIMEOUT` environment variables, so these can be set according to what is appropriate for the satellite/platform to work on; alternatively read defaults from a configuration file that can be provided as an `env_file` in Docker Compose or as a `ConfigMap` in Kubernetes
- Generate a single Docker image: Jupyter Notebook could be optionally installed upon deployment, based on an environment variable, e.g. `JUPYTER_NOTEBOOK` set to `YES`; the main drawback of doing so (compared to building separate Docker images) is that dependencies might fail to support the installation of Jupyter Notebook 
- Evaluate the use of [RQ](https://python-rq.org/), [Celery](http://www.celeryproject.org/), or [pyres](https://github.com/binarydud/pyres) for implementing a more resilient work queue
