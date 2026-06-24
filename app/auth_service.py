"""
Authentication service.

Code under Test.
"""


def login(username, password, users_db):
    """
    Authenticate a user against an in-memory user database.

    Args:
        username (str): Username supplied by the user.
        password (str): Password supplied by the user.
        users_db (dict): Dictionary containing user records.

    Returns:
        dict: Authentication result containing success flag and message.
    """

    if not username or not password:
        return {
            "success": False,
            "message": "Username and password are required"
        }

    user = users_db.get(username)

    if user is None:
        return {
            "success": False,
            "message": "Invalid username or password"
        }

    if user.get("locked", False):
        return {
            "success": False,
            "message": "Account is locked"
        }

    if user.get("password") != password:
        return {
            "success": False,
            "message": "Invalid username or password"
        }

    return {
        "success": True,
        "message": "Login successful"
    }