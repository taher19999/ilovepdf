# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/plugins/dm/action_inline/search_query.py"

from . import *
from plugins.utils.util import *
from .default import default_ans, search
from pyrogram.types import (
    InlineQueryResultPhoto,
    InlineQueryResultCachedDocument,
)


@ILovePDF.on_inline_query()
async def inline_query_handler(bot, inline_query):
    try:
        query = inline_query.query.strip()
        results = []

        lang_code = await getLang(inline_query.from_user.id)
        trCHUNK, _ = await translate(text="INLINE", lang_code=lang_code)

        # Inline feature will not work if there is no log channel set up.
        if not log.LOG_CHANNEL:
            result = await default_ans(inline_query)
            return await inline_query.answer(
                results=result,
                cache_time=0,
                switch_pm_text=trCHUNK["noDB"],
                switch_pm_parameter="okay",
            )

        elif len(query) < 2:
            result = await default_ans(inline_query)
            return await inline_query.answer(
                results=result,
                cache_time=0,
                switch_pm_text=trCHUNK["min"],
                switch_pm_parameter="okay",
            )

        elif "|" in query:
            result = await search(inline_query)
            return await inline_query.answer(
                results=result, cache_time=0, switch_pm_text=""
            )

        else:
            if query:
                result = await Libgen(result_limit=50).search(
                    query=query,
                    return_fields=[
                        "title",
                        "pages",
                        "language",
                        "publisher",
                        "year",
                        "author",
                        "extension",
                        "coverurl",
                        "volumeinfo",
                        "mirrors",
                        "md5",
                    ],
                )
                if result is not None:
                    DATA[inline_query.from_user.id] = {}
                    for id, item in enumerate(result, start=1):
                        results.append(
                            InlineQueryResultPhoto(
                                photo_url="https://imgur.com/BpM9gA4"
                                if result[item]["coverurl"] is None
                                else result[item]["coverurl"],
                                title=result[item]["title"],
                                id=f"{id}",
                                description=trCHUNK["description"].format(
                                    result[item]["author"],
                                    result[item]["volumeinfo"],
                                    result[item]["year"],
                                    result[item]["pages"],
                                    result[item]["language"],
                                    result[item]["extension"],
                                    result[item]["publisher"],
                                ),
                                caption=trCHUNK["caption"].format(
                                    result[item]["md5"],
                                    result[item]["title"],
                                    result[item]["author"],
                                    result[item]["volumeinfo"],
                                    result[item]["year"],
                                    result[item]["pages"],
                                    result[item]["language"],
                                    result[item]["publisher"],
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [
                                        [
                                            InlineKeyboardButton(
                                                text=trCHUNK["select"],
                                                url=f"https://t.me/{myID[0].username}?start=-m{result[item]['md5']}",
                                            )
                                        ]
                                    ]
                                ),
                            )
                        )
                        DATA[inline_query.from_user.id][id] = {
                            "thumb": "https://imgur.com/BpM9gA4"
                            if result[item]["coverurl"] is None
                            else result[item]["coverurl"],
                            "caption": f"MD5: {result[item]['md5']}\n"
                            f"Title: **{result[item]['title']}.**\n"
                            f"Author: **{result[item]['author']}.**",
                        }
        if results:
            return await inline_query.answer(
                results=results,
                cache_time=60,
                is_personal=False,
                switch_pm_text=trCHUNK["query"].format(len(results)),
                switch_pm_parameter="okey",
            )
        else:
            result = await default_ans(inline_query)
            return await inline_query.answer(
                results=result,
                cache_time=0,
                switch_pm_text=trCHUNK["nothing"].format(query),
                switch_pm_parameter="okay",
            )

    except errors.QueryIdInvalid:
        pass
    except Exception as Error:
        logger.exception("🐞 %s: %s" % (file_name, Error), exc_info=True)

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
