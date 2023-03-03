# copyright ©️ 2021 nabilanavab
file_name = "lang/eng.py"


from configs.config   import settings

# REPLY MESSAGE FOR BROKEN WORKS
RESTART = {
    "msg" : """☠ `𝐎𝐕𝐄𝐑𝐋𝐎𝐀𝐃 𝐃𝐄𝐂𝐓𝐄𝐂𝐓𝐄𝐃`☠:\n__تحديث الخادم__ \n
لاحظت أن عملك كان أيضا في قائمة الانتظار
هل يمكنك المحاولة مرة أخرى من فضلك..!""",
    "btn" : { "🚶 أغلق 🚶" : "close|mee" }
}

# PM WELCOME MESSAGE (HOME A, B, C, D...)
HOME = {
    "HomeA" : "مرحبا بك {}..!!\n"
"في بوت {}.!\n\n"

"يمكن لهذا البوت تحويل الصور الPDF وكذلك تعديل علىPDF من قص ودمج وضغط وتشفير ودمج سلادين وغيرها…\n\n"  
"لمعرفة المزيد من خصائص البوت إضغط **⚠️ المساعدة ⚠️**",
    "HomeACB": {
        "⚙️ الإعدادات ⚙️": "Home|B" , "⚠️ مساعدة ⚠️": "Home|C",
        "📢 القناة 📢": f"{str(settings.OWNED_CHANNEL)}",
        " 🌟تقييم 🌟": f"{str(settings.SOURCE_CODE)}",
        "🚶 اغلق 🚶": "close|mee"
    } ,
    "HomeAdminCB": {
        "⚙️ الإعدادات ⚙️": "Home|B" , "⚠️ مساعدة ⚠️": "Home|C",
        "📢 القناة 📢": f"{str(settings.OWNED_CHANNEL)}",
        "🌟تقييم 🌟": f"{str(settings.SOURCE_CODE)}",
        "🗽 الحالة 🗽": "status|home", "🚶 قريب 🚶": "close|mee"
    } ,
    "HomeB" : """صفحة الإعدادات⚙️

اسم المستخدم   : {}
معرف المستخدم           : {}
اسم مستخدم    : {}
تاريخ الانضمام      : {}

لغة    : {}
API                    : {}
واجهة            : {}
تعليق         : {}
اسم الملف      : {}""",
    "HomeBCB" : {
        "📍 واجهك 📍" : "set|thumb",
        "📈 الاسم 📈" : "set|fname",
        "💩 API 💩" : "set|api",
        "📅 تعليق 📅" : "set|capt",
        "« العودة الرئيسية «" : "Home|B2A"
    },
    "HomeC": """🪂 ** رسالة مساعدة **:

``` بعض الميزات الرئيسية هي:
 ◍ تحويل الصور إلى PDF \n ◍ Manupultions PDF \n ◍ العديد من برامج الترميز الشائعة إلى pdf
 
تعديل ملف pdf:
 ◍ PDF⥃ الصور [الكل , النطاق , الصفحات] \n ◍ المستندات إلى PDF [png , jpg , jpeg] \n ◍ الصور PDF \n ◍ بيانات PDF الوصفية \n ◍ PDF⥃TEXT \n ◍ TEXT⥃PDF \n ◍ ضغط ملف pdf
 ◍ انقسام PDF [النطاق , الصفحات] \n ◍ دمج PDF \n ◍ إضافة طابع \n ◍ إعادة تسمية PDF \n ◍ تدوير PDF \n ◍ ENCRYPT / DECRYPT PDF \n ◍ PDF FORMATTER \n ◍ PDF⥃JSON / TXT FILE
 ◍ PDF⥃HTML [عرض الويب] \n ◍ URL⥃PDF \n ◍ PDF⥃ZIP / TAR / RAR [الكل , النطاق , الصفحات] \n وأكثر من ذلك بكثير .. """ ,
    "HomeCCB": {"« BACK HOME «": "Home|A", "🛈 INSTRUCTIONS 🛈": "Home|D"},
    "HomeD": """` نظرًا لأن هذه خدمة مجانية , لا يمكنني ضمان المدة التي يمكنني خلالها الحفاظ على هذه الخدمة ..`😝
 
⚠️ تعليمات ⚠️:
🛈 __يرجى عدم محاولة إساءة استخدام إدارة Bot__ 😒
🛈 __لا ترسل بريدًا عشوائيًا هنا , فقد يؤدي ذلك إلى حظر دائم 🎲__.
🛈 __محتويات الاباحيه ايضا ستمنحك حظر دائم 💯__

** أرسل أي صورة لتبدأ: ** 😁 """,
    "HomeDCB": {"⚠️ مساعدة ⚠️": "Home|C", "» عودة للرئيسية »": "Home|A"}
}

