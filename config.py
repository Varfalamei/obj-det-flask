import os

bot_owner_id = 275319916
bot_token = "925275676:AAG0SpykgoxkNu8O0YL28M8DVteAj9q_PU8"

class Config(object):
    SECRET_KEY = os.urandom(24)
    MAX_CONTENT_LENGTH = 1024 * 1024 * 16  # for 16MB max-limit.
    # UPLOAD_FOLDER = '/static/photos/'
