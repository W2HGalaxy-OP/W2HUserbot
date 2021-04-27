import time

from telethon import version
from userbot import ALIVE_NAME, StartTime, W2Hversion
from W2HBOT.utils import admin_cmd, edit_or_reply, sudo_cmd


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "W2H User"
W2H_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "Legend's Choice W2HBot"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="w2h$"))
@bot.on(sudo_cmd(pattern="w2h$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if W2H_IMG:
        W2H_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        W2H_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        W2H_caption += f"     __**BOT STATUS**__\n\n"
        W2H_caption += f"**★ Telethon version :** `{version.__version__}`\n"
        W2H_caption += f"**★ W2HBOT :**`{W2Hversion}`\n"
        W2H_caption += f"**★ Uptime :** `{uptime}\n`"
        W2H_caption += f"**★ Master:** {mention}\n"
        await alive.client.send_file(
            alive.chat_id, W2H_IMG, caption=W2H_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"      __**BOT STATUS**__\n\n"
            f"**★ Telethon Version :** `{version.__version__}`\n"
            f"**★ W2HBOT:** `{W2Hversion}`\n"
            f"**★ Uptime :** `{uptime}\n`"
            f"**★ Master:** {mention}\n",
        )
