from aiogram import types
from loader import dp, bot
from mfyInfos import MFYInfos
from data.config import DEVID
from keyboards.inline.backSecKeys import *

devID = DEVID

@dp.callback_query_handler(lambda query: query.data.startswith('$'))
async def sec1Handle(query: types.CallbackQuery):
    mfyid = query.data.split("$")[1]
    mfydata = MFYInfos[mfyid]

    mfyidforKeys = mfyid.split(".")[0]
    keyboard = None
    
    if mfyid in MFYInfos:
      if mfyidforKeys == str(1):
        keyboard = backSec1
      elif mfyidforKeys == str(2):
          keyboard = backSec2
      elif mfyidforKeys == str(3):
        keyboard = backSec3
      elif mfyidforKeys == str(4):
        keyboard = backSec4
      await query.message.edit_text(f"🔹Маҳалла фуқаролар йиғини раиси: \n⚡️{mfydata['rais']['ism']}\n☎️ {mfydata['rais']['tel']} \n\n🔹Ҳоким ёрдамчиси: \n⚡️ {mfydata['yordamchi']['ism']} \n☎️ {mfydata['yordamchi']['tel']} \n\n🔹Хотин-қизлар фаоли: \n⚡️ {mfydata['ayollar']['ism']} \n☎️ {mfydata['ayollar']['tel']} \n\n🔹Ёшлар етакчиси: \n⚡️ {mfydata['yetakchi']['ism']} \n☎️ {mfydata['yetakchi']['tel']} \n\n🔹Профилактика инспектори: \n⚡️ {mfydata['prof']['ism']} \n☎️ {mfydata['prof']['tel']}", reply_markup=keyboard)

    else:
      await bot.send_message(chat_id=devID, text=f"The bot has an error in dictionary {mfyid}")
