""" 
Syntax: .invite<username>
for all users
Customized by @meanii 
Please Don't remove credit name 
"""

from telethon import functions
from uniborg.util import admin_cmd
from telethon import events


@borg.on(admin_cmd(pattern="invite ?(.*)"))
@borg.on(events.NewMessage(pattern=r"\.invite ?(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.reply("`.invite` users to a chat, not to a Private Message")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
           
            for user_id in to_add_users.split(" "):
                try:
                    await borg(functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id,
                        user_id=user_id,
                        fwd_limit=1000000
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.reply("Invited Successfully")
        else:
           
            for user_id in to_add_users.split(" "):
                try:
                    await borg(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[user_id]
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.reply("Invited Successfully")
