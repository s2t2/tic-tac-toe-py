


import os

from dotenv import load_dotenv

load_dotenv() # read env vars from the ".env" file

APP_ENV = os.getenv("APP_ENV", default="development")

APP_VERSION = "1.0"

OPPOSITE_LETTERS = {"X": "O", "O": "X"}
