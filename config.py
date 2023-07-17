import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "5433537770:AAEs5_y6wFIuBDkjPmRWcjQGZ7FbL3VZ3ZY")
      API_ID = int(os.environ.get("API_ID", 12210813))
      API_HASH = os.environ.get("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad1")
      OWNER_ID = int(os.environ.get("OWNER_ID", "123559329"))

