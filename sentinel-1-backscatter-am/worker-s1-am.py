#!/usr/bin/env python

################
# ARD workflow #
################

import timeout_decorator
import json
from utils.prepS1AM import prepareS1AM

@timeout_decorator.timeout(10800, use_signals=False)
def process_scene(json_data):
    loaded_json = json.loads(json_data)
    prepareS1AM(**loaded_json)

##################
# Job processing #
##################

import os
import logging
import rediswq

level = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(format="%(asctime)s %(levelname)-8s %(name)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=level)

host = os.getenv("REDIS_SERVICE_HOST", "redis-master")
q = rediswq.RedisWQ(name="jobS1AM", host=host)

logger = logging.getLogger("worker")
logger.info("Worker with sessionID: " +  q.sessionID())
logger.info("Initial queue state: empty=" + str(q.empty()))

while not q.empty():
  item = q.lease(lease_secs=1800, block=True, timeout=600) 
  if item is not None:
    itemstr = item.decode("utf=8")
    logger.info("Working on " + itemstr)

    # In case the COG conversion gets stuck, a TimeoutError is raised and we try again: the existance of a COG from an earlier iteration is often enough to progress upon retrying
    for x in range(0, 2):  # try 2 times
      e = False
      try:
        process_scene(itemstr)
        e = True
      except timeout_decorator.TimeoutError:
        logger.info("Timed out while working on " + itemstr)
        e = False
        pass
      if e:
        break

    q.complete(item)
  else:
    logger.info("Waiting for work")

logger.info("Queue empty, exiting")

