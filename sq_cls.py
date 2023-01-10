import sqlite3

class Database:

	def __init__(self):
		self.conn = sqlite3.connect("Bot.db")
		self.c = self.conn.cursor()

	def create(self):
		self.c.execute("""CREATE TABLE IF NOT EXISTS Users(
				telegram_id varchar(20),
				username varchar(25),
				contact varchar(15) NULL,
				location varchar(30) NULL
				)""")

	def insert(self, tg_id, username):
		self.c.execute(f"INSERT INTO Users (telegram_id, username) VALUES ('{tg_id}', '{username}')")
		return self.conn.commit()

	def select(self, tg_id):
		self.c.execute(f"SELECT * FROM Users WHERE telegram_id = '{tg_id}' ")
		return self.c.fetchone()

	def update_contact(self, tg_id, ph_num):
		self.c.execute(f"UPDATE Users SET contact = '{ph_num}' WHERE telegram_id = '{tg_id}' ")
		return self.conn.commit()

	def update_location(self, tg_id, lctn):
		self.c.execute(f"UPDATE Users SET location = '{lctn}' WHERE telegram_id = '{tg_id}' ")
		return self.conn.commit()