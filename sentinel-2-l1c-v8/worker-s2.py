#!/usr/bin/env python

################
# ARD workflow #
################

import json
from utils.prepS2 import prepareS2

def process_scene(json_data):
    loaded_json = json.loads(json_data)
    prepareS2(**loaded_json)

##################
# Job processing #
##################

import os
import logging
import rediswq
import datetime

level = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(format="%(asctime)s %(levelname)-8s %(name)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=level)

host = os.getenv("REDIS_SERVICE_HOST", "redis-master")
q = rediswq.RedisWQ(name="jobS2L1Cv8", host=host)

logger = logging.getLogger("worker")
logger.info(f"Worker with sessionID: {q.sessionID()}")
logger.info(f"Initial queue state: empty={q.empty()}")

while not q.empty():
    item = q.lease(lease_secs=1800, block=True, timeout=600)
    if item is not None:
        itemstr = item.decode("utf=8")
        logger.info(f"Working on {itemstr}")
        start = datetime.datetime.now().replace(microsecond=0)

        process_scene(itemstr)
        q.complete(item)

        end = datetime.datetime.now().replace(microsecond=0)
        logger.info(f"Total processing time {end - start}")
    else:
        logger.info("Waiting for work")

logger.info("Queue empty, exiting")

