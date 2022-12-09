import datetime
import json
import logging
import os
import redis

from workflows.utils.prepLS import prepareLS

if __name__ == "__main__":
    log_file_name = f"landsat_ard_{datetime.datetime.now()}.log"
    log_file_path = f"/tmp/{log_file_name}"
    level = os.getenv("LOGLEVEL", "INFO").upper()
    logging.basicConfig(format="%(asctime)s %(levelname)-8s %(name)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S",
                        level=level)
    logging.getLogger().addHandler(logging.StreamHandler())
    logging_file_handler = logging.FileHandler(log_file_path)
    logging.getLogger().addHandler(logging_file_handler)
    logger = logging.getLogger("worker")

    try:
        host = os.getenv("REDIS_HOST", "localhost")
        port = int(os.getenv("REDIS_PORT", "6379"))
        redis_queue = os.getenv("REDIS_USGS_PROCESSED_CHANNEL", "jobLS")
        logging.info(f"Connecting to Redis at {host}:{port}")
        redis = redis.Redis(host=host, port=port)

        while True:
            item = redis.blpop(redis_queue, timeout=1)
            if item is not None:
                item_decoded = item[1].decode("utf=8")
                logger.info(f"Working on {item_decoded}")
                start = datetime.datetime.now().replace(microsecond=0)
                loaded_json = json.loads(item_decoded)
                prepareLS(**loaded_json)
                end = datetime.datetime.now().replace(microsecond=0)
                logger.info(f"Total processing time {end - start}")
            else:
                logger.info("No work found in queue")
                break

        logger.info("Queue empty, exiting")
        exit(0)

    except Exception as e:
        logger.exception(e)
        logging.getLogger().removeHandler(logging_file_handler)
        logging_file_handler.close()