# GROUP WELCOME MESSAGE
HomeG = {
    "HomeA" : HOME['HomeA'],
    "HomeACB" : {
        "🌍 اللغة 🌍" : "set|lang",
        "🛡️ المساعدة 🛡️": "Home|C",
        "📢 القناة 📢" : f"{str(settings.OWNED_CHANNEL)}",
        "🌟 التقييم 🌟": f"{settings.SOURCE_CODE}",
        "🚶 اغلق 🚶" : "close|mee",
    }
}

SETTINGS = {
    "lang" : "الآن، اختر أي لغة..",
    "default" : ["الافتراضي ❌", "CUSTOM ✅"],
    "cant" : "لا يمكن استخدام هذه الميزة ❌",
    "wait" : { "في انتظار.. 🥱" : "nabilanavab" },
    "feedbtn" : { "أبلغ عن أي أخطاء تجدها!" : settings.REPORT },
    "chgLang" : {"الإعداد ⚙️ » تغيير لانج 🌐" : "nabilanavab"},
    "askApi" : "\n\nافتح الرابط **أدناه** وأرسل لي الرمز السري:",
    "waitApi" : { "افتح الرابط ✅" : "https://www.convertapi.com/a/signin" },
    "error" : "حدث خطأ ما أثناء استرداد البيانات من قاعدة البيانات",
    "result" : ["لا يمكن تحديث الإعدادات ❌", "تم تحديث الإعدادات بنجاح ✅"],
    "back" : [{ "« الرئيسية «" : "Home|B2S" }, { "« الرئيسية «" : "Home|B2A" }],
    "feedback" : "تحذير من الأخطاء! إذا كانت رسائلي تبدو غريبة، فمن المحتمل أن يكون خطأ ترجمة جوجل."
                 "\n\nأبلغ عن خطأ في {} Lang:\n`• حدد Lang\n• رسالة خطأ\n• رسالة جديدة`",
    "ask" : [
        "الآن، أرسل لي..",
        "الآن، أرسل لي.. 😅\n\nبعيد.! ليس لدي المزيد من الوقت لمراجعة النص.. 😏\n\n/cancel: للإلغاء"
    ],
    "thumb" : [
        {
            "الاعدادات ⚙️ » THUMBNAIL 📷" : "nabilanavab",
            "♻ أضف ♻" : "set|thumb+",
            "« الرئيسية «" : "Home|B"
        },
        {
            "الاعدادات ⚙️ » THUMBNAIL 📷" : "nabilanavab",
            "♻ تغيير ♻" : "set|thumb+",
            "🗑 حذف 🗑" : "set|thumb-",
            "«  الرئيسية«" : "Home|B2S"
        }
    ],
    "fname" : [
        {
            "الاعدادات ⚙️ » FNAME 📷" : "nabilanavab",
            "♻ أضف ♻" : "set|fname+",
            "« الرئيسية «" : "Home|B2S"
        },
        {
            "الاعدادات ⚙️ » FNAME 📷" : "nabilanavab",
            "♻ تغيير ♻" : "set|fname+",
            "🗑 حذف 🗑" : "set|fname-",
            "« الرئيسية «" : "Home|B2S"
        }
    ],
    "api" : [
        {
            "الاعدادات ⚙️ » API 📷" : "nabilanavab",
            "♻ أضف ♻" : "set|api+",
            "« الرئيسية «" : "Home|B2S"
        },
        {
            "الاعدادات ⚙️ » API 📷" : "nabilanavab",
            "♻ تغيير ♻" : "set|api+",
            "🗑 حذف 🗑" : "set|api-",
            "« الرئيسية «" : "Home|B2S"
        }
    ],
    "capt" : [
        {
            "الاعدادات ⚙️ » CAPTION 📷" : "nabilanavab",
            "♻ أضف ♻" : "set|capt+",
            "« الرئيسية «" : "Home|B2S"
        },
        {
            "الاعدادات ⚙️ » CAPTION 📷" : "nabilanavab",
            "♻ تغيير ♻" : "set|capt+",
            "🗑 حذف 🗑" : "set|capt-",
            "« الرئيسية «" : "Home|B2S"
        }
    ]
}

BOT_COMMAND = {"start": "رسالة ترحيب ..", "txt2pdf": "إنشاء ملف PDF نصي"}

