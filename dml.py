import sqlite3

def add_meeting(name):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		INSERT INTO meetings (name) VALUES (?)
		""", 
		(name,)
	)
	conn.commit()
	conn.close()
	
def add_user(name):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		INSERT INTO users (name) VALUES (?)
		""",
		(name,)
	)
	conn.commit()
	conn.close()

def add_action_item(meeting_id, user_id, item, completion, notes):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		INSERT INTO action_items (meeting_id, user_id, item, completion, notes, date) VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
		""",
		(meeting_id, user_id, item, completion, notes)
	)
	conn.commit()
	conn.close()
	
def get_all_meetings():
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM meetings")
	meetings = cursor.fetchall()
	conn.close()
	return meetings

def get_all_users():
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM users")
	users = cursor.fetchall()
	conn.close()
	return users

def get_all_action_items():
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM action_items")
	action_items = cursor.fetchall()
	conn.close()
	return action_items
	

