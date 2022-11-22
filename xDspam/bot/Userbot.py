# ""ᴅᴇᴀʀ ᴘʀᴏ ᴘᴇᴏᴘʟᴇ,  ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ & ᴄʜᴀɴɢᴇ ᴛʜɪꜱ ʟɪɴᴇ
# ᴛɢ :- @FabinoXD
# ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :- @xDspamBots
# ɢɪᴛʜᴜʙ :- @FabinoXD ""

import datetime
import os
import sys
import time

from pyrogram import Client
from pyrogram import __version__ as pyro_vr
from pyrogram import filters
from pyrogram.types import Message

from xDspam import (
    ALIVE_MSG,
    ALIVE_PIC,
    HNDLR,
    PING_MSG,
    SUDO_USERS,
    __version__,
    start_time,
)

pongg = PING_MSG if PING_MSG else "ᴢɪɴᴅᴀ ʜᴜ ʙᴀʙʏ....."
LUL_PIC = (
    ALIVE_PIC if ALIVE_PIC else "https://telegra.ph//file/ade7408323919332f2e09.jpg"
)
Alivemsg = ALIVE_MSG if ALIVE_MSG else "𝗭𝗶𝗡𝗗𝗮 𝗛𝘂 𝗕𝗮𝗯𝘆....."


HNY = f"⁂ {Alivemsg} ⁂\n\n"
HNY += f"━───────╯•╰───────━\n"
HNY += f"➠ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.10.4`\n"
HNY += f"➠ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ** : `{pyro_vr}`\n"
HNY += f"➠ **xᴅꜱᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{__version__}`\n"
HNY += f"➠ **ᴄʜᴀɴɴᴇʟ** : [Join.](https://t.me/EnoughBio)\n"
HNY += f"━───────╮•╭───────━\n\n"
HNY += f"➠ **Source Code:** [•Repo•](https://github.com/EnoughBio/xDspam)"


async def get_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
async def ping(_, e: Message):
    start = datetime.datetime.now()
    uptime = await get_time((time.time() - start_time))
    Fuk = await e.reply("**Pong !!**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await Fuk.edit_text(
        f"⌾ {pongg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}` \n ༝ ᴠᴇʀsɪᴏɴ: `{__version__}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR)
)
async def alive(xspam: Client, e: Message):
    if ".jpg" in LUL_PIC or ".png" in LUL_PIC:
        await xspam.send_photo(e.chat.id, LUL_PIC, caption=HNY)
    if ".mp4" in LUL_PIC or ".MP4," in LUL_PIC:
        await xspam.send_video(e.chat.id, LUL_PIC, caption=HNY)


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart", "reboot"], prefixes=HNDLR)
)
async def reboot(xspam: Client, e: Message):
    reboot_text = "**Re-starting** \n\n __Wait For A While To Use it Again__ "
    await e.reply_text(reboot_text)
    try:
        xspam.disconnect()
    except Exception:
        pass
    args = [sys.executable, "-m", "xDspam"]
    os.execl(sys.executable, *args)
    quit()