STATUS_MSG = {
    "HOME": "الآن , حدد أي خيار أدناه للحصول على الحالة الحالية 💱 ..` ",
    "_HOME" : {
        "📊 ↓ SERVER ↓ 📊": "nabilanavab", "📶 STORAGE 📶": "status|server",
        "🥥 قاعدة البيانات 🥥": "status|db" , "🌝 ↓ الحصول على قائمة ↓ 🌝": "nabilanavab",
        "💎 المشرف 💎": "status|admin", "👤 المستخدمون 👤": "status|users",
        "« رجوع  «": "Home|A"
    } ,
    "DB": """📂 قاعدة البيانات: \n \n ** ◍ مستخدمو قاعدة البيانات: **` {} `📍 \n ** ◍ محادثات قاعدة البيانات: **` {} `📍""" ,
    "SERVER": """** ◍ المساحة الإجمالية: **` {} `
** ◍ المساحة المستخدمة: ** `{} ({}٪)` \n ** ◍ مساحة حرة: ** `{}`
** ◍ استخدام وحدة المعالجة المركزية: ** "{}`٪ \n ** ◍ استخدام ذاكرة الوصول العشوائي: ** `{}`٪
** ◍ العمل الحالي: ** `{}` \n ** ◍ معرف الرسالة: ** `{}""" ,
    "BACK": {"« BACK «": "status|home"}, "ADMIN": "** Total ADMIN: ** __ {} __ \n",
    "USERS": "المستخدمون: \n\n" , "NO_DB": "لم يتم تعيين قاعدة البيانات بعد 💩"
}

feedbackMsg = f"[اكتب تعليقًا 📋]({settings.FEEDBACK})"

BAN = {
    "UCantUse" : """مرحبا {}

لسبب ما لا يمكنك استخدام هذا الروبوت:(""",
    "UCantUseDB" : """مرحبا {}

لسبب ما لا يمكنك استخدام هذا الروبوت :(

سبب: {}""",
    "GroupCantUse" : """{} لا تتوقع أبدا استجابة جيدة مني
منعني المشرفون من العمل هنا.. 🤭""",
    "GroupCantUseDB" : """{} لا تتوقع أبدا استجابة جيدة مني
منعني المشرفون من العمل هنا.. 🤭

سبب: {}""",
    "cbNotU" : "عفوا، آسف لكسر قلبك، هذه الرسالة ليست لك 💔.\n\nحظا أفضل في المرة القادمة! 😏",
    "Fool" : "من فضلك لا تحاول خداعي.. 🤭",
    "banCB" : {
        "قناة البوت": f"{settings.SOURCE_CODE}",
        "تابع تحديثات": f"{settings.SOURCE_CODE}",
        "انضم": "https://telegram.dog/i2pdfbotchannel"
    },
    "Force" : """Wait [{}](tg://user?id={})..!!

Due To The Huge Traffic Only **Channel Members** Can Use this Bot 🚶

This Means That You Need To **Join** The Below Mentioned Channel for Using Me!

Hit on `"♻️retry♻️"` after joining.. 😅""",
    "ForceCB" : {
        "🌟 JOIN CHANNEL 🌟" : "{0}",
        "♻️ Refresh ♻️" : "refresh{1}"
    },
}

checkPdf = {
    "pg" : "`Number of Pages: •{}•` 🌟",
    "pdf" : """`What should I do with this file.?`

File Name : `{}`
File Size : `{}`""",
    "pdfCB1" : {
        "⭐ META£ATA ⭐" : "metaData",
        "🗳️ PREVIEW 🗳️" : "preview",
        "🖼️ IMAGES 🖼️" : "pdf|img",
        "✏️ TEXT ✏️" : "pdf|txt",
        "🔐 ENCRYPT 🔐" : "work|encrypt",
        "🔒 DECRYPT 🔓" : "work|decrypt",
        "🗜️ COMPRESS 🗜️" : "work|compress",
        "🤸 ROTATE 🤸" : "pdf|rotate",
        "✂️ SPLIT ✂️" : "pdf|split",
        "🧬 MERGE 🧬" : "merge",
        "™️ STAMP ™️" : "pdf|stp",
        "✏️ RENAME ✏️" : "work|rename",
        "🔗 URL 🔗" : "link",
        "» 🏴‍☠️ MORE 🏴‍☠️ »" : "pdf2",
        "🚫 CLOSE 🚫" : "close|all"
    },
    "pdfCB2" : {
        " ↓ SECOND PAGE  ↓ " : "nabilanavab",
        "📝 OCR 📝" : "work|ocr",
        "🥷 A4 FORMAT 🥷" : "work|format", 
        "🖤 BLACK/WHITE 🤍" : "baw",
        "🍴 SATUTATION 🍴" : "sat",
        "📎 COMBINE PDF 📎" : "comb",
        "🔎 ZOOM PDF 🔎" : "zoom",
        "➖ DELETE PAGES ➖": "close|dev",
        "➕ ADD PAGES ➕" : "close|dev",
        "🎨 DRAW PDF 🎨" : "draw",
        "😈 CODEC 😈" : "close|dev",
        "💦 WATERMARK 💦" : "close|dev",
        "« 🏴‍☠️ BACK 🏴‍☠️ «" : "pdf1",
        "🚫 CLOSE 🚫" : "close|all"
    },
    "error" : """__I can't do anything with this file.__ 😏

🐉  `CODEC ERROR`  🐉""",
    "errorCB" : {
        "❌ ERROR IN CODEC ❌" : "error",
        "🔸 CLOSE 🔸" : "close|all"
    },
    "encrypt" : """`FILE IS ENCRYPTED` 🔐

File Name: `{}`
File Size: `{}`""",
    "encryptCB" : {"🔓 DECRYPT 🔓" : "work|decrypt"}
}

