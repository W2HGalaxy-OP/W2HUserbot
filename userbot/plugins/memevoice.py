# Credits to @spechide and his team for @TROLLVOICEBOT
# made by @David99q from the snippets of waifu AKA stickerizerbot....
# kang karega kya madarchod?
# aukaat h bsdk teri...jake baap ka loda chus ke aa....


import re

from userbot import bot
from W2HBOT.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
from userbot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(aura):
    W2H = aura.pattern_match.group(1)
    if not W2H:
        if aura.is_reply:
            (await aura.get_reply_message()).message
        else:
            await edit_or_reply(aura, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(W2H))}")

    await troll[0].click(
        aura.chat_id,
        reply_to=aura.reply_to_msg_id,
        silent=True if aura.is_reply else False,
        hide_via=True,
    )
    await aura.delete()
    

CmdHelp("memevoice").add_command(
  "mev", "<meme txt>", "Searches and uploads the meme in voice format (if any)."
).add()