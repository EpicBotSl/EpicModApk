import os
import logging
from utils.database import Database
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from info import START_MSG, CHANNELS, ADMINS, INVITE_MSG, DATABASE_URI
from utils import Media, unpack_new_file_id

logger = logging.getLogger(__name__)

@Client.on_message(filters.command("start"))
async def startprivate(client, message):
    #return
    chat_id = message.from_user.id
    if not await database.is_user_exist(chat_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await database.add_user(chat_id)
        if -1001645328504:
            await client.send_message(
                -1001645328504,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\**ID:**{message.from_user.id}\n Started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    file_id = "CAACAgUAAxkBAAEFIihiuYjFehkzzJg6fBsp9NSddE2QSQACsAYAAseOyVXbaQF75owUgCkE"
    await client.send_sticker(message.chat.id, file_id)
    text = f"Hi {message.from_user.mention}, Welcome to **Epic App Store Bot**🎭 ✓Click Help To more Helps⚡"
    reply_markup = Backbuttons  
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
        
@Client.on_message(filters.command("help"))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/6b3bee7715543e8fd6afa.jpg",caption=helps_msg,reply_markup=Help_backbtn)


DATABASE_URI=DATABASE_URI
database = Database(DATABASE_URI, "epic_bot")     
#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#Callbacks

@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="Epic Devs",
        )
    elif update.data == "DevsCallback":
         await update.message.edit_text(
             text=DEVS_MG,
             reply_markup=DEVS_BTN,
             disable_web_page_preview=True
         )
         await update.answer(
             text="</ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰",
         )  
    elif update.data == "back_Clbs":
         await update.message.edit_text(
             text=Back_Msg,
             reply_markup=Backbuttons
         )
         await update.answer(
             text="Menu 🔙"
         )
    elif update.data == "HELP_CLB":
         await update.message.edit_text(
             text=helps_msg,
             reply_markup=Help_backbtn
         )
         await update.answer(
             text="This Is Help Menu🌹"
         )
    elif update.data == "HELP_BACK":
         await update.message.edit_text(
             text=Back_Msg,
             reply_markup=Backbuttons
         )
         await update.answer(
             text="Help🔙"
         )


#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#Buttons & Msgs

DEVS_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Navanjana', url='https://t.me/NA_VA_N_JA_NA1'),
                 InlineKeyboardButton('Wisula', url='https://t.me/wisula4')
                 ],
                 [
                 InlineKeyboardButton('🔙', callback_data="back_Clbs")
                 ]]
                  )

DEVS_MG = "🌱We Are epic Developers 🌟"

helps_msg = """
⸙𝚃𝚑𝚒𝚜 𝙸𝚜 𝙴𝚙𝚒𝚌 𝙰𝚙𝚙 𝚂𝚝𝚘𝚛𝚎 𝙱𝚘𝚝𝚜 𝙷𝚎𝚕𝚙 𝚂𝚎𝚌𝚝𝚒𝚘𝚗!

**𝚆𝚑𝚊𝚝 𝙲𝚊𝚗 𝙳𝚘 𝚃𝚑𝚒𝚜 𝙱𝚘𝚝?**

➡𝚃𝚑𝚒𝚜 𝙱𝚘𝚝 𝚆𝚒𝚕𝚕 𝙱𝚎 𝚁𝚞𝚗𝚗𝚒𝚗𝚐 𝙾𝚗 𝙾𝚠𝚎𝚛 𝚊𝚙𝚔 𝚍𝚊𝚝𝚊𝚋𝚊𝚜𝚎.
➡𝚃𝚑𝚒𝚜 𝙱𝚘𝚝 𝙷𝚊𝚟𝚎 
      ▪𝙼𝚘𝚍 𝙰𝚙𝚔𝚜
      ▪𝙿𝚛𝚎𝚖𝚒𝚞𝚖 𝙰𝚙𝚔𝚜
      ▪𝙻𝚊𝚛𝚐𝚎 𝙰𝚙𝚔𝚜
➡𝚃𝚑𝚒𝚎 𝙱𝚘𝚝 𝚆𝚘𝚛𝚔 𝙾𝙽 𝙸𝚗𝚕𝚒𝚗𝚎 𝙼𝚘𝚘𝚍 𝚂𝚠𝚑𝚒𝚝𝚑 𝙸𝚗𝚕𝚒𝚗𝚎 𝙼𝚘𝚘𝚍 𝙰𝚗 𝚂𝚎𝚊𝚛𝚌𝚑 𝙰𝚙𝚔𝚜

✔𝙼𝚘𝚛𝚎 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 
     ▫ @EpicBotsSl
✔𝚀𝚞𝚎𝚜𝚝𝚒𝚘𝚗𝚜 
     ▫ @EpicChats
✔𝙰𝚙𝚔 𝙳𝚊𝚝𝚊𝚋𝚊𝚜𝚎 
     ▫ @EpicApkDatabase
     
                   `</ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰2022©`
"""

Help_backbtn = InlineKeyboardMarkup([[
                InlineKeyboardButton('🔙', callback_data="HELP_BACK")
            ]])

Backbuttons = InlineKeyboardMarkup([[
                InlineKeyboardButton('🆘HELP🆘', callback_data="HELP_CLB")
            ],
            [
                InlineKeyboardButton('👑Apk Database👑', url='https://t.me/EpicApkDatabase'),
                InlineKeyboardButton('👩‍💻Bot Devs👩‍💻', callback_data="DevsCallback")
            ],
            [
                InlineKeyboardButton('</ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰', url='https://t.me/EpicBotsSl')
            ],
            [
                InlineKeyboardButton('🔍Search here🔄', switch_inline_query_current_chat=''),
                InlineKeyboardButton('↗️Go inline↗️', switch_inline_query='')
            ]
        ])

Back_Msg = "Hi Welcome to **Epic App Store Bot**🎭 ✓Click Help To more Helps⚡"

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#


@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('ttl') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if not (reply and reply.media):
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    msg = await message.reply("Processing...⏳", quote=True)

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    file_id = unpack_new_file_id(media.file_id)[0]
    result = await Media.collection.delete_one({'file_id': file_id})

    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')
