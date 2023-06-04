from aiogram import types
from loader import dp


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handlePhoto(message: types.Message):
    photo= message.photo[-1]
    print(photo)


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def handlePhoto(message: types.Message):
    doc_id = message.document.file_id
    print(doc_id)

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def handlePhoto(message: types.Message):
    doc_id = message.video.file_id
    print(doc_id)