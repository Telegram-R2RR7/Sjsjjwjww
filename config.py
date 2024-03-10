from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/0078467a38a2386dda832.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/0078467a38a2386dda832.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/zzwm12")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/zzwm12")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2038302618").split()))


CHANNEL_SUDO = getenv(
    "CHANNEL_SUDO", "zzwm12"
)

YAFA_NAME = getenv(
    "YAFA_NAME", "انمي"
)

YAFA_CHANNEL = getenv(
   " YAFA_CHANNEL", "https://t.me/zzwm12" 
)


FAILED = "https://telegra.ph/file/0078467a38a2386dda832.jpg"
