import os
import logging
import redis

logging.basicConfig(level=logging.DEBUG)

ADDRESS = os.getenv('TESTTEST_SERVICE_HOST', '127.0.0.1')
PORT = os.getenv('TESTTEST_SERVICE_PORT', '6379')

r = redis.StrictRedis(
    host=ADDRESS,
    port=PORT,
    db=0
)

logging.info(r.get('aiueo'))
