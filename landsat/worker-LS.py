#!/usr/bin/env python

################
# ARD workflow #
################

import json
from utils.prepLS import prepareLS
from utils.prep_utils import s3_single_upload

def process_scene(json_data):
    loaded_json = json.loads(json_data)
    prepareLS(**loaded_json)

##################
# Job processing #
##################

import os
import logging
import rediswq
import datetime


log_file_name = f"landsat_ard_{datetime.datetime.now()}.log"
log_file_path = f"/tmp/{log_file_name}"
level = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(format="%(asctime)s %(levelname)-8s %(name)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=level)
logging.getLogger().addHandler(logging.StreamHandler())
logging_file_handler = logging.FileHandler(log_file_path)
logging.getLogger().addHandler(logging_file_handler)
try:
    host = os.getenv("REDIS_SERVICE_HOST", "redis-master")
    port = int(os.getenv("REDIS_SERVICE_PORT", "6379"))
    logging.info(f"Connecting to Redis at {host}:{port}")
    q = rediswq.RedisWQ(name="jobLS", host=host, port=port)

    logger = logging.getLogger("worker")
    logger.info(f"Connnecting to redis host: {host} got {q}")
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
            logger.info("No work. Exiting")
            break

    logger.info("Queue empty, exiting")
    exit(0)

except:
    
    logging.getLogger().removeHandler(logging_file_handler)
    logging_file_handler.close()
    bucket = os.getenv("AWS_BUCKET", "")
    if bucket:
        logging.info(f"Uploading log file to s3://{bucket}/common_sensing2/logs/{log_file_name}")
        s3_single_upload(log_file_path, f"common_sensing2/logs/{log_file_name}", bucket)