PROGRESS = {
    "progress" : """\n**Done ✅ : **{0}/{1}
**Speed 🚀:** {2}/s
**Estimated Time ⏳:** {3}""",
    "workInP" : "WORK IN PROGRESS.. 🙇",
    "upFile" : "`Started Uploading..`📤",
    "refresh" : { "♻️ Refresh ♻️" : "{}" },
    "dlFile" : "`Downloading your file..` 📥",
    "dlImage" : "`Downloading your Image..⏳`",
    "upFileCB" : {"📤 .. UPLOADING.. 📤" : "nabilanavab"},
    "takeTime" : """```⚙️ Work in Progress..`
`It might take some time..```💛""",
    "cbPRO_D" : ["📤 DOWNLOAD: {:.2f}% 📤", "🎯 CANCEL 🎯"],
    "cbPRO_U" : ["📤 UPLOADED: {:.2f}% 📤", "🎯 CANCEL 🎯"]
}

GENERATE = {
    "noQueue" : "`No Queue found..`😲",
    "noImages" : "No image found.!! 😒",
    "currDL" : "Downloaded {} Images 🥱",
    "geting" : "File Name: `{}`\nPages: `{}`",
    "getFileNm" : "Now Send Me a File Name 😒: ",
    "deleteQueue" : "`Queue deleted Successfully..`🤧",
    "getingCB" : {"📚 GENERATING PDF.." : "nabilanavab"},
}

document = {
    "reply" : checkPdf['pdf'],
    "upFile" : PROGRESS['upFile'],
    "process" : "⚙️ Processing..",
    "replyCB" : checkPdf['pdfCB1'],
    "inWork" : PROGRESS['workInP'],
    "download" : PROGRESS['dlFile'],
    "refresh" : PROGRESS['refresh'],
    "dlImage" : PROGRESS['dlImage'],
    "takeTime" : PROGRESS['takeTime'],
    "fromFile" : "`Converted: {} to {}`",
    "unsupport" : "Unsupported file..🙄`",
    "cancelCB" : { "⟨ Cancel ⟩" : "close|me" },
    "generate" : { "GENERATE 📚" : "generate" },
    "generateRN" : {
        "GENERATE 📚" : "generate",
        "RENAME ✍️" : "generateREN"
    },
    "noAPI" : """`Please add convert API.. 💩

start » settings » api » add/change`""",
    "error" : """SOMETHING went WRONG.. 🐉

ERROR: `{}`""",
    "setHdImg" : """Now Image To PDF is in HD mode 😈""",
    "setDefault" : { "« Back to Default Quality «" : "close|hd" },
    "useDOCKER" : "`File Not Supported, deploy bot using docker`",
    "big" : """Due to Overload, Owner limits {}mb for pdf files 🙇

`please Send me a file less than {}mb Size` 🙃""",
    "bigCB" : {
        "💎 Create 2Gb Support Bot 💎" : "https://github.com/nabilanavab/ilovepdf"
    },
    "imageAdded" : """`Added {} pages to your PDF..`🤓

fileName: `{}.pdf`"""
}

gDocument = {
    "admin" : """Due to Some Telegram Limits..

I can only work as an admin
__Please promote me as admin__ ☺️""",
    "notDOC" : "Broh Please Reply to a Document or an Image..🤧",
    "Gadmin" : """Only Group Admins Can Use This Bot
Else Come to my Pm 😋""",
    "adminO" : """`Only admins can do it..`

Or try on your pdfs(__reply to your message__)"""
}
gDocument.update(document)

