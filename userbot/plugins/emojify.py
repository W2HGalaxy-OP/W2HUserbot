
from userbot import bot

from userbot.utils import edit_or_reply ,admin_cmd 
from userbot.helpers import fonts as emojify
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern=r"emotes ?(.*)"))
async def itachi(event):
    "To get emoji art text."
    args = event.pattern_match.group(1)
    get = await event.get_reply_message()
    if not args and get:
        args = get.text
    if not args:
        await edit_or_reply(
            event, "__What am I Supposed to do with this idiot, Give me a text.__"
        )
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.kakashiemoji[emojify.kakashitext.index(a)]
            result += char
        else:
            result += a
    await edit_or_reply(event, result)


@bot.on(admin_cmd(pattern=r"cemotes ?(.*)"))
async def itachi(event):
    "To get custom emoji art text."
    args = event.pattern_match.group(1)
    get = await event.get_reply_message()
    if not args and get:
        args = get.text
    if not args:
        return await edit_or_reply(
            event, "__What am I Supposed to do with this idiot, Give me a text.__"
        )
    try:
        emoji, arg = args.split(" ", 1)
    except Exception:
        arg = args
        emoji = "😺"
    result = ""
    for a in arg:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.itachiemoji[emojify.kakashitext.index(a)].format(cj=emoji)
            result += char
        else:
            result += a
    await edit_or_reply(event, result)

  
CmdHelp("emojify").add_command(
    "emotes", "<text>", "Use and See"
).add_command(
    "cemotes", "<text>", "Use and See"
).add()
    
