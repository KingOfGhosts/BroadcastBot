import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6475835405:AAEqKHDhEHE24_pPt5mxFCqgApfhAXwsksg")
API_ID = int(os.environ.get("API_ID", "12192489"))
API_HASH = os.environ.get("API_HASH", "ed39e721f5d4fd6d3c05121c1661b8ea")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002236362534"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5097048997").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Priyanshu:Priyanshu@cluster0.zlp9qrl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Broadcast")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
