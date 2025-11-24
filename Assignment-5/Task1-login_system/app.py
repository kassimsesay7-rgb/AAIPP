import os
import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Optional, Tuple

from flask import Flask, request, redirect, render_template, session, url_for, g, flash
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

APP_DIR = Path(__file__).parent
DB_PATH = APP_DIR / "app.db"


def create_app() -> Flask:
	app = Flask(__name__)

	secret_key = os.environ.get("SECRET_KEY")
	if not secret_key:
		# Generate a strong random key for dev-only usage; recommend setting SECRET_KEY in env
		secret_key = os.urandom(32).hex()
		app.logger.warning("SECRET_KEY not set in environment; generated a temporary key for this run.")
	app.secret_key = secret_key

	@app.before_request
	def before_request() -> None:
		g.db = get_db_connection()

	@app.teardown_request
	def teardown_request(exception) -> None:  # type: ignore[no-redef]
		conn = getattr(g, "db", None)
		if conn is not None:
			conn.close()

	# Initialize database if not present
	initialize_database()

	@app.get("/")
	def index():
		if session.get("user_id"):
			return redirect(url_for("dashboard"))
		return redirect(url_for("login"))

	@app.route("/register", methods=["GET", "POST"])
	def register():
		if request.method == "POST":
			username = request.form.get("username", "").strip()
			password = request.form.get("password", "")

			if not username or not password:
				flash("Username and password are required.", "error")
				return redirect(url_for("register"))

			if len(password) < 8:
				flash("Password must be at least 8 characters.", "error")
				return redirect(url_for("register"))

			password_hash = generate_password_hash(password)
			try:
				with closing(g.db.cursor()) as cur:
					cur.execute(
						"INSERT INTO users (username, password_hash) VALUES (?, ?)",
						(username, password_hash),
					)
					g.db.commit()
			except sqlite3.IntegrityError:
				flash("Username already exists.", "error")
				return redirect(url_for("register"))

			flash("Registration successful. Please log in.", "success")
			return redirect(url_for("login"))

		return render_template("register.html")

	@app.route("/login", methods=["GET", "POST"])
	def login():
		if request.method == "POST":
			username = request.form.get("username", "").strip()
			password = request.form.get("password", "")

			user = find_user_by_username(g.db, username)
			if not user:
				flash("Invalid username or password.", "error")
				return redirect(url_for("login"))

			user_id, db_username, db_password_hash = user
			if not check_password_hash(db_password_hash, password):
				flash("Invalid username or password.", "error")
				return redirect(url_for("login"))

			session["user_id"] = user_id
			session["username"] = db_username
			flash("Logged in successfully.", "success")
			return redirect(url_for("dashboard"))

		return render_template("login.html")

	@app.get("/dashboard")
	def dashboard():
		if not session.get("user_id"):
			return redirect(url_for("login"))
		return render_template("dashboard.html", username=session.get("username"))

	@app.post("/logout")
	def logout():
		session.clear()
		flash("Logged out.", "success")
		return redirect(url_for("login"))

	return app


def get_db_connection() -> sqlite3.Connection:
	conn = sqlite3.connect(DB_PATH)
	conn.row_factory = sqlite3.Row
	return conn


def initialize_database() -> None:
	with closing(sqlite3.connect(DB_PATH)) as conn:
		with closing(conn.cursor()) as cur:
			cur.execute(
				"""
				CREATE TABLE IF NOT EXISTS users (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					username TEXT NOT NULL UNIQUE,
					password_hash TEXT NOT NULL
				)
				"""
			)
			conn.commit()


def find_user_by_username(conn: sqlite3.Connection, username: str) -> Optional[Tuple[int, str, str]]:
	with closing(conn.cursor()) as cur:
		cur.execute("SELECT id, username, password_hash FROM users WHERE username = ?", (username,))
		row = cur.fetchone()
		if not row:
			return None
		return int(row[0]), str(row[1]), str(row[2])


if __name__ == "__main__":
	app = create_app()
	# Enable debug only via environment variable FLASK_DEBUG=1
	debug_mode = os.environ.get("FLASK_DEBUG") == "1"
	app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)), debug=debug_mode)
