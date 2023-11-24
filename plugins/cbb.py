#(©)Codexbotz
#Recoded By @Its_Tartaglia_Childe

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n┃ Dҽʋҽʅσρҽɾ : <a href='tg://user?id={5090651635}'>Iȶֆ Cɦɨʟɖɛ</a>\n┃ ¢яєαтσя : <a href='tg://user?id={OWNER_ID}'>​ꜱᴀʜɪʟ​</a>\n┃ Lαɳɠυαɠҽ : <code>Python3</code>\n┃ LιႦɾαɾყ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n┃ ѕσυя¢є ¢σ∂є : <a href=https://t.me/Its_Tartaglia_Childe>ᴏᴡɴᴇʀ</a>\n┃ мαιη ¢нαηηєℓ : <a href=https://t.me/Anime_X_Hunters>ᴀɴɪᴍᴇ ʜᴜɴᴛᴇʀꜱ​​</a>\n┃ Sυρρσɾƚ Gɾσυρ : <a href=https://t.me/Hunters_Discussion>ʜᴜɴᴛᴇʀꜱ ᴅɪꜱᴄᴜꜱꜱɪᴏɴ</a>\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💥​ᴄʟᴏꜱᴇ​💥", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
