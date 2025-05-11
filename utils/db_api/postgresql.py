from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_chanel(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Channel (
        id SERIAL PRIMARY KEY,
        chanelll VARCHAR(301) NOT NULL,
        url varchar(301) NOT NULL
                );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, telegram_id, username):
        sql = "INSERT INTO users (full_name, telegram_id, username) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, telegram_id, username, fetchrow=True)

    async def add_chanell(self, chanelll, url):
        sql = "INSERT INTO Channel (chanelll, url) VALUES($1, $2) returning *"
        return await self.execute(sql, chanelll, url, fetchrow=True)

    async def add_json_file_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_chanel(self):
        sql = "SELECT * FROM Channel"
        return await self.execute(sql, fetch=True)

    async def get_chanel(self, channel):
        sql = f"SELECT * FROM Channel WHERE chanelll=$1"
        return await self.execute(sql, channel, fetch=True)

    async def select_top_users(self):
        sql = "SELECT * FROM Users WHERE score IS NOT NULL ORDER BY score DESC LIMIT 20"
        return await self.execute(sql, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_score(self, score, telegram_id):
        sql = "UPDATE Users SET score=$1 WHERE telegram_id=$2"
        return await self.execute(sql, score, telegram_id, execute=True)

    async def update_chanel(self, chanelll, url, id):
        sql = "UPDATE Channel SET chanelll=$1, url=$2 WHERE id=$3"
        return await self.execute(sql, chanelll, url, id, execute=True)

    async def update_user_oldd(self, oldd, telegram_id):
        sql = "UPDATE Users SET oldd=$1 WHERE telegram_id=$2"
        return await self.execute(sql, oldd, telegram_id, execute=True)

    async def update_user_args(self, user_args, telegram_id):
        sql = "UPDATE Users SET user_args=$1 WHERE telegram_id=$2"
        return await self.execute(sql, user_args, telegram_id, execute=True)

    async def update_user_phone(self, phone, telegram_id):
        sql = "UPDATE Users SET phone=$1 WHERE telegram_id=$2"
        return await self.execute(sql, phone, telegram_id, execute=True)

    async def update_user_score(self, score, telegram_id):
        sql = "UPDATE Users SET score=$1 WHERE telegram_id=$2"
        return await self.execute(sql, score, telegram_id, execute=True)

    async def delete_users(self, telegram_id):
        sql = "DELETE FROM Users WHERE telegram_id=$1"
        await self.execute(sql, telegram_id, execute=True)

    async def delete_channel(self, chanel):
        sql = "DELETE FROM Channel WHERE chanelll=$1"
        await self.execute(sql, chanel, execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    async def drop_Chanel(self):
        await self.execute("DROP TABLE Channel", execute=True)
