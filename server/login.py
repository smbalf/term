def login_user(conn_db, username, password):
    # Check if the user exists and the password matches
    cursor = conn_db.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    row = cursor.fetchone()
    if row is not None:
        response = "Login successful!"
        return response

    response = "Invalid username or password"
    return response
