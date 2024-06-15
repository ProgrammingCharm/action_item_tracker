import sqlite3
import time

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

def add_action_item(meeting_name, user_name, item, completion, notes, date):
	meeting_id = get_id_by_meeting_name(meeting_name)
	user_id = get_id_by_user_name(user_name)
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		INSERT INTO action_items (meeting_id, user_id, meeting_name, user_name, item, completion, notes, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
		""",
		(meeting_id, user_id, meeting_name, user_name, item, completion, notes, date)
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
	cursor.execute("SELECT * FROM action_items WHERE completion == 'not completed'")
	action_items = cursor.fetchall()
	conn.close()
	return action_items
	
	
def get_id_by_meeting_name(meeting_name):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		SELECT id FROM meetings WHERE name = ?
		""",
		(meeting_name,)
	)
	meeting_id = cursor.fetchone()
	conn.close()
	return meeting_id[0] if meeting_id else None


def get_id_by_user_name(user_name):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		SELECT id FROM users WHERE name = ?
		""",
		(user_name,)
	)
	user_id = cursor.fetchone()
	conn.close()
	return user_id[0] if user_id else None	
	

def get_action_items_by_meeting(meeting_id):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		SELECT action_items.*, meetings.name
		FROM action_items
		JOIN meetings ON action_items.meeting_id = meetings.id
		WHERE action_items.meeting_id = ? and completion == 'not completed'
		""",
		(meeting_id,)
	)
	action_items = cursor.fetchall()
	conn.close()
	return action_items
	
def get_action_items_by_user(user_id):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		SELECT action_items.*, users.name
		FROM action_items
		JOIN users ON action_items.user_id = users.id
		WHERE action_items.user_id = ? and completion == 'not completed'
		""",
		(user_id,)
	)
	action_items = cursor.fetchall()
	conn.close()
	return action_items
	
def update_action_item_completion(completed_action_item_ids):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.executemany(
		"""
		UPDATE action_items SET completion='completed'
		WHERE id = ?
		""",
		[(id,) for id in completed_action_item_ids]
	)
	conn.commit()
	conn.close()
				
				
def get_id_by_action_item_name(action_item_name):
	conn = sqlite3.connect('action_item_tracker.db')
	cursor = conn.cursor()
	cursor.execute(
		"""
		SELECT id FROM action_items
		WHERE item = ?
		""",
		(action_item_name,)
	)
	item_id = cursor.fetchone()
	conn.close()
	return item_id[0] if item_id else None	
	
	
def append_note_to_action_item(action_item_id, new_note):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		UPDATE action_items
		SET notes = notes || '\n' || ?
		WHERE id = ?
		""",
		(new_note, action_item_id)
	)
	conn.commit()
	conn.close()

def get_timestamp():
	current_time = time.localtime()
	return time.strftime('%Y-%m-%d %H:%M:%S', current_time)
	
def append_timestamp_to_date(action_item_id, date_time):
	conn = sqlite3.connect("action_item_tracker.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		UPDATE action_items
		SET date = date || '\n' || ?
		WHERE id = ?
		""",
		(date_time, action_item_id)
	)
	conn.commit()
	conn.close()
