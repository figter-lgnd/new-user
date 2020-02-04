from telethon import events
import time

"""Command: .bigspamreboot <number> DO NOT TRY THIS WITH YOUR ACCOUNT

telethon.errors.rpcerrorlist.FloodWaitError: A wait of 280 seconds is required"""

@borg.on(events.NewMessage(pattern=r"\.bigspam (.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    for i in range(int(input_str)):
        m = await event.respond("https://telegra.ph/file/e024abfbdc070871b0210.mp4")
        await m.delete()
  
