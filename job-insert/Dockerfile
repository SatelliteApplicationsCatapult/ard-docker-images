FROM bitnami/redis:5.0.5-debian-9-r104

LABEL maintainer="Luigi Di Fraia"

CMD /bin/cat /var/opt/work-items.list | redis-cli -h redis-master --pipe
