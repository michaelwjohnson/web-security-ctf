import os
from flask import Flask, request, render_template, session, redirect, url_for
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__)
app.secret_key = "supersecretkey123"  # Intentionally weak for demo purposes


# Initialize the database
def init_db():
    # Connect to the database
    conn = sqlite3.connect("users.db")

    # Create a cursor object to interact with the database
    c = conn.cursor()

    # Create the 'users' table if it doesn't already exist
    c.execute(
        """CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT, role TEXT)"""
    )

    # Insert test users with obvious hints
    c.execute(
        "INSERT OR IGNORE INTO users VALUES (?, ?, ?)", ("guest", "guest123", "user")
    )
    c.execute(
        "INSERT OR IGNORE INTO users VALUES (?, ?, ?)",
        ("admin", "admin123", "admin"),
    )

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()


init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Connect to the database
        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        # Execute the SQL query with the user input
        query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(
            username, password
        )

        try:
            c.execute(query)
            user = c.fetchone()
            if user:
                # Login successful!
                session["username"] = username
                session["role"] = user[2]
                return redirect(url_for("dashboard"))
            else:
                # Login failed
                return "Invalid username or password", 401
        except sqlite3.OperationalError as e:
            # Handle SQL errors
            return "Error: {}".format(e), 500
        finally:
            conn.close()
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    # Check if the user is logged in
    if "username" not in session:
        # Redirect the user to the login page if they are not logged in
        return redirect(url_for("login"))

    # Render the dashboard page with the username and role of the logged in user
    return render_template(
        "dashboard.html", username=session["username"], role=session["role"]
    )


@app.route("/logout")
def logout():
    # Clear the session data
    session.clear()
    # Redirect the user to the login page
    return redirect(url_for("login"))


@app.route("/flag")
def flag():
    # Check if the current user's role in the session is not 'admin'
    if session.get("role") != "admin":
        # If the user is not an admin, return an access denied message
        # with a 403 Forbidden HTTP status code
        return "Access Denied: Admin privileges required", 403

    # If the user is an admin, return the flag string
    return "FLAG{easy_sql_injection}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
