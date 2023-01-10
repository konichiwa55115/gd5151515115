from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command(["start"]), group=-2)
async def start(_, message):
    join_button = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("القناة ", url="https://t.me/ibnAlQyyim")],
            [InlineKeyboardButton("الإبلاغ عن الأعطال", url="https://t.me/nase7aaa")],
        ]
    )

    welcome_msg = f"السلام عليكم يا  <b>{message.from_user.first_name}</b>\n/أنا بوت أقوم برفع الملفات إلى جوجل درايف \n أرسل /help لمزيد من المعلومات \n\n لبقية البوتات هنا \n\n  https://t.me/ibnAlQyyim/1120 \n\n و لدعم استمرار المشروع هنا \n\n http://paypal.me/kelectronic89 "
    s = await message.reply_text(welcome_msg, reply_markup=join_button)

    raise StopPropagation
