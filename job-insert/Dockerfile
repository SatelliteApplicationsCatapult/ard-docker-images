FROM bitnami/redis:5.0.5-debian-9-r104

LABEL maintainer="Luigi Di Fraia"

CMD [ "sh", "-c", "/bin/cat /var/opt/work-items.list | redis-cli -h ${REDIS_SERVICE_HOST:-redis-master} --pipe" ]
