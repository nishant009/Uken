import pydash as _
import redis

class RedisInsert(object):

    MAX_RECORDS = 100000

    def __init__(self, host, port, db):
        if _.is_empty(host) or _.is_empty(port) or _.is_empty(db):
            raise RuntimeError('Redis host or port or db missing. Please provide all three.')

        self._redis = redis.StrictRedis(host=host, port=port, db=db)
        self._pipe = self._redis.pipeline()
        self._count = 0

    def insert(self, key, value):
        self._pipe.set(key, value)
        self._count += 1

        if self._count == self.MAX_RECORDS:
            self._pipe.execute()
            self._count == 0