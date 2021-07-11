import asyncio
import random
from userbot.cmdhelp import CmdHelp
from . import *

from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
NUMBER = ["0", "1"]

OS = [
    "IF U NEED ANY HELP U CAN TYPE WHEN HE COME BACK HE WILL REPLY U",
    "PLS DONT DISTURB HIM RAVAN IS BUSY NOW WHEN HE COME BACK HE REPLY U",
    "DON'T BREAK THE HEART OF THE HACKER BCOZ U DON'T KNOW WHAT WILL HAPPN TN",
    "RAVAN IS TOO MUCH BUSY TRY TO UNDERSTAND",
    "I KNOW U ARE WAITING FOR ME I WILL BE BACK SOON",
]

que = {}


@bot.on(admin_cmd(incoming=True))
@bot.on(sudo_cmd(incoming=True, allow_sudo=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.5)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(OS)),
            reply_to=event.message.id,
        )

@bot.on(admin_cmd(pattern="rstarts(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="rstarts(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "GAME")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"RAVAN IS STARTING GAME😁😁😁😁")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "GAME")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"W2H {ALIVE_NAME}")


@bot.on(admin_cmd(pattern="rstops(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="rstops(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "GAME OVER")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"GAME HAS STOPED")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "GAME OVER")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"W2H STOPED RAID {ALIVE_NAME}")
        
        
CmdHelp("rpersonal").add_command(
    'rstarts', None, 'Reply to him or her to start ravan personal file'
).add_command(
    'rstops', None, 'Reply To her Ya him To stop ravan personal file'
).add()
