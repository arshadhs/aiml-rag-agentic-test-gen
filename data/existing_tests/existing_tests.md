# Existing Tests

This file represents the existing test suite before AI-generated tests are added.

The current project has only a small number of tests. The AI test generator should identify missing coverage and generate additional pytest tests.

## Existing pytest tests

```python
from app.auth_service import login


def test_login_success():
    users_db = {
        "alice": {
            "password": "password123",
            "locked": False
        }
    }

    result = login("alice", "password123", users_db)

    assert result["success"] is True
    assert result["message"] == "Login successful"


def test_invalid_password():
    users_db = {
        "alice": {
            "password": "password123",
            "locked": False
        }
    }

    result = login("alice", "wrong-password", users_db)

    assert result["success"] is False
    assert result["message"] == "Invalid username or password"
```

## Current Coverage Gaps

The existing tests do not cover:

- Unknown username
- Locked account
- Empty username
- Empty password
- Missing users database entry
- Response dictionary structure
- Security expectation that invalid username and invalid password return the same generic message

## AI Test Generation Task

The AI system should generate additional pytest tests that improve coverage and check the missing scenarios above.

Generated tests should follow the existing project style:

- Use pytest
- Use clear test names
- Use simple in-memory dictionaries
- Assert both `success` and `message`
- Avoid external services or database dependencies
