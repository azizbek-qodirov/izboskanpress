from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
DEVID = env.str("DEVID")
ADMINS = env.list("ADMINS") 
IP = env.str("ip")
USER = env.str('USER')
DBPASSWORD=env.str('DBPASSWORD')
PORT=env.str('PORT')
DBNAME=env.str('DBNAME')
HOST=env.str('HOST')