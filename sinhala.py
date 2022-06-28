import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

STARTCMD = "🌼Choose language To Start bot!"

COMMAND_LANGBTN = InlineKeyboardMarkup([[
      InlineKeyboardButton('සිංහල 🇱🇰', callback_data="START_SI")
      ],
      [
      InlineKeyboardButton('ENGLISH 🇬🇧', callback_data="START_SI")
      ]])

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#START_SI Callback Text & Btn

SI_HELP = InlineKeyboardMarkup([[
                InlineKeyboardButton('පෙර මෙනුවට පිවිසෙන්න', callback_data="HELP_BACK")
            ]])

SI_STARB = InlineKeyboardMarkup([[
                InlineKeyboardButton('උදව්❔', callback_data="SIHELP_CLB")
            ],
            [
                InlineKeyboardButton('👩‍💻අපගේ ඇප්ප් ඩේටාබේස් එක👩‍💻', url='https://t.me/EpicApkDatabase'),
                InlineKeyboardButton('බොට් ඩිවලොපර්ස්', callback_data="Si_Devs")
            ],
            [
                InlineKeyboardButton('</ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰', url='https://t.me/EpicBotsSl')
            ],
            [
                InlineKeyboardButton('🔍ඇප් සර්ච් කරම්න🔄', switch_inline_query_current_chat=''),
                InlineKeyboardButton('↗️ශෙයාර් කරපම්↗️', switch_inline_query='')
            ]
        ])

SI_STARTM = "Hi සාදරයෙන් පිළිගනිමු **Epic App Store Bot**🎭 ✓වැඩිදුර උදවු සඳහා උදවු ක්ලික් කරන්න⚡"
