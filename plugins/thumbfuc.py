from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client,message):
    thumb = find(int(message.chat.id))[0]
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("ππ·π΄ππ΄ πΈπ π½πΎ π²ππππΎπΌ ππ·ππΌπ±π½π°πΈπ» π΅πΎππ½π³") 
		
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client,message):
    delthumb(int(message.chat.id))
    await message.reply_text("π²ππππΎπΌ ππ·ππΌπ±π½π°πΈπ» πππ²π²π΄πππ΅ππ»π»π π³π΄π»π΄ππ΄π³")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
    file_id = str(message.photo.file_id)
    addthumb(message.chat.id , file_id)
    await message.reply_text("ππΎππ π²ππππΎπΌ ππ·ππΌπ±π½π°πΈπ» πππ²π²π΄πππ΅ππ»π»π ππ°ππ΄π³")
	
