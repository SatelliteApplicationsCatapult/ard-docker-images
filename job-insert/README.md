# Job insertion Docker image

Docker image that inserts job definitions into the Redis server used to process ARD campaigns.

## Usage examples

Find below examples to insert 1827 Landsat jobs from the `work-items.list` file.

### Using Docker

Run the job insert image directly with a bind mount:

```
~/ard-docker-images/job-insert$ docker run \
  -it \
  --name job-inserter \
  --mount type=bind,source="$(pwd)"/work-items.list,target=/var/opt/work-items.list \
  --network=landsat_default \
  satapps/ard-workflow-job-insert:1.1.0

Welcome to the Bitnami redis container
Subscribe to project updates by watching https://github.com/bitnami/bitnami-docker-redis
Submit issues and feature requests at https://github.com/bitnami/bitnami-docker-redis/issues
Send us your feedback at containers@bitnami.com


All data transferred. Waiting for the last reply...
Last reply received from server.
errors: 0, replies: 1827
```

### Using Docker Compose

Use the provided [docker-compose.yaml](docker-compose.yaml) file:

```
~/ard-docker-images/job-insert$ docker-compose up
Recreating job-inserter ... done
Attaching to job-inserter
job-inserter    |
job-inserter    | Welcome to the Bitnami redis container
job-inserter    | Subscribe to project updates by watching https://github.com/bitnami/bitnami-docker-redis
job-inserter    | Submit issues and feature requests at https://github.com/bitnami/bitnami-docker-redis/issues
job-inserter    | Send us your feedback at containers@bitnami.com
job-inserter    |
job-inserter    |
job-inserter    | All data transferred. Waiting for the last reply...
job-inserter    | Last reply received from server.
job-inserter    | errors: 0, replies: 1827
job-inserter exited with code 0
```

### Using Kubernetes

Create a ConfigMap using the contents of the `work-items.list`:

```
NAMESPACE=ard

kubectl create configmap ard-work-items --namespace=$NAMESPACE --from-file ./work-items.list 
```

Create the job insert Pod using the provided [job-inserter.yaml](job-inserter.yaml) file:

```
kubectl apply -f ./job-inserter.yaml
```

Show log for the Pod:

```
kubectl logs job-inserter -n $NAMESPACE

Welcome to the Bitnami redis container
Subscribe to project updates by watching https://github.com/bitnami/bitnami-docker-redis
Submit issues and feature requests at https://github.com/bitnami/bitnami-docker-redis/issues
Send us your feedback at containers@bitnami.com


All data transferred. Waiting for the last reply...
Last reply received from server.
errors: 0, replies: 1827
```

## Cleaning up examples

### Using Docker

```
~/ard-docker-images/job-insert$ docker rm job-inserter
```

### Using Docker Compose

```
~/ard-docker-images/job-insert$ docker-compose down
```

### Using Kubernetes

```
kubectl delete configmap ard-work-items --namespace=$NAMESPACE
kubectl delete -f ./job-inserter.yaml
```
