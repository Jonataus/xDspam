# ""ᴅᴇᴀʀ ᴘʀᴏ ᴘᴇᴏᴘʟᴇ,  ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ & ᴄʜᴀɴɢᴇ ᴛʜɪꜱ ʟɪɴᴇ
# ᴛɢ :- @FabinoXD
# ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :- @xDspamBots
# ɢɪᴛʜᴜʙ :- @FabinoXD ""

import os
import sys
import asyncio
from xDspam import (SUDO_USERS, OWNER_ID, ALIVE_PIC)
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


Pic = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/a50a32854921ea49b665f.jpg"
Hn = "/"
btn = InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Channel •", url="https://t.me/EnoughBio"),
                    InlineKeyboardButton(
                        "• Support •", url="https://t.me/DevilsHeavenMF")
                ], [
                    InlineKeyboardButton(
                        "• Repo •", url="https://github.com/The-HellBot/ArrayCore")
                ]]
            )
 
                   
@Client.on_message(filters.private & filters.incoming & filters.command(['start'], prefixes=Hn))
async def _start(_, ok: Message):
    msg = f"**Hello [{ok.from_user.first_name}](tg://user?id={ok.from_user.id}) !** \n\n __ • I'm xDspam An Advance Spambot__ \n\n **Click Below Buttons for More Info**"           
    if ".jpg" in Pic or ".png" in Pic:
              await ok.reply_photo(Pic, caption=msg, reply_markup=btn)
    if ".mp4" in Pic or ".MP4," in Pic:
              await ok.reply_video(Pic, caption=msg, reply_markup=btn)
