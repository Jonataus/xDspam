# ""ᴅᴇᴀʀ ᴘʀᴏ ᴘᴇᴏᴘʟᴇ,  ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ & ᴄʜᴀɴɢᴇ ᴛʜɪꜱ ʟɪɴᴇ
# ᴛɢ :- @FabinoXD
# ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :- @xDspamBots
# ɢɪᴛʜᴜʙ :- @FabinoXD ""

import asyncio
from random import choice

from pyrogram import Client, filters
from pyrogram.types import Message

from xDspam import HNDLR, LOGS_CHANNEL, OWNER_ID, SUDO_USERS
from xDspam.data import *

Usage = f"**❌ Wrong Usage ❌** \n Type: `{HNDLR}help dm`"


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR)
)
async def dmraid(xspam: Client, e: Message):
    """Module: Dm Raid"""
    HNY = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    if len(HNY) == 2:
        ok = await xspam.get_users(HNY[1])
        id = ok.id
        if int(id) in EnoughBio:
            text = f"I can't raid on @EnoughBio's Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is The Owner Of these Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is sudo user."
            await e.reply_text(text)
        else:
            counts = int(HNY[0])
            await e.reply_text("⚜️ Dm Raid Started Successfully ⚜️")
            for _ in range(counts):
                reply = choice(RAID)
                msg = f"{reply}"
                await xspam.send_message(id, msg)
                await asyncio.sleep(0.10)
    elif e.reply_to_message:
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if int(id) in EnoughBio:
            text = f"I can't raid on @EnoughBio's Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is The Owner Of these Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is sudo user."
            await e.reply_text(text)
        else:
            counts = int(HNY[0])
            await e.reply_text("⚜️ Dm Raid Started Successfully ⚜️")
            for _ in range(counts):
                reply = choice(RAID)
                msg = f"{reply}"
                await xspam.send_message(id, msg)
                await asyncio.sleep(0.10)
    else:
        await xspam.reply_text(Usage)
    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"started DM Raid By User: {e.from_user.id} \n\n On User: {id} \n Counts: {counts}",
            )
        except Exception as a:
            print(a)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
async def dm(xspam: Client, e: Message):
    HNY = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    if len(HNY) == 2:
        usr = str(HNY[0])
        ok = await xspam.get_users(usr)
        id = ok.id
        if int(id) in EnoughBio:
            text = f"I can't raid on @EnoughBio's Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is the Owner Of these Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is sudo user."
            await e.reply_text(text)
        else:
            msg = str(HNY[1])
            await e.reply_text("🔸 Message Delivered 🔸")
            await xspam.send_message(id, msg)
    elif e.reply_to_message:
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if int(id) in EnoughBio:
            text = f"I can't raid on @EnoughBio's Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is The Owner Of these Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is sudo user."
            await e.reply_text(text)
        else:
            msg = str(HNY[0])
            await e.reply_text("🔸 Message Delivered 🔸️")
            await xspam.send_message(id, msg)
    else:
        await xspam.reply_text(Usage)
    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"Direct Message By User: {e.from_user.id} \n\n On User: {id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR)
)
async def dmspam(xspam: Client, e: Message):
    HNY = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    HNYop = HNY[1:]
    if len(HNYop) == 2:
        msg = str(HNYop[1])
        ok = await xspam.get_users(HNY[0])
        id = ok.id
        if int(id) in EnoughBio:
            text = f"I can't raid on @EnoughBio's Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is The Owner Of these Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is sudo user."
            await e.reply_text(text)
        else:
            counts = int(HNYop[0])
            await e.reply_text("☢️ Dm Spam Started ☢️")
            for _ in range(counts):
                await xspam.send_message(id, msg)
                await asyncio.sleep(0.10)
    elif e.reply_to_message:
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if int(id) in EnoughBio:
            text = f"I can't raid on @EnoughBio's Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is the Owner Of these Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is sudo user."
            await e.reply_text(text)
        else:
            counts = int(HNY[0])
            msg = str(HNYop[0])
            await e.reply_text("☢️ Dm Spam Started ☢️")
            for _ in range(counts):
                await xspam.send_message(id, msg)
                await asyncio.sleep(0.10)
    else:
        await xspam.reply_text(Usage)
    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"started DM Spam By User: {e.from_user.id} \n\n On User: {id} \n Counts: {counts} \n Message: {msg}",
            )
        except Exception as a:
            print(a)
