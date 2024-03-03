from flask import Flask, render_template, request, jsonify
import sqlite3
websitestart = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@websitestart.route('/')
@websitestart.route('/get_posts')
def index():
    selected_state = request.args.get('state')
    conn = get_db_connection()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        query = 'SELECT * FROM posts WHERE usstate = ?'
        params = [selected_state]
        print(params)
        posts = conn.execute(query, tuple(params)).fetchall()
        print(posts)
        conn.close()
        return render_template('index.html', posts=posts)
    else:
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        return render_template('base.html', posts=posts)

