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
        await message.reply_text("أولاً يجب عليك إرسال عنوان بريد جوجل الخاص بك إلى هذا البوت \n\n https://t.me/Dashmelchatbot \n\n ثم شاهد شرح البوت  \n\n https://t.me/ibnAlQyyim/1284 \n\n ",
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
