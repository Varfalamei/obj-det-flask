import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MAX_CONTENT_LENGTH = 1024 * 1024 * 16  # for 16MB max-limit.
    # UPLOAD_FOLDER = '/static/photos/'
