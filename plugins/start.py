"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

from os import environ
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
from helper.txt import mr
from helper.database import insert 
from helper.utils import not_subscribed 

FLOOD = int(environ.get("FLOOD", "10"))
START_PIC = environ.get("START_PIC", "https://graph.org/file/51dbdf46bdfe49baa25da.jpg")

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="π’πΉπππ πΌπ’ ππππππ π²πππππππ’", url=client.invitelink) ]]
    text = "ποΈππΎπππ π³ππ³π΄ ππΎππ π½πΎπ πΉπΎπΈπ½π³ πΌπ π²π·π°π½π½π΄π»ποΈ. πΏπ»π΄π°ππ΄ πΉπΎπΈπ½ πΌπ π²π·π°π½π½π΄π» ππΎ πππ΄ ππ·πΈπ π±πΎπ"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
           
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo=START_PIC,
       caption=f"""Hi {message.from_user.mention} \nπΈ'π π° ππππππ π΅πππ ππππππ+π΅πππ ππ πππππ π²πππππππ π±πΎπ ππππ πΏππππππππ πππππππππ & π²πππππ π²ππππππ πππππππ! """,
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("π³π΄ππ", callback_data='dev'),
           InlineKeyboardButton('ππΏπ³π°ππ΄π', url='https://t.me/Inline_db')
           ],[
           InlineKeyboardButton('π°π±πΎππ', callback_data='about'),
           InlineKeyboardButton('π·π΄π»πΏ', callback_data='help')
           ]]
          )
       )
    return


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("πππ°ππ ππ΄π½π°πΌπ΄", callback_data="rename") ],
                   [ InlineKeyboardButton("π²π°π½π²π΄π»", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.x)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("πππ°ππ ππ΄π½π°πΌπ΄", callback_data="rename") ],
                   [ InlineKeyboardButton("π²π°π½π²π΄π»", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""Hi {query.from_user.mention} \nπΈ'π π° ππππππ π΅πππ ππππππ+π΅πππ ππ πππππ π²πππππππ π±πΎπ ππππ πΏππππππππ πππππππππ & π²πππππ π²ππππππ πππππππ! """,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("π³π΄ππ", callback_data='dev'),                
                InlineKeyboardButton('ππΏπ³π°ππ΄π', url='https://t.me/Inline_db')
                ],[
                InlineKeyboardButton('π°π±πΎππ', callback_data='about'),
                InlineKeyboardButton('π·π΄π»πΏ', callback_data='help')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("π²π»πΎππ΄", callback_data = "close"),
               InlineKeyboardButton("π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("π²π»πΎππ΄", callback_data = "close"),
               InlineKeyboardButton("π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("π²π»πΎππ΄", callback_data = "close"),
               InlineKeyboardButton("π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





