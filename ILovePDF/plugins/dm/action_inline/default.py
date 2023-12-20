# This module is part of https://telegramic.org/bot/i2pdfbot/
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/plugins/dm/action_inline/default.py"

from . import *
from plugins.utils import *
from pyrogram.types import (
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultArticle,
)


async def default_ans(inline_query) -> list:
    try:
        lang_code = await util.getLang(inline_query.from_user.id)
        CHUNK, _ = await util.translate(text="INLINE", lang_code=lang_code)

        # Getting Lang Data..
        BUTTON = CHUNK["lang_b"]
        _lang = {
            langList[lang][
                1
            ]: f"https://t.me/{myID[0].username}?start=-l{lang}-r{inline_query.from_user.id}"
            for lang in langList
        }
        BUTTON.update(_lang)
        BUTTON.update({"♻": "-|refresh"})
        BUTTON = await util.createBUTTON(
            btn=BUTTON, order=int(f"1{((len(BUTTON)-2)//2)*'2'}{(len(BUTTON)-2)%2}1")
        )

        answer = [
            InlineQueryResultArticle(
                thumb_url="https://i.imgur.com/NmKgTrk.png",
                title=CHUNK["sear_t"],
                description=CHUNK["sear_d"],
                input_message_content=InputTextMessageContent(CHUNK["sear_d"]),
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text=CHUNK["search"], switch_inline_query_current_chat="",)
                    ]]
                ),
            ),
            InlineQueryResultArticle(
                thumb_url="https://i.imgur.com/vXzBL0G.png",
                title=CHUNK["lang_t"],
                reply_markup=BUTTON,
                description=CHUNK["lang_d"],
                input_message_content=InputTextMessageContent(CHUNK["lang_d"]),
            ),
            InlineQueryResultArticle(
                thumb_url="https://i.imgur.com/tRqsigZ.png",
                title=CHUNK["refer_t"],
                description=CHUNK["refer_d"],
                input_message_content=InputTextMessageContent(
                    f"[@{myID[0].username}](https://t.me/{myID[0].username}?start=-r{inline_query.from_user.id})",
                    disable_web_page_preview=True,
                ),
            ),
            InlineQueryResultArticle(
                thumb_url="https://i.imgur.com/ylUGuxH.png",
                title="🌟rate bot 🌟",
                description="About bot..",
                input_message_content=InputTextMessageContent(
                    f"https://telegramic.org/bot/i2pdfbot/",
                    disable_web_page_preview=True,
                ),
            ),
        ]

        return answer
    except Exception as Error:
        logger.exception("🐞 %s: %s" % (file_name, Error), exc_info=True)


async def search(inline_query) -> list:
    try:
        lang_code = await util.getLang(inline_query.from_user.id)
        CHUNK, _ = await util.translate(text="INLINE", lang_code=lang_code)

        answer = [
            InlineQueryResultArticle(
                thumb_url="https://i.imgur.com/NmKgTrk.png",
                title=CHUNK["sear_t"],
                description=CHUNK["sear_d"],
                input_message_content=InputTextMessageContent(CHUNK["sear_d"]),
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(text=CHUNK["search"],
                            switch_inline_query_current_chat=f"{inline_query.query.split('|')[1]}",)
                    ]]
                ),
            )
        ]

        return answer
    except Exception as Error:
        logger.exception("🐞 %s: %s" % (file_name, Error), exc_info=True)

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!   XD
