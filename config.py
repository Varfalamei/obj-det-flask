import os

class Config(object):
    SECRET_KEY = os.urandom(24)
    MAX_CONTENT_LENGTH = 1024 * 1024 * 16  # for 16MB max-limit.
    # UPLOAD_FOLDER = '/static/photos/'
