#!/usr/bin/env python

################
# ARD workflow #
################

import json
from utils.prepS3 import prepareS3

def process_scene(json_data):
    loaded_json = json.loads(json_data)
    prepareS3(**loaded_json)

##################
# Job processing #
##################

import rediswq

import os
host = os.getenv("REDIS_SERVICE_HOST", "redis-master")

q = rediswq.RedisWQ(name="jobS3", host=host)
print("Worker with sessionID: " +  q.sessionID())
print("Initial queue state: empty=" + str(q.empty()))
while not q.empty():
  item = q.lease(lease_secs=1800, block=True, timeout=600) 
  if item is not None:
    itemstr = item.decode("utf=8")
    print("Working on " + itemstr)
    #time.sleep(10) # Put your actual work here instead of sleep.
    process_scene(itemstr)
    q.complete(item)
  else:
    print("Waiting for work")
print("Queue empty, exiting")

