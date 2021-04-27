from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from W2HBOT import bot, CmdHelp
from W2HBOT.utils import admin_cmd, edit_or_reply as eor, sudo_cmd

@W2HBOT.on(admin_cmd(pattern="history ?(.*)"))
@W2HBOT.on(sudo_cmd(pattern="history ?(.*)", allow_sudo=True))
async def _(W2Hevent):
    if W2Hevent.fwd_from:
        return 
    if not W2Hevent.reply_to_msg_id:
       await eor(W2Hevent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await W2Hevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eor(W2Hevent, "Need actual users. Not Bots")
       return
    await eor(W2Hevent, "Checking...")
    async with W2Hevent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await W2Hevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await eor(W2Hevent, "User never changed his Username...")
          else: 
             await W2Hevent.delete()
             await W2Hevent.client.send_message(W2Hevent.chat_id, response2.message)

@W2HBOT.on(admin_cmd(pattern="unh ?(.*)"))
@W2HBOT.on(sudo_cmd(pattern="unh ?(.*)", allow_sudo=True))
async def _(W2Hevent):
    if W2Hevent.fwd_from:
        return 
    if not W2Hevent.reply_to_msg_id:
       await eor(W2Hevent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await W2Hevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eor(W2Hevent, "Need actual users. Not Bots")
       return
    await eor(W2Hevent, "Checking...")
    async with W2Hevent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await W2Hevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await eor(W2Hevent, "User never changed his Username...")
          else: 
             await W2Hevent.delete()
             await W2Hevent.client.send_message(W2Hevent.chat_id, response3.message)

CmdHelp("history").add_command(
  "history", "<reply to a user>", "Fetches the name history of replied user."
).add_command(
  "unh", "<reply to user>", "Fetches the Username History of replied users."
).add()
