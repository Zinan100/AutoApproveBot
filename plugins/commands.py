from pyogram import Client as app, filters
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from Script import *
from info import *

@app.on_message(filters.command(start))
#kanged from eva maria
if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        buttons = [[
                    Button("Updates", url="t.me/zib_bots")
        reply_markup = Markup(buttons)
        await message.reply_text(
            text=GSTART_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:  hu = await bot.get_me()
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

