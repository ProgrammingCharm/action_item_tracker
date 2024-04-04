# app.py

from dml import add_meeting, add_user, add_action_item, get_all_meetings, get_all_users
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# Check if form is for adding a meeting
		if 'name' in request.form and 'date' in request.form:
			name = request.form['name']
			date = request.form['date']
			add_meeting(name, date)
		# Check if form is for adding a user
		elif 'username' in request.form:
			username = request.form['username']
			add_user(username)
	meetings = get_all_meetings()
	users = get_all_users()
	return render_template('index.html', meetings=meetings, users=users)

@app.route('/add_action_item', methods=['GET', 'POST'])
def action_item():
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
	return render_template('add_action_item.html', meetings=meetings, users=users)
	
	
if __name__ == '__main__':
	app.run(debug=True)
	

	
