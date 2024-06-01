# app.py

from dml import add_meeting, add_user, add_action_item, get_all_meetings, get_all_users, get_all_action_items, get_id_by_meeting_name, get_action_items_by_meeting, get_id_by_user_name, get_action_items_by_user, update_action_item_completion
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# If form is for adding an action item
		if 'meeting_id' in request.form and 'user_id' in request.form and 'item' in request.form and 'completion' in request.form and 'notes' in request.form:
			meeting_id = request.form['meeting_id']
			user_id = request.form['user_id']
			item = request.form['item']
			completion = request.form.get('completion', 'not completed')
			notes = request.form['notes']
			add_action_item(meeting_id, user_id, item, completion, notes)
	meetings = get_all_meetings()
	users = get_all_users()
	action_items = get_all_action_items()
	return render_template('index.html', meetings=meetings, users=users, action_items=action_items)
	
@app.route('/filter_by_meeting', methods=['POST'])
def filter_by_meeting():
	meeting_name = request.form['meeting_name']
	#print(f"Meeting Name: {meeting_name}")
	meeting_id = get_id_by_meeting_name(meeting_name)
	#print(f"Meeting ID: {meeting_id}")
	#print(f"Meeting Name: {meeting_name}")
	action_items = get_action_items_by_meeting(meeting_id)
	#print(f"Action Items: {action_items}")
	return render_template('index.html', meetings=get_all_meetings(), users=get_all_users(), action_items=action_items)
	
@app.route('/filter_by_user', methods=["POST"])
def filter_by_user():
	user_name = request.form['user_name']
	print(f"User Name: {user_name}")
	user_id = get_id_by_user_name(user_name)
	print(f"User ID: {user_id}")
	action_items = get_action_items_by_user(user_id)
	print(f"Action Items: {action_items}")
	return render_template('index.html', meetings=get_all_meetings(), users=get_all_users(), action_items=action_items)

@app.route('/mark_complete', methods=['POST'])
def mark_complete():
	completed_ids = request.form.getlist('completed_ids')
	update_action_item_completion(completed_ids)
	return index()
	
@app.route('/settings', methods=['GET', 'POST'])
def add_meeting_user():
	if request.method == 'POST':
		# Check if form is for adding a meeting
		if 'name' in request.form:
			name = request.form['name']
			add_meeting(name)
		# Check if form is for adding a user
		elif 'username' in request.form:
			username = request.form['username']
			add_user(username)
	meetings = get_all_meetings()
	users = get_all_users()
	return render_template('settings.html', meetings=meetings, users=users)
	
	
if __name__ == '__main__':
	app.run(debug=True)
	


