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
