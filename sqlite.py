import sqlite3

conn = sqlite3.connect("Bot.db")

c = conn.cursor()

def db_create():
	c.execute("""CREATE TABLE IF NOT EXISTS Bot_Users (
		telegram_id varchar(12), 
		username varchar(100),
		first_name varchar(50),
		phone_number varchar(15) NULL,
		location varchar(30) NULL
		)""")

def db_insert(tg_id, username, first_name):
	c.execute(f"INSERT INTO Bot_Users (telegram_id, username, first_name) VALUES ('{tg_id}', '{username}', '{first_name}')")
	conn.commit()

def db_select(tg_id):
	c.execute(f"SELECT * from Bot_Users WHERE telegram_id = '{tg_id}' ")
	return c.fetchone()

def db_select_all():
	c.execute("SELECT * from Bot_Users")
	return c.fetchall()

def db_update(tg_id, location):
	c.execute(f"UPDATE Bot_Users SET location = '{location[0], location[1]}' WHERE telegram_id = '{tg_id}' ")
	conn.commit()