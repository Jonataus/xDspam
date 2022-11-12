import os
import asyncio

from xDspam import SUDO_USERS
from xDspam.data import EYE

from pyrogram.types import Message
from pyrogram import filters, Client


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["eye"], ["."]))
async def eye(client, m: Message):
    if m.reply_to_message:
        if m.reply_to_message.from_user.id in SUDO_USERS:
            return await m.reply_text("ᴀʏᴇ ᴍᴀᴅʜᴀʀᴄʜᴏᴅ ᴀᴘɴᴀ ᴋᴀᴀᴍ ᴋᴀʀ ɴᴀ")
        else:
            sex = await m.reply_to_message.reply_text("👁👁\n\n  👄  =====> Abey Ja Na Gandu")
    else:
        sex = await m.reply_text("👁👁\n\n  👄  =====> Abey Ja Na Gandu")
    for x in range(0, 7):
        await asyncio.sleep(2)
        await sex.edit_text(EYE[x % 8])