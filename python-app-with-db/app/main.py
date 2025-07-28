from flask import Flask
from db import get_connection

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/db')
def db_version():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"PostgreSQL version: {version[0]}"
    except Exception as e:
        return f"DB connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
