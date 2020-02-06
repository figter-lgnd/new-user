"""
For all user
Syntax: .qbot with reply
Made by @meanii 
Please Don't remove credit name 
"""
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="anii(.*)"))
@borg.on(events.NewMessage(pattern=r"\.anii(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return 
    
    if not event.reply_to_msg_id:
       await event.reply("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.reply("```Reply to text message```")
       return
    await event.delete()
    process = await event.reply("```Converting...```")
    await process.delete()
    chat = "@asticker2vid_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.reply("```Reply to actual users message.```")
       return
    
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=984498642))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock me (@asticker2vid_bot)```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