noHelp = f"`No one gonna help you` 😏"

split = {
    "work" : ["Range", "Single"],
    "inWork" : PROGRESS['workInP'],
    "download" : PROGRESS['dlFile'],
    "cancelCB" : document['cancelCB'],
    "exit" : "`Process Cancelled..` 😏",
    "button" : {
        "⚙️ PDF » SPLIT ↓" : "nabilanavab",
        "With In Range 🦞" : "split|R",
        "Single Page 🐛" : "split|S",
        "« BACK «" : "pdf1"
    },
    "over" : "`5 attempts over.. Process cancelled..`😏",
    "pyromodASK_1" : """__PDF Split » By Range
Now, Enter the range (start:end) :__

/exit __to cancel__""",
    "completed" : "`Downloading Completed..` ✅",
    "error_1" : "`Syntax Error: justNeedStartAndEnd `🚶",
    "error_2" : "`Syntax Error: errorInEndingPageNumber `🚶",
    "error_3" : "`Syntax Error: errorInStartingPageNumber `🚶",
    "error_4" : "`Syntax Error: pageNumberMustBeADigit` 🧠",
    "error_5" : "`Syntax Error: noEndingPageNumber Or notADigit` 🚶",
    "error_6" : "`Can't find any number..`😏",
    "error_7" : "`Something went Wrong..`😅",
    "error_8" : "`Enter Numbers less than {}..`😏",
    "error_9" : "`1st Check Number of pages` 😏",
    "upload" : "⚙️ `Started Uploading..` 📤"
}

pdf2IMG = {
    "uploadfile" : split["upload"],
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "toImage" : {
        "⚙️ PDF » IMAGES ↓" : "nabilanavab",
        "🖼 IMG 🖼" : "pdf|img|img",
        "📂 DOC 📂" : "pdf|img|doc",
        "🤐 ZIP 🤐" : "pdf|img|zip",
        "🎯 TAR 🎯" : "pdf|img|tar",
        "« BACK «" : "pdf1" 
    },
    "imgRange" : {
        "⚙️ PDF » IMAGES » {} ↓" : "nabilanavab",
        "🙄 ALL 🙄" : "p2img|{}A",
        "🤧 RANGE 🤧" : "p2img|{}R",
        "🌝 PAGES 🌝" : "p2img|{}S",
        "« BACK «" : "pdf|img"
    },
    "over" : "`5 attempt over.. Process canceled..`😏",
    "pyromodASK_1" : """__Pdf - Img›Doc » Pages:
Now, Enter the range (start:end) :__

/exit __to cancel__""",
    "pyromodASK_2" : """"__Pdf - Img›Doc » Pages:
Now, Enter the Page Numbers seperated by__ (,) :

/exit __to cancel__""",
    "exit" : "`Process Canceled..` 😏",
    "error_1" : "`Syntax Error: justNeedStartAndEnd `🚶",
    "error_2" : "`Syntax Error: errorInEndingPageNumber `🚶",
    "error_3" : "`Syntax Error: errorInStartingPageNumber `🚶",
    "error_4" : "`Syntax Error: pageNumberMustBeADigit` 🧠",
    "error_5" : "`Syntax Error: noEndingPageNumber Or notADigit` 🚶",
    "error_6" : "`Can't find any number..`😏",
    "error_7" : "`Something went Wrong..`😅",
    "error_8" : "`PDF only have {} pages` 💩",
    "error_9" : "`1st Check Number of pages` 😏",
    "error_10" : "__Due to Some restrictions Bot Sends Only 50 pages as ZIP..__😅",
    "total" : "`Total pages: {}..⏳`",
    "upload" : "`Uploading: {}/{} pages.. 🐬`",
    "current" : "`Converted: {}/{} pages.. 🤞`",
    "complete" : "`Uploading Completed.. `🏌️",
    "canceledAT" : "`Canceled at {}/{} pages..` 🙄",
    "cbAns" : "⚙️ okDA, Canceling.. ",
    "cancelCB" : {"💤 CANCEL 💤" : "close|P2I"},     # EDITABLE: ❌
    "canceledCB" : {"🍄 CANCELLED 🍄" : "close|P2IDONE"},
    "completed" : {"😎 COMPLETED 😎" : "close|P2ICOMP"}
}

