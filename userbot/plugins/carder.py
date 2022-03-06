from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from W2HBOT.utils import admin_cmd, edit_or_reply, sudo_cmd

from W2HBOT import CmdHelp
from W2HBOT import bot as W2HBOT


@W2HBOT.on(admin_cmd("gencc$"))
@W2HBOT.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(W2Hevent):
    if W2Hevent.fwd_from:
        return
    W2Hcc = Faker()
    W2Hname = W2Hcc.name()
    W2Hadre = W2Hcc.address()
    W2Hcard = W2Hcc.credit_card_full()

    await edit_or_reply(
        W2Hevent,
        f"__**👤 NAME :- **__\n`{W2Hname}`\n\n__**🏡 ADDRESS :- **__\n`{W2Hadre}`\n\n__**💸 CARD :- **__\n`{W2Hcard}`",
    )


@W2HBOT.on(admin_cmd(pattern="bin ?(.*)"))
@W2HBOT.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    W2H_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/bin {W2H_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@W2HBOT.on(admin_cmd(pattern="vbv ?(.*)"))
@W2HBOT.on(sudo_cmd(pattern="vbv ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    W2H_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/vbv {W2H_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@W2HBOT.on(admin_cmd(pattern="key ?(.*)"))
@W2HBOT.on(sudo_cmd(pattern="key ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    W2H_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/key {W2H_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@W2HBOT.on(admin_cmd(pattern="iban ?(.*)"))
@W2HBOT.on(sudo_cmd(pattern="iban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    W2H_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/iban {W2H_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@W2HBOT.on(admin_cmd(pattern="ccheck ?(.*)"))
@W2HBOT.on(sudo_cmd(pattern="ccheck ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    W2H_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/ss {W2H_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@W2HBOT.on(admin_cmd(pattern="ccbin ?(.*)"))
@W2HBOT.on(sudo_cmd(pattern="ccbin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    W2H_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit(f"Trying to generate CC from the given bin `{W2H_input}`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/gen {W2H_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CmdHelp("carder").add_command("gencc", None, "Generates fake cc...").add_command(
    "ccheck", "<query>", "Checks that the given cc is live or not"
).add_command(
    "iban", "<query>", "Checks that the given IBAN ID is live or not"
).add_command(
    "key", "<query>", "Checks the status of probided key"
).add_command(
    "vbv", "<query>", "Checks the vbv status of given card"
).add_command(
    "bin", "<query>", "Checks that the given bin is valid or not"
).add_command(
    "ccbin", "<bin>", "Generates CC from the given bin."
).add()
