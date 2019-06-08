from flask import Flask
import os
import logging
import redis

logging.basicConfig(level=logging.DEBUG)

ADDRESS = os.getenv('HYPER_REDIS_SERVICE_HOST', 'redis')
PORT = os.getenv('HYPER_REDIS_SERVICE_PORT', '6379')

r = redis.StrictRedis(
    host=ADDRESS,
    port=PORT,
    db=0
)

app = Flask(__name__)


@app.route('/')
def index():
    # index.html をレンダリングする
    logging.info(r.get('aiueo'))
    return r.get('aiueo')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
