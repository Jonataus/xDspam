# ""ᴅᴇᴀʀ ᴘʀᴏ ᴘᴇᴏᴘʟᴇ,  ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ & ᴄʜᴀɴɢᴇ ᴛʜɪꜱ ʟɪɴᴇ
# ᴛɢ :- @FabinoXD
# ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :- @xDspamBots
# ɢɪᴛʜᴜʙ :- @FabinoXD ""

from pyrogram import Client, filters
from pyrogram.types import Message

from xDspam import HNDLR, LOGS_CHANNEL, SUDO_USERS


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR)
)
async def leave(xspam: Client, e: Message):
    HNY = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    if len(e.text) > 7:
        chat = HNY[0]
        try:
            await xspam.leave_chat(chat)
            await e.reply_text("**Left Successfully ✅ **")
        except Exception as ex:
            await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
    else:
        chat = e.chat.id
        ok = e.from_user.id
        if int(chat) == int(ok):
            return await e.reply_text(
                f"Usage: {HNDLR}leave <chat username or id> or {HNDLR}leave (type in Group for Direct leave)"
            )
        if int(chat) == -1001321613309:
            return e.reply_text("**Error**")
        try:
            await xspam.leave_chat(chat)
            await e.reply_text("**Left Successfully ✅ **")
        except Exception as ex:
            await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
        if LOGS_CHANNEL:
            try:
                await xspam.send_message(
                    LOGS_CHANNEL,
                    f"Leaved Chat \n\n Chat: {chat} \n Cmd By User: {e.from_user.id}",
                )
            except Exception as a:
                print(a)
