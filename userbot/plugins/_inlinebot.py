from telethon import version
import asyncio
import html
import os
import re
from math import ceil
from re import compile

from telethon import Button, custom, events, functions
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.users import GetFullUserRequest
from math import ceil
from re import compile

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from W2HBOT.utils import *

from userbot import *
from userbot.cmdhelp import *
from W2HBOT.Config import Config
from userbot.Config import Config
W2H_row = Config.BUTTONS_IN_HELP
W2H_emoji = Config.EMOJI_IN_HELP
from . import ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "W2H User"

aura = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={aura})"

alive_emoji = "❤️"

alive_txt = """
ᴡ2ʜʙᴏᴛ Is ᴘʀᴇsᴇɴᴛɪɴɢ ʙᴇsᴛᴇsᴛ ʙᴏᴛ
  ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
  🔥Bø† Status🔥
**•{}•Owner :** {}
**•{}•W2HBOT :** {}
**•{}•Telethon :** {}
**•{}•Sudo      :** {}
"""
ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"


ALV_PIC = os.environ.get("ALIVE_PIC", None) or "https://telegra.ph/file/4cd888a3491e7ff759bbb.jpg"

W2Hversion = "2.0"

def button(page, modules):
    Row = W2H_row

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(
                    f"{W2H_emoji} " + pair, data=f"Information[{page}]({pair})"
                )
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
                f"⬅️ 𝐁𝐀𝐂𝐊 {W2H_emoji}",
                data=f"page({(max_pages - 1) if page == 0 else (page - 1)})",
            ),
            custom.Button.inline(f"•{W2H_emoji} ❌ {W2H_emoji}•", data="close"),
            custom.Button.inline(
                f"{W2H_emoji} 𝐍𝐄𝐗𝐓 ➡️",
                data=f"page({0 if page == (max_pages - 1) else page + 1})",
            ),
        ]
    )
    return [max_pages, buttons]
    # Changing this line may give error in bot as i added some special cmds in W2HBOT channel to get this module work...

    modules = CMD_HELP


if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@W2H_Userbot":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALV_PIC,
                    text=f"**Running W2HBOT**\n\n__Number of plugins installed__ :`{len(CMD_HELP)}`\n**page:** 1/{veriler[0]}",
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    ALV_PIC,
                    text=f"**Running W2HBOT**\n\n__Number of plugins installed__ :`{len(CMD_HELP)}`\n**page:** 1/{veriler[0]}",
                    title="W2H Help menu",
                    buttons=veriler[1],
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=f"**Running W2HBOT**\n\n__Number of plugins installed__ :`{len(CMD_HELP)}`\n**page:** 1/{veriler[0]}",
                    title="W2H Help",
                    buttons=veriler[1],
                    link_preview=False,
                )
        elif event.query.user_id == bot.uid and query == "alive":
            leg_end = alive_txt.format(
                alive_emoji,
                DEFAULTUSER,
                alive_emoji,
                W2Hversion,
                alive_emoji,
                version.__version__,
                alive_emoji,
                sudou,
            )
            alv_btn = [
                [
                    custom.Button.url(
                        f"Owner", "https://t.me/W2h_ravan"
                    ),
                ],
                [
                    custom.Button.url(
                        f"Support", "https://t.me/W2hsupport"
                    ),
                ],
                [
                    custom.Button.url(
                        f"Chatting", "https://t.me/ravan102030"
                    ),
                ],
            ]
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALV_PIC,
                    text=leg_end,
                    buttons=alv_btn,
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    ALV_PIC,
                    text=leg_end,
                    title="W2H Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=leg_end,
                    title="W2H Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        else:
            result = builder.article(
                "@W2H_Userbot",
                text="""**Hey! This is [W2HBOT.](https://t.me/W2H_Userbot) \nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        custom.Button.url("🔥 CHANNEL 🔥", "https://t.me/W2H_Userbot"),
                        custom.Button.url("⚡ GROUP ⚡", "https://t.me/W2HSupport"),
                    ],
                    [
                        custom.Button.url(
                            "✨ REPO ✨", "https://github.com/W2HGalaxy-OP/W2HBOT"
                        ),
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Mil Gyi Tasalli..? Kabse mere bot me ungli kr rhe h. Khudka bna lo na agr chaiye to pta nhi kaha se aajate h disturb krne. ©W2HBOT™ ",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"**Legenday AF** [W2HBOT](https://t.me/W2H_Userbot) __Working...__\n\n**Number of modules installed :** `{len(CMD_HELP)}`\n**page:** {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=False,
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await delete_W2H(
                event,
                "⚜️W2HBOT Menu Provider Is now Closed⚜️\n\n         **[©W2HBOT](t.me/W2H_Userbot)**",
                5,
                link_preview=False,
            )
        else:
            W2H_alert = "Mil Gyi Tasalli..? Kabse mere bot me ungli kr rhe h. Khudka bna lo na agr chaiye to pta nhi kaha se aajate h disturb krne. ©W2HBOT"
            await event.answer(W2H_alert, cache_time=0, alert=True)

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Mil Gyi Tasalli..? Kabse mere bot me ungli kr rhe h. Khudka bna lo na agr chaiye to pta nhi kaha se aajate h disturb krne. ©W2HBOT ",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "❦ " + cmd[0] + " ❦", data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("◀️ ᏰᎯᏣᏦ", data=f"page({page})")])
        await event.edit(
            f"**📗 File:** `{commands}`\n**🔢 Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Mil Gyi Tasalli..? Kabse mere bot me ungli kr rhe h. Khudka bna lo na agr chaiye to pta nhi kaha se aajate h disturb krne. ©W2HBOT ",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**📗 File:** `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                result += f"**⚠️ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
        else:
            result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"**💬 Explanation:** `{command['usage']}`\n\n"
        else:
            result += f"**💬 Explanation:** `{command['usage']}`\n"
            result += (
                f"**⌨️ For Example:** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"
            )

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("◀️ ᏰᎯᏣᏦ", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )


# Ask owner before using it in your codes
# Kangers like LB stay away...
