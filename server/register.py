def register_user(conn_db, username, password):
    # Check if the user already exists
    cursor = conn_db.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    if row is not None:
        message = "Username already in use"
        return message
    conn_db.execute(f"INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn_db.commit()

    message = "Registration successful!"
    return message
