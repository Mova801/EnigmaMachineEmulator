import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.urandom(24).hex()  # os.environ.get('SECRET_KEY')
    HOST = '0.0.0.0'
    # PORT = 8000
