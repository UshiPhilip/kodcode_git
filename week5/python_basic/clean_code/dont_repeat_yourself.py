def create_admin_user(name, email, role):
    if not valid_name:
        raise ValueError("Invalid name")
    if not valid_email:
        raise ValueError("Invalid email")
    return name, email, role, "2024-01-01", True

def valid_name(name):
    return bool(name) and len(name) >= 2

def valid_email(email):
    return "@" in email