merge = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "upload" : PROGRESS['upFile'],
    "load" : "__Due to Overload you can only merge 5 PDFs at a time__",
    "sizeLoad" : "`Due to Overload Bot Only Support %sMb PDFs..", # removing %s show error
    "pyromodASK" : """__MERGE pdfs » Total PDFs in queue: {}__

/exit __to cancel__
/merge __to merge__""",
    "exit" : "`Process Cancelled..` 😏",
    "total" : "`Total PDFs : {} 💡",
    "current" : "__Started Downloading PDF : {} 📥__",
    "cancel" : "`Merging Process Cancelled.. 😏`",
    "started" : "__Merging Started.. __ 🪄",
    "caption" : "`Merged PDF 🙂`",
    "error" : """`May be File Encrypted..`

Reason: {}"""
}

metaData = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],   # [❌]
    "read" : "Please read this message again.. 🥴"
}

preview = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "error" : document['error'],
    "download" : PROGRESS['dlFile'],
    "_" : "PDF only have {} pages 🤓\n\n",
    "__" : "PDF pages: {}\n\n",
    "total" : "`Total pages: {}..` 🤌",
    "album" : "`Preparing an Album..` 🤹",
    "upload" : f"`Uploading: preview pages.. 🐬`"
}

stamp = {
    "stamp" : {
        "⚙️ PDF » STAMP ↓" : "nabilanavab",
        "Not For Public Release 🤧" : "pdf|stp|10",
        "For Public Release 🥱" : "pdf|stp|8",
        "Confidential 🤫" : "pdf|stp|2",
        "Departmental 🤝" : "pdf|stp|3",
        "Experimental 🔬" : "pdf|stp|4",
        "Expired 🐀" : "pdf|stp|5",
        "Final 🔧" : "pdf|stp|6",
        "For Comment 🗯️" : "pdf|stp|7",
        "Not Approved 😒" : "pdf|stp|9",
        "Approved 🥳" : "pdf|stp|0",
        "Sold ✊" : "pdf|stp|11",
        "Top Secret 😷" : "pdf|stp|12",
        "Draft 👀" : "pdf|stp|13",
        "AsIs 🤏" : "pdf|stp|1",
        "« BACK «" : "pdf1"
    },
    "stampA" : {
        "⚙️ PDF » STAMP » COLOR ↓" : "nabilanavab",
        "Red ❤️" : "spP|{}|r",
        "Blue 💙" : "spP|{}|b",
        "Green 💚" : "spP|{}|g",
        "Yellow 💛" : "spP|{}|c1",
        "Pink 💜" : "spP|{}|c2",
        "Hue 💚" : "spP|{}|c3",
        "White 🤍" : "spP|{}|c4",
        "Black 🖤" : "spP|{}|c5",
        "« Back «" : "pdf|stp"
    },
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "upload" : PROGRESS['upFile'],
    "stamping" : "`Started Stamping..` 💠",
    "caption" : """stamped pdf\ncolor : `{}`
annot : `{}`"""
}

work = {
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "takeTime" : PROGRESS['takeTime'],
    "upload" : PROGRESS['upFile'],
    "button" : document['cancelCB'],
    "rot360" : "You have some **big problem..🙂**",
    "ocrError" : "Owner Restricted 😎🤏",
    "largeNo" : "Send a PDF file less than 5 pages.. 🙄",
    "pyromodASK_1" : """__PDF {} »
Now, please enter the PASSWORD :__

/exit __to cancel__""",
    "pyromodASK_2" : """__Rename PDF »
Now, please enter the NEW NAME:__

/exit __to cancel__""",
    "exit" : "`process canceled.. `😏",
    "ren_caption" : "__New Name:__ `{}`", 
    "notENCRYPTED" : "`File is Not Encrypted..` 👀",
    "compress" : """⚙️ ```Started Compressing.. 🌡️
It might take some time..```💛""",
    "decrypt" : """⚙️ ```Started Decrypting.. 🔓
It might take some time..```💛""",
    "encrypt" : """⚙️ ```Started Encrypting.. 🔐
It might take some time..```💛""",
    "ocr" : """⚙️ ```Adding OCR Layer.. ✍️
It might take some time..```💛""",
    "format" : """⚙️ ```Started Formatting.. 🤘
It might take some time..```💛""",
    "rename" : """⚙️ ```Renameing PDf.. ✏️
It might take some time..```💛""",
    "rot" : """⚙️ ```Rotating PDf.. 🤸
It might take some time..```💛""",
    "pdfTxt" : """⚙️ ```Extracting Text.. 🐾
It might take some time..```💛""",
    "fileNm" : """Old Filename: {}
New Filename: {}""",
    "rotate" : {
        "⚙️ PDF » ROTATE ↓" : "nabilanavab",
        "90°" : "work|rot90",
        "180°" : "work|rot180",
        "270°" : "work|rot270",
        "360°" : "work|rot360",
        "« BACK «" : "pdf1"
    },
    "txt" : {
        "⚙️ PDF » TXT ↓" : "nabilanavab",
        "📜 MESSAGE 📜" : "work|M",
        "🧾 TXT FILE 🧾" : "work|T",
        "🌐 HTML 🌐" : "work|H",
        "🎀 JSON 🎀" : "work|J",
        "« BACK «" : "pdf1"
    }
}

