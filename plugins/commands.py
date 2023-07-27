from pyogram import Client as app, filters
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

@app.on_message(filters.command(start))
async def start(bot, msg):
  hu = await bot.get_me()
  btn = [[
    Button('Channel', url='zib_bots'),
    Button('Group', url='zib_discussion')
    ],[
    Button("Add me to your group or Channel', url='https://t.me/{hu}?startgroup=start')
  ]]      
  await msg.reply_text(
    text=START_TXT,
    reply_markup=Markup(btn),
    disable_web_page_preview=True
  )

