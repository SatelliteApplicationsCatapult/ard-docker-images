# ARD workflow container infrastructure

## Base image
The provided [Dockerfile](Dockerfile) creates a Docker image with an ARD workflow set up by means of Miniconda v4.7.10.
[Jupyter Notebook](https://jupyter.org/) is optionally included and started once the Docker image is run.

## Docker Compose
A [Docker Compose](docker-compose.yml) example file is provided to set up a fully functional ARD workflow instance.\
To use it you can issue, for example for 3 worker containers:

```docker-compose up --scale jupyter-worker=3 -d```

Once the above completes, the job queue is ready to be filled in with scene names by issuing:

```
docker exec -it redis-master /bin/bash
redis-cli -h redis-master
rpush jobS2 '{"in_scene": "S2A_MSIL2A_20190812T235741_N0213_R030_T56LRR_20190813T014708", "inter_dir": "/data/intermediate/"}'
...
lrange jobS2 0 -1
```

At any time afterwards, the queue can be processed interactively by running the [worker](worker.ipynb) Jupyter Notebook.

## Environment variables for Docker Compose
Environment variables can be set in a `.env` file for Docker Compose. You might use [.env.example](./.env.example) as a starting point.

## AWS access
In order to be able to get/put data from/to S3, you need to ensure that the environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are set.

## Jupyter Notebook
Jupyter Notebook can be accessed at the URL: http://{Serve's IP Address}:8888 for the first replica, 8889 for the second one if present, and so on.\
For the access token, check the CMD statement within the [Dockerfile](Dockerfile).

## TODO
- Define the `PLATFORM` and `QUEUE_NAME` environment variables, so these can be set to `SENTINEL_2` and `jobS2` respectively, making the worker code agnostic of the satellite/platform to work on
