from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/ee6ce6991f3ca199517bf.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/ee6ce6991f3ca199517bf.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/R125R")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/R125R")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5296856785").split()))


CHANNEL_SUDO = getenv(
    "CHANNEL_SUDO",
)

YAFA_NAME = getenv(
    "YAFA_NAME",
)

YAFA_CHANNEL = getenv(
   " YAFA_CHANNEL", 
)


FAILED = "https://telegra.ph/file/ee6ce6991f3ca199517bf.jpg"
