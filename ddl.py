# ddl.py

# Name: Jonah Gates
# Date: 2024-06-25
# Ownership: This code is proprietary and owned by Jonah Gates. Redistribution or modification without permission is prohibited.

import sqlite3

def initialize_database():
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS meetings(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT
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
			meeting_name TEXT,
			user_name TEXT,
			item TEXT,
			completion TEXT,
			notes TEXT,
			date TIMESTAMP,
			FOREIGN KEY (meeting_id) REFERENCES meetings(id),
			FOREIGN KEY (user_id) REFERENCES users(id)
		)
		"""
	)

	conn.commit()
	conn.close()
