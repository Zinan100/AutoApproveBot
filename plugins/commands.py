from pyogram import Client as app, filters
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

@app.on_message(filters.command(start))
async def start(bot, msg):
  if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
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

