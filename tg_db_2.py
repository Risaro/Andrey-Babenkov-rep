
import logging
from aiogram import Bot, Dispatcher, types, executor
import pymysql


bot = Bot(token="5886633479:AAHS7oha7qK3Ashom9gJkPPzTKoIckDPQJ8")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Здарова ботик!Я умею выполнять команды Кто ты?,Ты бот?,умножить,Отнять,прибавить,Разделить")


@dp.message_handler(commands="getPos")
async def cmd_test(message: types.Message):
    await message.reply("Будущая команда пока в разработке")


i = 1


@dp.message_handler(commands=['create'])
async def cmd_text(message: types.Message):
    con = pymysql.connect(host="185.231.153.103", user="study", password="study123",database="egor")
    with con:
      cur = con.cursor()
      cur.execute("SELECT VERSION()")
      version = cur.fetchone()
      await bot.send_message(message.from_user.id,str(version[0]))
@dp.message_handler(commands=['show_user'])
async def cmd_show_user(message: types.message):
    con = pymysql.connect(host="185.231.153.103", user="study", password="study123",database="egor")
    with con:
        cur = con.cursor()
        cur.execute("sELECT * FROM users")
        rows= cur.fetchall()
        for row in rows:
            await bot.send_message(message.from_user.id , f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
users = {1,1}
@dp.message_handler(commands=["insert"])
async def cmd_insert(message: types.Message):
    await bot.send_message(message.from_user.id, "\n".join(f"* {user_id}" for user_id in users))

if __name__ == "__main__":
    executor.start_polling(dp)



