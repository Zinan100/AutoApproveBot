from pyrogram import Client, filters
from info import *

Client = app(
  "Auto Req Acceptor Bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
  plugins={"root": "plugins"}
)




app.run()
