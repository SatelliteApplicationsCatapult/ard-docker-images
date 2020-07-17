# Job insertion Docker image

Docker image that inserts job definitions into the Redis server used to process ARD campaigns.

## Usage examples

Find below examples to insert 1827 Landsat jobs from the `work-items.list` file.

### Using Docker

Run the job insert image directly with a bind mount after replacing the network name as appropriate:

```
$ docker run \
  --rm \
  --name job-inserter \
  --env "REDIS_SERVICE_HOST=redis-master" \
  --mount type=bind,source="$(pwd)"/work-items.list,target=/var/opt/work-items.list \
  --network=landsat_default \
  satapps/ard-workflow-job-insert:1.2.1

Welcome to the Bitnami redis container
Subscribe to project updates by watching https://github.com/bitnami/bitnami-docker-redis
Submit issues and feature requests at https://github.com/bitnami/bitnami-docker-redis/issues
Send us your feedback at containers@bitnami.com


All data transferred. Waiting for the last reply...
Last reply received from server.
errors: 0, replies: 1827
```

### Using Docker Compose

Customize the provided [docker-compose.yml](docker-compose.yml) file with the name of the relevant network (e.g. `landsat_default`) and then issue:

```
$ docker-compose up
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

Set up environment variables as per [Redis Master server deployment](https://github.com/SatelliteApplicationsCatapult/helm-charts/tree/master/stable/ard-campaign#redis-master-server-deployment):

```
$ NAMESPACE=ard # This needs to be the namespace used to deploy the Redis server and ARD processing workers

$ RELEASEREDIS=redis # This needs to be the release name used to deploy the Redis Master server
```

Create a ConfigMap using the contents of the `work-items.list`:

```
$ kubectl create configmap ard-work-items --namespace=$NAMESPACE --from-file ./work-items.list 
```

Create the job insert Pod using the provided [job-inserter.yaml](job-inserter.yaml) file:

```
$ sed -i "s/namespace:.*/namespace: $NAMESPACE/" job-inserter.yaml

$ if [ ! "${RELEASEREDIS}" = "redis" ]; then
  REDIS_SERVICE_HOST=${RELEASEREDIS}-redis-master
  sed -i "s/redis-master/${REDIS_SERVICE_HOST}/g" job-inserter.yaml
fi

$ kubectl apply -f ./job-inserter.yaml
```

Show log from the Pod:

```
$ kubectl logs job-inserter -n $NAMESPACE

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

The Docker container `job-inserter` is automatically removed at the end of the job insertion.

### Using Docker Compose

```
$ docker-compose down
```

### Using Kubernetes

```
$ kubectl delete configmap ard-work-items --namespace=$NAMESPACE
$ kubectl delete -f ./job-inserter.yaml
```

## TODO
- Define a Helm chart for templating and value substitution or add the job inserter to the existing [ard-campaign](https://github.com/SatelliteApplicationsCatapult/helm-charts/tree/master/stable/ard-campaign) Helm chart.
