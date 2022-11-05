import os
import sys
from random import choice
from xDspam import (OWNER_ID, HNDLR, SUDO_USERS, hl, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message
from xDspam.data import *

Usage = f"**❌ Wrong Usage ❌** \n Type: `{HNDLR}help owner`"
Media = "xDspam/downloads/Profile.jpg"

@Client.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["setpic"], prefixes=HNDLR))
async def setpic(xspam: Client, e: Message):
     replied = e.reply_to_message
     if (replied and replied.media and (replied.photo or (replied.document and "image" in replied.document.mime_type))):
            await xspam.download_media(message=replied, file_name=Media)
            await xspam.set_profile_photo(photo=Media)
            await e.reply_text(f"**Changed profile picture successfully** ✅")
            if os.path.exists(Media):
                  os.remove(Media)
     else:
         await e.reply_text("Reply To any Photo To Change Profile pic")
     if LOGS_CHANNEL:
         try:
              await Client.send_message(LOGS_CHANNEL, f"Profile Pic Changed By User: {e.from_user.id}")
         except Exception as a:
             print(a)
             pass
      
etc_bio = "𝐱𝐃 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭𝐬 ! 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 - @DevilsHeavenMF"

@Client.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["setname"], prefixes=HNDLR))
async def setname(xspam: Client, e: Message): 
      HNY = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(HNY) == 1:
          name = str(HNY[0])
          try:
            await xspam.update_profile(first_name=name, bio=etc_bio)
            await e.reply_text(f"**Profile Name Changed Successfully !!** \n\n **New Name:** {name}")
          except Exception as ex:
            await e.reply_text(f"**Error !!** \n\n {ex}")
            print(ex)
      else:
          await e.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
             await xspam.send_message(LOGS_CHANNEL, f"Name Changed By User {e.from_user.id} \n\n New Name: {name}")
         except Exception as a:
             print(a)
             pass

@Client.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["setbio"], prefixes=HNDLR))
async def setbio(xspam: Client, e: Message):
      HNY = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(HNY) == 1:
          xd = str(HNY[0])
          ok = await xspam.get_me()
          nam = ok.first_name
          nam2 = ok.last_name
          try:
             await xspam.update_profile(first_name=nam, last_name=nam2, bio=xd)
             await e.reply_text(f"**Profile Bio Changed Successfully !** \n\n **New Bio**: {xd}")
          except Exception as ex:
            await e.reply_text(f"**Error !!** \n\n {ex}")
            print(ex)
      else:
          await e.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
             await xspam.send_message(LOGS_CHANNEL, f"Bio Changed By User: {e.from_user.id} \n\n New Bio: {xd}")
         except Exception as a:
             print(a)
             pass
