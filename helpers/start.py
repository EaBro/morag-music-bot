from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello {message.from_user.first_name}!
This Is Me Morag Music Bot. 
 I Can Play Music In Your Telegram Group's Voice Chat
 Use These Buttons Below To Know More. """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Source code", url="https://github.com/r0ld3x/morag-music-bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/moragchats"
                    ),
                    InlineKeyboardButton(
                        "Devloper 👨", url="https://t.me/r0ld3x"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "Hey I Am Here And I'm Working Perfectly!!!\nUse Me In Inline To Search For A YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶 Search 🎶", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
