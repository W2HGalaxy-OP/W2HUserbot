from userbot import *
from W2HBOT.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#-------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "W2H User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

aura = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={aura})"


PM_IMG = "https://telegra.ph/file/fd0978ae951f06e2798ec.mp4"
pm_caption ="**W2HBOT Is Online**\n\n"

pm_caption += f"**┏━━━━━━━━━━━━━┓**\n"
pm_caption += f"**┣★ Master : {mention}**\n"
pm_caption += f"**┣★ Telethon : `{version.__version__}`**\n"
pm_caption += f"**┣★ W2HBOT : {W2Hversion}**\n"
pm_caption += f"**┣★ Sudo       : `{sudou}`**\n"
pm_caption += f"**┣★ Channel   : [Join Here](https://t.me/W2H_Userbot)**\n"
pm_caption += f"**┣★ Creater    : [W2H Here](https://t.me/David99q)**\n"
pm_caption += f"**┗━━━━━━━━━━━━━┛**\n"

pm_caption += "    [✨REPO✨](https://github.com/W2HGalaxy-OP/W2HBOT) 🔹 [📜License📜](https://github.com/W2HGalaxy-OP/W2HBOT/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'W2H', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add_info(
  'Zinda Hai Kya Bro?'
).add()
