# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


from telethon.errors import ChatSendInlineForbiddenError
from telethon.errors.rpcerrorlist import BotMethodInvalidError as bmi

from . import *

REPOMSG = (
    "• **Googleboy's USERBOT** •\n\n",
    "• Repo - [Click Here](https://github.com/mr-googleboy/Ultroid/)\n",
    "• Addons - [Click Here](https://telegram.me/feedbuzzme)\n",
    "• Support - @UltroidSupport",
)


@ultroid_cmd(pattern="repo$")
async def repify(e):
    try:
        q = await ultroid_bot.inline_query(asst.me.username, "repo")
        await q[0].click(e.chat_id)
        if e.sender_id == ultroid_bot.uid:
            await e.delete()
    except ChatSendInlineForbiddenError or bmi:
        await eor(e, REPOMSG)
