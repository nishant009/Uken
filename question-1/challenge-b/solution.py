import optparse
import pydash as _
import redis

class RedisInsert(object):

    def __init__(self, host, port, db):
        if _.is_empty(host) or _.is_empty(port) or _.is_empty(db):
            raise RuntimeError('Redis host or port or db missing. Please provide all three.')

        self._redis = redis.StrictRedis(host=host, port=port, db=db)

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
    options, _ = parser.parse_args()

    redis_insert = RedisInsert(
        options.host,
        options.port,
        options.database
    )
    return

if __name__ == "__main__":
    main()