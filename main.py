from dotenv import load_dotenv     # pip install python-dotenv
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from python_aternos import Client, atserver


load_dotenv()
bot = Bot(token=os.environ.get('TOKEN'))
dp = Dispatcher(bot)

atclient = Client()
atclient.login_with_session(os.environ.get('ATERNOS_SESSION'))
# atclient.login()
aternos = atclient.account
servs = aternos.list_servers()
# servs[0].start()
srvs = aternos.list_servers()

for srv in srvs:
    print()
    print('***', srv.servid, '***')
    srv.fetch()
    print(srv.domain)
    print(srv.motd)
    print('*** Status:', srv.status)
    print('*** Full address:', srv.address)
    print('*** Port:', srv.port)
    print('*** Name:', srv.subdomain)
    print('*** Minecraft:', srv.software, srv.version)
    print('*** IsBedrock:', srv.edition == atserver.Edition.bedrock)
    print('*** IsJava:', srv.edition == atserver.Edition.java)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['startsrv'])
async def process_start_command(message: types.Message):
    await message.reply("Сервер запущен")


if __name__ == '__main__':
    executor.start_polling(dp)

