from pyrogram import Client, filters 
from helper.database import find, addcaption, delcaption 

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("𝙶𝙸𝚅𝙴 𝙼𝙴 𝙰 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 𝚃𝙾 𝚂𝙴𝚃.\n\n𝙴𝚇𝙰𝙼𝙿𝙻𝙴:- /set_caption 📕 𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴: {filename}\n\n💾 𝚂𝙸𝚉𝙴: {filesize}\n\n⏰ 𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽: {duration}")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("𝚈𝙾𝚄𝚁 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙳𝙳𝙴𝙳")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if not caption:
       return await message.reply_text("𝚃𝙷𝙴𝚁𝙴 𝙸𝚂 𝙽𝙾 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 𝙵𝙾𝚄𝙽𝙳")
    delcaption(int(message.chat.id))
    await message.reply_text("𝚈𝙾𝚄𝚁 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙳𝙴𝙻𝙴𝚃𝙴𝙳")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>𝚈𝙾𝚄𝚁 𝙲𝙰𝙿𝚃𝙸𝙾𝙽:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("𝚃𝙷𝙴𝚁𝙴 𝙸𝚂 𝙽𝙾 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 𝙵𝙾𝚄𝙽𝙳")
