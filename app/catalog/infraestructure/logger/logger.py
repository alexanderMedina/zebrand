import logging
from logstash_async.handler import AsynchronousLogstashHandler


def logger():
    host = 'logstash'
    port = 5000
    # Get you a test logger
    account_logger = logging.getLogger('python-logstash-logger')
    # Set it to whatever level you want - default will be info
    account_logger.setLevel(logging.DEBUG)
    # Create a handler for it
    async_handler = AsynchronousLogstashHandler(host, port, database_path=None)
    # Add the handler to the logger
    account_logger.addHandler(async_handler)
    return account_logger

def saveAnymousLog(ip: str, data: list):

    logs = []
    
    for item in data:
        logs.append(item.json())

    logger().info({"ip": ip, "data":logs})