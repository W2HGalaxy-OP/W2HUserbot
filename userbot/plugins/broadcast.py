import os

from telethon import events
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from . import *
from userbot import bot
from userbot.utils import admin_cmd, edit_or_reply

eor = edit_or_reply

@bot.on(admin_cmd(pattern="gcast(?:\s|$)([\s\S]*)"))
async def gcast(event):
    reply_msg = await event.get_reply_message()
    type = event.text[7:9]
    if reply_msg:
        tol = reply_msg.text
        file = reply_msg.media
    else:
        tol = event.text[9:]
        file = None
    if tol == "":
        return await eor(event, "I need something to Gcast.")
    hol = await eor(event, "Gcasting message...")
    sed = 0
    lol = 0
    if type == "-a":
        async for aman in event.client.iter_dialogs():
            chat = aman.id
            try:
                if chat != -1001551357238:
                    await event.client.send_message(chat, tol, file=file)
                    lol += 1
                elif chat == -1001551357238:
                    pass
            except BaseException:
                sed += 1
    elif type == "-p":
        async for krishna in event.client.iter_dialogs():
            if krishna.is_user and not krishna.entity.bot:
                chat = krishna.id
                try:
                    await event.client.send_message(chat, tol, file=file)
                    lol += 1
                except BaseException:
                    sed += 1
    elif type == "-g":
        async for sweetie in event.client.iter_dialogs():
            if sweetie.is_group:
                chat = sweetie.id
                try:
                    if chat != -1001551357238:
                        await event.client.send_message(chat, tol, file=file)
                        lol += 1
                    elif chat == -1001551357238:
                        pass
                except BaseException:
                    sed += 1
    else:
        return await hol.edit(
            "Please give a flag to Gcast message. \n\nAvailable flags are : \n• -all : To Gcast in all chats. \n• -pvt : To Gcast in private chats. \n• -grp : To Gcast in groups."
        )
    UwU = sed + lol
    if type == "-a":
        omk = "Chats"
    elif type == "-p":
        omk = "PM"
    elif type == "-g":
        omk = "Groups"
    await hol.edit(
        f"Gcast Executed Successfully !! \n\n Sent in : {lol} {omk}\n📍 Failed in : {sed} {omk}\n📍 Total :* {UwU} {omk}"
    )
    
CmdHelp("broadcast").add_command(
   'gcast', "flag", 'Publish message to all channel and group'
).add()
