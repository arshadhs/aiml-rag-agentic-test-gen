from app.auth_service import login

users_db = {
    "alice": {
        "password": "password123",
        "locked": False
    },
    "bob": {
        "password": "secure456",
        "locked": True
    }
}

def test_login_success():
    response = login("alice", "password123", users_db)
    assert response["success"] is True
    assert response["message"] == "Login successful"

def test_invalid_password():
    response = login("alice", "wrongpassword", users_db)
    assert response["success"] is False
    assert response["message"] == "Invalid username or password"

def test_unknown_user():
    response = login("charlie", "password123", users_db)
    assert response["success"] is False
    assert response["message"] == "Invalid username or password"

def test_locked_account():
    response = login("bob", "secure456", users_db)
    assert response["success"] is False
    assert response["message"] == "Account is locked"

def test_empty_username():
    response = login("", "password123", users_db)
    assert response["success"] is False
    assert response["message"] == "Username and password are required"

def test_empty_password():
    response = login("alice", "", users_db)
    assert response["success"] is False
    assert response["message"] == "Username and password are required"

def test_invalid_user_and_invalid_password_use_same_message():
    response_user = login("charlie", "wrongpassword", users_db)
    response_password = login("alice", "wrongpassword", users_db)
    assert response_user["message"] == response_password["message"] == "Invalid username or password"

def test_response_contains_success_and_message_keys():
    response = login("alice", "password123", users_db)
    assert "success" in response
    assert "message" in response