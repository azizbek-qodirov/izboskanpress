from aiogram import types 
from loader import dp, db, checkUser, sendRegText
from keyboards.inline.turismKeys import turismKeys
from keyboards.inline.contactAdminKey import contactAdmin
from keyboards.inline.registrationKey import regKey
from keyboards.inline.auksionKeys import auksionKey
from keyboards.default.sectors import sectorKeys
from keyboards.default.regionKeys import aboutRegionKeys
from keyboards.default.rahbariyatKeys import mainKey


@dp.message_handler(text="🌏 Туман ҳақида")
async def handleAboutRegion(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply_photo(photo="AgACAgIAAxkBAAIKbWR8QW66Hpg1rWGCTNg77hciYy1bAALoyTEbO8DpS7iKoMSR1eBxAQADAgADeQADLwQ", caption="📈 Избоскан туманининг асосий кўрсатгичлари ва ижтимоий-иқтисодий ҳолати билан танишмоқчи бўлсангиз, қуйидаги тугмачалардан бирини босинг! \n\n<b>❗️Эслатиб ўтамиз:</b> <i>Мазкур маълумотлар 2022 йил январь-декабрь ойлари мисолида тақдим этилмоқда.</i>", reply_markup=aboutRegionKeys, parse_mode="HTML")
  else:
    await sendRegText(message)

@dp.message_handler(text="🏛 Раҳбарият")
async def handleMenu(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.answer(text="Қуйидаги тугмалардан бирини танланг", reply_markup=mainKey)
  else:
    await sendRegText(message)

@dp.message_handler(text = "🏘 МФЙлар ҳақида")
async def handleMenu(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply("Керакли Секторлардан бирини танланг: ", reply_markup=sectorKeys)
  else:
    await sendRegText(message)

@dp.message_handler(text = "🗒 Бўш иш ўринлари")
async def handleMenu(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply_document(document="BQACAgIAAxkBAAIDJ2R17j7t4Yhe_0cCzDTaUfhEZWctAAK8LwACkcGxS0qvOrt75x4FLwQ", caption="Aндижон Вилояти Избоскан туманида жойлашган корхона ва ташкилотлардаги мавжуд бўш иш ўринлари тўғрисида маълумот.Избоскан туманида жойлашган корхона ва ташкилотлардаги мавжуд бўш иш ўринлари тўғрисида маълумот \n\n<i>(Ушбу маълумот ҳар ойнинг 15-санасига қадар янгиланиб борилади)</i>", parse_mode="HTML")
  else:
    await sendRegText(message)

@dp.message_handler(text = '📝 "E-auksion"')
async def handleContactKey(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply_video(video="BAACAgIAAxkBAAIHtGR4qp-qSPVd2V3CO7FIJNSDxjTXAAJkKQACZFHIS1-lY9RJ5G7jLwQ", caption="Сизда “E-auksion” савдо ва танловларида иштирок этиш тартиблари ва савдо платформасидан фойдаланишда маълумотлар олмоқчи бўлсангиз “Электрон онлайн-аукционларни ташкил этиш маркази” ДУКнинг Андижон вилояти ҳудудий вакилларига мурожаат қилишигиз мумкинлигини эслатиб ўтамиз. \n\nТел рақамлар: \n☎️ +998 99 207-26-14 \n☎️ +998 74 223-22-12 \n\n“Электрон онлайн-аукционларни ташкил этиш маркази” ДУКнинг Андижон вилояти ҳудудий вакили Жамшидбек Исроилов.", reply_markup=auksionKey)
  else:
    await sendRegText(message)

@dp.message_handler(text="🛩 Туман туризми")
async def turismHandle(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply_video(video="BAACAgIAAxkBAAIJVmR8I_2SuQvwWBU3syU1n1cgGhNwAAKdOQACO8DhS2p9XLkDNx_QLwQ", caption="Избосканинг туризм салоҳиятидан бохабармисиз? \n\nХабарингиз бўлмаса, ушбу маълумотлар айнан Сизлар учун!", reply_markup=turismKeys)
  else:
    await sendRegText(message)

@dp.message_handler(text = "☎️ Биз билан боғланиш")
async def handleContactKey(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.answer(f"Биз билан боғланиш учун қуйидаги тугма орқали ботга тўғридан-тўғри хабарингизни юборинг ёки ишонч телефон рақамларига мурожаат қилинг: \n\n⚡Aбдуносир Мамажонов (Избоскан тумани матбуот хизмати раҳбари — Aхборот сиёсати масалалари бўйича ҳоким маслаҳатчиси) \n☎️  +998 93 214 12 99 \n\nИзбоскан тумани расмий саҳифалари: \n<a href='https://izboskanpress.uz/'>Web-sayt</a> | <a href='https://www.facebook.com/profile.php?id=100081700170350'>Facebook</a> | <a href='http://www.youtube.com/channel/UCyKEzU3YmNM2Cd7Ri2rfJtA'>You Tube</a> | <a href='https://www.instagram.com/izboskanpressuz/'>Instagram</a> | <a href='https://twitter.com/izboskanpress'>Twitter</a> | <a href='https://t.me/izboskanpress'>Telegram</a>",  disable_web_page_preview=True, reply_markup=contactAdmin)
  else:
    await sendRegText(message)

