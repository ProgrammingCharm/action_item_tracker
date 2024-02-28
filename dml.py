import sqlite3

def add_meeting(name, date):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		INSERT INTO meetings (name, date) VALUES (?, ?)
		""", 
		(name, date)
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

def add_action_item(meeting_id, user_id, item, notes, completion, owner):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		INSERT INTO action_items (meeting_id, user_id, item, notes, completion, owner) VALUES (?, ?, ?, ?, ?, ?)
		""",
		(meeting_id, user_id, item, notes, completion, owner)
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
	
		
	
