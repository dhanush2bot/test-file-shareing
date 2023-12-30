import os
from datetime import datetime, timedelta
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Log level for logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Premium user IDs
PREMIUM_USERS = []

# Owner ID
OWNER_ID = int(os.getenv("OWNER_ID", "1764208280"))

# Other configurations...

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")

# ...

# Logging configuration
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=LOG_LEVEL,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


# Function to add a user to premium
def add_premium_user(user_id, days):
    expiry_time = datetime.now() + timedelta(days=days)
    PREMIUM_USERS.append({"user_id": user_id, "expiry_time": expiry_time})
    notify_user(user_id, expiry_time)


# Function to notify the user about premium status
def notify_user(user_id, expiry_time):
    # Add your notification logic here
    pass


# Function to check if a user is premium
def is_premium_user(user_id):
    for user in PREMIUM_USERS:
        if user["user_id"] == user_id:
            return datetime.now() < user["expiry_time"]
    return False
