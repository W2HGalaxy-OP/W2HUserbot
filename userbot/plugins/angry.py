import asyncio
from collections import deque

from . import *


@bot.on(admin_cmd(pattern=r"^🤬", outgoing=True))
@bot.on(sudo_cmd(pattern=r"^🤬", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "𝙸 𝚊𝚖 𝚊𝚗𝚐𝚛𝚢 ")
    deq = deque(list("😡🔥😡🔥😡🔥😡"))
    for _ in range(50):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(1)


import asyncio
from collections import deque

from . import *


@bot.on(admin_cmd(pattern=r"^🤣", outgoing=True))
@bot.on(sudo_cmd(pattern=r"^🤣", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Lots Of Laugh")
    deq = deque(list("🤣😂😅😆😃😄😁😊"))
    for _ in range(50):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(1)


CmdHelp("angry").add_command("🤬", None, "υѕє αи∂ ѕєє ex - 🤬").add_command(
    "🤣", None, "Use and See"
).add()
