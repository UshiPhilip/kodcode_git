def create_admin_user(name, email, role):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    return name, email, role, "2024-01-01", True