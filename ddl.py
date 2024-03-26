import sqlite3

conn = sqlite3.connect("action_item_tracker.db")
cursor = conn.cursor()

cursor.execute(
	"""
	CREATE TABLE IF NOT EXISTS meetings(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		date DATE
	)
	"""
)

cursor.execute(
	"""
	CREATE TABLE IF NOT EXISTS users(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT
	)
	"""
)		

cursor.execute(
	"""
	CREATE TABLE IF NOT EXISTS action_items(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		meeting_id INTEGER,
		user_id INTEGER,
		item TEXT,
		completion TEXT,
		notes TEXT,
		FOREIGN KEY (meeting_id) REFERENCES meetings(id),
		FOREIGN KEY (user_id) REFERENCES users(id)
	)
	"""
)

conn.commit()
conn.close()

