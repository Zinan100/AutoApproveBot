from pyrogram import Client as app, filters

@app.on_chat_join_request((filters.group | filters.channel))
async def auto_approve(bot, msg):
  chat=msg.chat
  user=msg.from_user
  print(f"{user.first_name} Joined {chat.title}")
  await msg.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
  await message.reply_text(
      chat_id=user.id,
      text="Your Request To {chat.title} was Approved"
  )
