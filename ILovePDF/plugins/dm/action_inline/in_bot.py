# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/plugins/dm/action_inline/in_bot.py"


from . import *
from plugins.utils import *
from pyrogram.enums import MessageMediaType


async def download(current, total, bot, message):
    try:
        await message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "📥 DOWNLOADED(تنزيل) {:.2f}% 📥".format(current / total * 100),
                        callback_data="https://t.me/i2pdfbotchannel",)
                ]]
            )
        )
    except errors.MessageNotModified as e:
        logger.debug("🐞 %s: %s" % (file_name, e))
    except errors.FloodWait as e:
        logger.debug("🐞 %s: %s" % (file_name, e))
        await asyncio.sleep(e.x)
    except Exception as e:
        logger.exception("🐞 %s: %s" % (file_name, e), exc_info=True)


async def openInBot(bot, message, md5: Union[str, int]) -> bool:
    try:
        lang_code = await getLang(message.chat.id)
        trCHUNK, _ = await translate(text="INLINE", lang_code=lang_code)

        if md5.isdigit():
            getMSG = await bot.get_messages(
                chat_id=int(log.LOG_CHANNEL), message_ids=int(md5)
            )
            if getMSG.empty or getMSG.media != MessageMediaType.PHOTO:
                return await messaage.reply(trCHUNK["old"])
            md5 = getMSG.caption.splitlines()[0].split(":")[1].strip()

        if await work.work(message, "check", True):
            return await message.reply(
                text=trCHUNK["inWork"],
                quote=True,
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            "♻", callback_data=f"refresh{f'-m{md5}' if isinstance(md5, int) else ''}",)
                    ]]
                ),
            )
        cDIR = await work.work(message, "create", True)

        markup = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "⚠️ DOWNLOADING(تنزيل) ⚠️", url="https://t.me/i2pdfbotchannel")
            ]]
        )
        data = await Libgen().search(
            query=md5,
            search_field="md5",
            return_fields=[
                "title",
                "author",
                "publisher",
                "year",
                "language",
                "volumeinfo",
                "filesize",
                "extension",
                "timeadded",
                "timelastmodified",
                "coverurl",
            ],
        )
        caption = ""
        for key, value in data[list(data.keys())[0]].items():
            if key in ["coverurl", "timeadded", "timelastmodified"] or value == "":
                continue
            caption += f"{key}: **{value}**\n"
        reply = await message.reply_photo(
            data[list(data.keys())[0]]["coverurl"], caption=caption, reply_markup=markup
        )

        link = f"http://library.lol/main/{md5}"
        file = await Libgen().download(
            link, dest_folder=cDIR, progress=download, progress_args=[bot, reply]
        )

        await reply.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "🐍 STARTED UPLOADING 🐍", callback_data="https://t.me/i2pdfbotchannel",)
                ]]
            )
        )

        await reply.reply_document(
            document=file,
            caption=caption,
            progress=render.cbPRO,
            progress_args=(reply, 0, "UPLOADED", True),
        )

        await reply.edit_reply_markup(reply_markup=None)
        return await work.work(message, "delete", True)
    except Exception as e:
        logger.exception("🐞 %s: %s" % (file_name, e), exc_info=True)
        return await work.work(message, "delete", True)

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
