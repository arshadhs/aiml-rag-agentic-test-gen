# Source Code

This file contains the demo source code that the RAG system can use to generate tests.

In the real project, this content may come directly from `.py` source files. For the first RAG demo, we keep it inside Markdown so the document loader can index it easily.

## File: app/auth_service.py

```python
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
```

## Important Business Rules

- Username and password are mandatory.
- Unknown users should not reveal that the username does not exist.
- Invalid password and unknown username should return the same generic error message.
- Locked accounts should be rejected before password validation.
- Successful login should only happen when the user exists, the account is not locked, and the password is correct.

## Suggested Tests

The generated test suite should include:

- `test_login_success`
- `test_invalid_password`
- `test_unknown_user`
- `test_locked_account`
- `test_empty_username`
- `test_empty_password`
- `test_invalid_user_and_invalid_password_use_same_message`
- `test_response_contains_success_and_message_keys`