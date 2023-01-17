import os

from pydrive.auth import GoogleAuth
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot import Creds_path, LOGGER
from bot.drivefunc.Tokenverify import token_make


@Client.on_message(filters.command(["login"]), group=-2)
async def Auth(client, message):
    LOGGER.info(f"{message.from_user.username} : is Trying to verify")
    token_make(client, message)
    gauth = GoogleAuth()
    ID = str(message.from_user.id)
    try:
        gauth.LoadCredentialsFile(os.path.join(Creds_path, ID))
    except Exception as e:
        LOGGER.error(e)

    if gauth.credentials is None:
        authurl = gauth.GetAuthUrl()
        # print(authurl)
        AUTH = f"{authurl}"
        await message.reply_text("ادخل على هذا الرابط و سجل بحساب جوجل الذي تريد الرفع عليه \n\n سوف يحولك إلى صفحة مكتوب عليها كود معين \n\n غالباً يكون بعد  \n\n code= \n\n و قبل \n\n & \n\n كما في هذه الصورة هنا \n\n https://drive.google.com/file/d/1p2sok2PVtkalji7252goTla2Hj_Oe9El/view?usp=sharing  \n\n انسخه ثم أرسله هنا ",
                                 reply_markup=InlineKeyboardMarkup(
                                     [[InlineKeyboardButton("ربط الحساب", url=AUTH)]
                                      ]))

    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()

        await message.reply_text("أنت الفعل مسجل بحساب")
    else:
        # Initialize the saved creds
        gauth.Authorize()
        await message.reply_text("أنت بالفعل مسجل بحساب ")
    raise StopPropagation
