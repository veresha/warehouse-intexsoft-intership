import os

# DB_USER = os.environ['DB_USER']
# DB_PASSWORD = os.environ['DB_PASSWORD']
# HOST_ADDRESS = os.environ['HOST_ADDRESS']
# DB_NAME = os.environ['DB_NAME']
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
HOST_ADDRESS = os.getenv('HOST_ADDRESS', '172.17.0.1:5430')
DB_NAME = os.getenv('DB_NAME', 'test_table')
RABBITMQ_BROKER = os.getenv('RABBITMQ_BROKER', 'amqp://guest:guest@localhost:5672/')
