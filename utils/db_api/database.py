import asyncpg
from data.config import USER, DBPASSWORD, DBNAME, HOST, PORT
import datetime

class DatabaseManager:
    def __init__(self) -> None:
        self.connection = None
    async def connect(self):
        try:
            self.connection = await asyncpg.connect(dsn=f"postgresql://{USER}:{DBPASSWORD}@{HOST}:{PORT}/{DBNAME}")
            print('Succesfully connected to the database pgsql!')
        except Exception as e:  
            print('Something went wrong while connecting pgsql: ', e)
    async def disconnect(self):
        await self.connection.close()

    async def fetch(self, query):
        return await self.connection.fetch(query)
    async def fetchval(self, query):
        return await self.connection.fetchval(query)
    async def fetchrow(self, query):
        return await self.connection.fetchrow(query)

    async def execute(self, query):
        return await self.connection.execute(query)
    
    async def add_user(self, userID, fullName, phone, joined_date):
        query = "INSERT INTO users (id, fullname, phone, joined_date) VALUES ($1, $2, $3, $4)"
        await self.connection.execute(query, userID, fullName, phone, joined_date)
    
    async def get_user(self, telegram_id):
        query = "SELECT * FROM users WHERE id = $1"
        return await self.connection.fetchrow(query, telegram_id)

    async def count_users(self):
        query = "SELECT count(*) FROM users"
        return await self.connection.fetchval(query)
    
    async def count_today_joined_users(self):
        today = datetime.date.today()
        query = "SELECT count(*) FROM users WHERE joined_date = $1"
        return await self.connection.fetchval(query, today)
    

    async def count_this_month_joined_users(self):
        today = datetime.date.today()
        start_of_month = datetime.date(today.year, today.month, 1)
        query = "SELECT count(*) FROM users WHERE joined_date >= $1"
        return await self.connection.fetchval(query, start_of_month)


    async def check_user_exists(self, telegram_id):
        query = "SELECT COUNT(*) FROM users WHERE id = $1"
        result = await self.connection.fetchval(query, telegram_id)
        return result == 1