PROCESS = {
    "ocr" : "OCR added",
    "decryptError" : "__Cannot Decrypt the file with__ `{}` 🕸️",
    "decrypted" : "__Decrypted File__",
    "encrypted" : "__Page Number__: {}\n__key__ 🔐: ||{}||",
    "compressed" : """`Original Size : {}
Compressed Size : {}

Ratio : {:.2f} %`""",
    "cantCompress" : "File Can't be Compressed More..🤐",
    "pgNoError" : """__For Some Reason A4 FORMATTING Supports only for PDFs with less than 5 Pages__

Total Pages: {} ⭐""",
    "ocrError" : "`Already Have A Text Layer.. `😏",
    "90" : "__Rotated 90°__",
    "180" : "__Rotated 180°__",
    "270" : "__Rotated 270°__",
    "formatted" : "A4 Formatted File",
    "M" : "♻ Extracted {} Pages ♻",
    "H" : "HTML File",
    "T" : "TXT File",
    "J" : "JSON File"
}

pdf2TXT = {
    "upload" : PROGRESS["upFile"],
    "exit" : split['exit'],
    "nothing" : "Nothing to create.. 😏",
    "TEXT" : "`Create PDF From Text Messages »`",
    "start" : "Started Converting txt to Pdf..🎉",
    "font_btn" : {
        "TXT@PDF » SET FONT" : "nabilanavab",
        "Times" : "pdf|font|t",
        "Courier" : "pdf|font|c",
        "Helvetica (Default)" : "pdf|font|h",
        "Symbol" : "pdf|font|s",
        "Zapfdingbats" : "pdf|font|z",
        "🚫 CLOSE 🚫" : "close|me"
    },
    "size_btn" : {
        "TXT@PDF » {} » SET SCALE" : "nabilanavab",
        "Portarate" : "t2p|{}|p",
        "Landscape" : "t2p|{}|l",
        "« Back «": "pdf|T2P"
    },
    "askT" : """__TEXT TO PDF » Now, please enter a TITLE:__

/exit __to cancel__\n/skip __to skip__""",
    "askC" : """__TEXT TO PDF » Now, please enter paragraph {}:__

/exit __to cancel__\n/create __to create__"""
}

URL = {
    "notPDF" : "`Not a PDF File",
    "close" : { "close" : "close|all" },
    "get" : {"🧭 Get PDF File 🧭" : "getFile"},
    "error" : """🐉 SOMETHING WENT WRONG 🐉,

ERROR: `{}`

NB: In Groups, Bots Can Only fetch documents Send After Joining Group =)""",
    "done" : "```Almost Done.. ✅\nNow, Started Uploading.. 📤```",
    "_error_" : "send me any url or direct telegram pdf links",
    "openCB" : {"Open In Browser" : "{}"},
    "_error" : "`Some Thing Went Wrong =(`\n\n`{}`",
    "_get" : """[Open Chat]({})

**ABOUT CHAT ↓**
Chat Type   : {}
Chat Name : {}
Chat Usr    : @{}
Chat ID        : {}
Date : {}

**ABOUT MEDIA ↓**
Media       : {}
File Name : {}
File Size   : {}
File Type : {}"""
}

getFILE = {
    "wait" : "Wait.. Let me.. 😜",
    "inWork" : PROGRESS['workInP'],
    "big" : "Send PDF url less than {}mb",
    "dl" : {"📥 ..DOWNLOADING.. 📥" : "nabilanavab"},
    "up" : {"📤 ..UPLOADING..  📤" : "nabilanavab"},
    "complete" : {"😎 COMPLETED 😎" : f"{str(settings.SOURCE_CODE)}"}
}

cbAns = [
    "This feature is Under Development ⛷️",
    "Error annenn paranjille.. then what.. 😏",
    "Process Canceled.. 😏",
    "File Not Encrypted.. 👀",
    "Nothing Official About it.. 😅",
    "🎉 Completed.. 🏃"
]

