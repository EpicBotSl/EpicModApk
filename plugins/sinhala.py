from pyrogram.types import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Pyrogram import *

STARTCMD = "🌼Choose language To Start bot!"

COMMAND_LANGBTN = InlineKeyboardMarkup([[
      InlineKeyboardButton('සිංහල 🇱🇰', callback_data="START_SI")
      ],
      [
      InlineKeyboardButton('ENGLISH 🇬🇧', callback_data="START_SI")
      ]])

