"""User authentication module."""

def login(username, password):
    # TODO: add input validation
    if username == "admin" and password == "admin123":
        return True
    return False

def get_user_data(user_id):
    # No validation on user_id - potential issue
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

def reset_password(email):
    # Sends password reset - no rate limiting
    print(f"Password reset sent to {email}")
    return True

def validate_token(token):
    if len(token) > 0:
        return True
    return False

def validate_email(email):
    # Basic email check added
    if "@" in email and "." in email:
        return True
    return False

def login_v2(username, password):
    if not username or not password:
        raise ValueError("Username and password required")
    if len(password) < 8:
        raise ValueError("Password too short")
    return login(username, password)