wa = {
    "exit" : split["exit"],
    "over" : pdf2IMG['over'],
    "upFile" : PROGRESS['upFile'],
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "error" : "Something went Wrong 🙂",
    "cancelCB" : {"⟨ Cancel ⟩" : "close|me"},
    "add" : "Adding watermark to PDF File 💩",
    "waDL" : "__Getting watermark File..__ 🙄",
    "type" : {
        "⚙️ PDF » WATERMARK ↓" : "nabilanavab",
        "TEXT" : "pdf|wa|txt",
        "IMAGE" : "pdf|wa|img",
        "PDF" : "pdf|wa|pdf",
        "« BACK «" : "pdf2"
    },
    "op" : {
        "⚙️ PDF » WATERMARK » {} » OPCACiTY ↓" : "nabilanavab",
        "10 %":"pdf|wa|{}|o01",
        "20 %":"pdf|wa|{}|o02",
        "30 %":"pdf|wa|{}|o03",
        "40 %":"pdf|wa|{}|o04",
        "50 %":"pdf|wa|{}|o05",
        "60 %":"pdf|wa|{}|o06",
        "70 %":"pdf|wa|{}|o07",
        "80 %":"pdf|wa|{}|o08",
        "90 %":"pdf|wa|{}|o09",
        "100 %":"pdf|wa|{}|o10",
        "« BACK «" : "pdf|wa"
    },
    "po" : {
        "⚙️ PDF » WATERMARK » POSiTiON ↓" : "nabilanavab",
        "᠎᠎᠎ " : "wa|{0}|{1}|TL",
        "᠎᠎   " : "wa|{0}|{1}|TM",
        "᠎᠎ " : "wa|{0}|{1}|TR",
        "᠎᠎  " : "wa|{0}|{1}|ML",
        "᠎᠎　" : "wa|{0}|{1}|MM",
        "᠎᠎⠀ ⠀" : "wa|{0}|{1}|MR",
        "᠎᠎ " : "wa|{0}|{1}|BL",
        "᠎ ᠎ " : "wa|{0}|{1}|BM",
        "᠎  ᠎ " : "wa|{0}|{1}|BR",
        "« BACK «" : "pdf|wa|{0}"
    }, 
    "txt" : """__Now, Send me any Text Message__

/exit : to cancel""", 
    "pdf" : """__Send me the watermark pdf.__

/exit : to cancel""",
    "img" : """__Send me the watermark Image as file.__
__ Supported Files [png, jpeg, jpg]__

/exit : to cancel""",
}

comb = {
    "upFile" : PROGRESS['upFile'],
    "inWork" : PROGRESS['workInP'],
    "process" : document['process'],
    "process" : document['process'],
    "download" : PROGRESS['dlFile'],
    "cancelCB" : {"⟨ Cancel ⟩" : "close|me"},
}

inline_query = {
    "capt" : "SET LANGUAGE ⚙️",
    "des" : "By: @nabilanavab ❤",
    "TOP" : { "Now, Select Language ⮷" : "nabilanavab" },
}

LINK = {
    "gen" : "`🔗 Generating..`",
    "_gen" : """```🔗 Generating..
We're working on it!

Please allow a moment for the processing to complete.```""",
    "no" : "Unfortunately, we encountered an error 😓",
    "type" : """`🔗 Generating..`

**Public** 📢:
__The file accessed via this link will be publicly available, allowing anyone to save and forward it__.


**Protect** 🔐:
__Ensures the confidentiality of the message by preventing its forwarding and saving__.""",
    "notify" : "Get Notify when a someone fetch this pdf",
    "notify_pvt" : {
        "🔔 NOTIFY 🔔" : "link-pvt-ntf",
        "🔕 MUTE 🔕" : "link-pvt-mut"
    },
    "notify_pub" : {
        "🔔 NOTIFY 🔔" : "link-pbc-ntf",
        "🔕 MUTE 🔕" : "link-pbc-mut"
    },
    "typeBTN" : {
        "📢 PUBLIC 📢" : "link-pub",
        "🔐 PRIVATE 🔐" : "link-pvt"
    },
    "link" : "**Here it is! This is what you were searching for..**",
    "error" : "Oops, it looks like something went wrong. Please try again later.\n\n`ERROR:` {}"
}

DELETE = {
    "button" : {
        "⚙️ PDF » SPLIT ↓" : "nabilanavab",
        "With In Range 🦞" : "split|dR",
        "Single Page 🐛" : "split|dS",
        "« BACK «" : "pdf1"
    },
}
