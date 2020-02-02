""" Command: .porn """

from telethon import events


@borg.on(events.NewMessage(pattern=r"\Downloaded",outgoing=True))
async def song(event):
    if event.fwd_from:
        return
    await event.edit("@songsxd")
    