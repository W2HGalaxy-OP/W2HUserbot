from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from AuraXBot import bot, CmdHelp
from AuraXBot.utils import admin_cmd, edit_or_reply as eor, sudo_cmd

@AuraXBot.on(admin_cmd(pattern="history ?(.*)"))
@AuraXBot.on(sudo_cmd(pattern="history ?(.*)", allow_sudo=True))
async def _(AuraXevent):
    if AuraXevent.fwd_from:
        return 
    if not AuraXevent.reply_to_msg_id:
       await eor(AuraXevent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await AuraXevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eor(AuraXevent, "Need actual users. Not Bots")
       return
    await eor(AuraXevent, "Checking...")
    async with AuraXevent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await AuraXevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await eor(AuraXevent, "User never changed his Username...")
          else: 
             await AuraXevent.delete()
             await AuraXevent.client.send_message(AuraXevent.chat_id, response2.message)

@AuraXBot.on(admin_cmd(pattern="unh ?(.*)"))
@AuraXBot.on(sudo_cmd(pattern="unh ?(.*)", allow_sudo=True))
async def _(AuraXevent):
    if AuraXevent.fwd_from:
        return 
    if not AuraXevent.reply_to_msg_id:
       await eor(AuraXevent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await AuraXevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eor(AuraXevent, "Need actual users. Not Bots")
       return
    await eor(AuraXevent, "Checking...")
    async with AuraXevent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await AuraXevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await eor(AuraXevent, "User never changed his Username...")
          else: 
             await AuraXevent.delete()
             await AuraXevent.client.send_message(AuraXevent.chat_id, response3.message)

CmdHelp("history").add_command(
  "history", "<reply to a user>", "Fetches the name history of replied user."
).add_command(
  "unh", "<reply to user>", "Fetches the Username History of replied users."
).add()
