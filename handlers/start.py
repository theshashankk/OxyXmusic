# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""➼ Helloowww 👋 {message.from_user.first_name}! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n➼ Do you want me to play music in your Telegram groups'voice chats? ➼ Use the buttons below to know more about me ❤️🔥 """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Commands 📜", url="https://telegra.ph/%F0%9D%95%90%F0%9D%96%94%F0%9D%96%9A%F0%9D%96%97---%F0%9D%95%AF%F0%9D%96%86%F0%9D%96%89%F0%9D%96%89%F0%9D%95%AA-%EA%97%84-04-23-5")
                  ],[
                    InlineKeyboardButton(
                        "🚑 Support group 🚑", url="https://t.me/IDK_LOL3"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Add Me To Ur Group", url="https://t.me/{BOT_USERNAME}?groupstart=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**➼ Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support group", url="https://t.me/IDK_LOL3")
                ]
            ]
        )
   )

