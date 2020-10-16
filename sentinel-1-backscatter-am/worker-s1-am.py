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
logging.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=level)

host = os.getenv("REDIS_SERVICE_HOST", "redis-master")
q = rediswq.RedisWQ(name="jobS1AM", host=host)

logging.info("Worker with sessionID: " +  q.sessionID())
logging.info("Initial queue state: empty=" + str(q.empty()))

while not q.empty():
  item = q.lease(lease_secs=1800, block=True, timeout=600) 
  if item is not None:
    itemstr = item.decode("utf=8")
    logging.info("Working on " + itemstr)

    try:
      process_scene(itemstr)
    except timeout_decorator.TimeoutError:
      logging.info("Timed out while working on " + itemstr)
      pass

    q.complete(item)
  else:
    logging.info("Waiting for work")

logging.info("Queue empty, exiting")

