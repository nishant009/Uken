import optparse
from flask import Flask
from flask import request

from solution import RedisInsert

app = Flask(__name__)

redis_insert = None

@app.route('/')
def hello():
    return 'This is a server that takes redis key pair values and \
        inserts them into redis. Use \
        "http://localhost:5000/pair?key=key&val=value" for inserting.'

@app.route('/pair', methods=['GET'])
def insert():
    redis_insert.insert(
        request.args.get('key', ''), 
        request.args.get('value', '')
    )
    return 'Success'

def setup():
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

    try:
        instance = RedisInsert(
            options.host,
            options.port,
            options.database
        )
        return instance
    except RuntimeError as error:
        print(error.args)
        raise

if __name__ == "__main__":
    try:
        redis_insert = setup()
        app.run(host='0.0.0.0')
    except RuntimeError as error:
        raise