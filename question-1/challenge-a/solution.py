import optparse
import pydash as _
import redis
import time

class RedisInsert(object):
    
    MODE_SLOW = 0
    MODE_FAST = 1

    MAX_RECORDS = 100000

    def __init__(self, host, port, db, mode=MODE_FAST):
        if _.is_empty(host) or _.is_empty(port) or _.is_empty(db):
            raise RuntimeError('Redis host or port or db missing. Please provide all three.')

        self._redis = redis.StrictRedis(host=host, port=port, db=db)
        self._mode = mode

    def _slow_insert(self):
        for i in range(0, self.MAX_RECORDS):
            value = str(i)
            result = self._redis.set('slow-' + value, value)
            if result == False:
                raise RuntimeError('Failed to insert a key')
    
    def _fast_insert(self):
        pipe = self._redis.pipeline()
        
        for i in range(0, self.MAX_RECORDS):
            value = str(i)
            pipe.set('fast-' + value, value)
        
        result = pipe.execute()
        if False in result:
            raise RuntimeError('One or more keys failed to insert')

    def do_inserts(self):
        if self._mode == self.MODE_SLOW:
            self._slow_insert()
        else:
            self._fast_insert()

def main():
    parser = optparse.OptionParser()
    parser.add_option(
        '-t',
        '--host',
        action='store',
        dest='host',
        help='Redis host',
        default='localhost'
    )
    parser.add_option(
        '-p',
        '--port',
        action='store',
        dest='port',
        help='Redis port',
        default='6379'
    )
    parser.add_option(
        '-d',
        '--db',
        action='store',
        dest='database',
        help='Redis database',
        default='0'
    )
    parser.add_option(
        '-m',
        '--mode',
        action='store',
        dest='mode',
        help='Insert mode. Slow=0, Fast=1',
        default='1'
    )
    options, _ = parser.parse_args()

    redis_insert = RedisInsert(
        options.host,
        options.port,
        options.database,
        options.mode
    )

    try:
        start = time.time()
        redis_insert.do_inserts()
        end = time.time()

        print('Took ', str(end-start), ' to insert ', str(redis_insert.MAX_RECORDS))
    except RuntimeError as error:
        print(error.args)
        raise

    return

if __name__ == "__main__":
    main()