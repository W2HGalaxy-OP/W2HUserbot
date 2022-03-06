from telethon import events

from userbot import *

from . import *

PM_IMG = "https://telegra.ph/file/b89e26622fab4b5b1dfeb.jpg"


pm_caption = f"⚜『W2Hẞø†』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{ALIVE_NAME}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『W2Hẞø†』~ `{LEGENDversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/W2H_userbot)\n"
pm_caption += f"┣Copyright ~ By [『W2Hẞø†』 ](https://t.me/W2HSupport)\n"
pm_caption += f"┣Assistant ~ By [『W2Hẞøy』 ](https://t.me/RAVAN102030)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [W2Hẞø†](https://t.me/W2HSUPPORT) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
