import re
from os import getenv
import os
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

# Get it from @Botfather in Telegram
BOT_TOKEN = getenv("BOT_TOKEN")

# Database to save your chats and stats
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "3000"))

EXTRA_PLUGINS = getenv("EXTRA_PLUGINS", "False")
EXTRA_PLUGINS_REPO = getenv("EXTRA_PLUGINS_REPO", "https://github.com/Highpower143/ExtraPlugin")
EXTRA_PLUGINS_FOLDER = getenv("EXTRA_PLUGINS_FOLDER", "plugins")

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1000"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002223516578"))

OWNER_ID = list(map(int, getenv("OWNER_ID", "6972508083").split()))

PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-VIPMUSIC-08-30")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# Fixed upstream repo and branch
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Highpower143/NobitaBro")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# GIT TOKEN for private repos
GIT_TOKEN = getenv("GIT_TOKEN", "")

if UPSTREAM_REPO:
    if not re.match(r"(?:http|https)://", UPSTREAM_REPO):
        raise ValueError("[ERROR] - Your UPSTREAM_REPO URL is invalid. It must start with https://")

if GIT_TOKEN and "github.com" in UPSTREAM_REPO:
    UPSTREAM_REPO = UPSTREAM_REPO.replace("https://", f"https://{GIT_TOKEN}@")

AUTO_GCAST = os.getenv("AUTO_GCAST", "on")
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Lucky_jet_game_signal")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Betting_Fantasy_Tips")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", 1800))

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/vishalpandeynkp/VIPNOBITAMUSIC_REPO")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "999"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "500"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "500"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "1073741824"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

SET_CMDS = getenv("SET_CMDS", "False")

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "VIPlogs.txt"
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

# Images
START_IMG_URL = getenv("START_IMG_URL", "https://envs.sh/ctj.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://envs.sh/ctj.jpg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "https://envs.sh/ctj.jpg")
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL", "https://envs.sh/ctj.jpg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://envs.sh/ctj.jpg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "https://envs.sh/ctj.jpg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "https://envs.sh/ctj.jpg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "https://envs.sh/ctj.jpg")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", "https://envs.sh/ctj.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://envs.sh/ctj.jpg")

SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "https://envs.sh/ctj.jpg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "https://envs.sh/ctj.jpg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "https://envs.sh/ctj.jpg")


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))
