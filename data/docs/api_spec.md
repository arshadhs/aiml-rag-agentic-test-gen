# API Specification

## Overview

This document describes the expected behaviour of the authentication service used in the RAG test generation demo.

The current demo implementation is function-based rather than a full HTTP API, but the behaviour is written in an API-style format so that the RAG system can retrieve requirements and generate meaningful test cases.

## Endpoint: Login

### Operation

`login(username, password, users_db)`

### Description

Authenticates a user by checking whether:

1. Username and password are provided
2. The username exists
3. The account is not locked
4. The supplied password matches the stored password

### Request Parameters

| Field | Type | Required | Description |
|---|---|---:|---|
| username | string | Yes | Unique username of the user |
| password | string | Yes | Plain-text password for this demo only |
| users_db | dictionary | Yes | In-memory user data store |

### Example User Database

```python
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
```

### Successful Response

```python
{
    "success": True,
    "message": "Login successful"
}
```

### Failed Responses

#### Missing Username or Password

```python
{
    "success": False,
    "message": "Username and password are required"
}
```

#### Invalid Username or Password

```python
{
    "success": False,
    "message": "Invalid username or password"
}
```

#### Locked Account

```python
{
    "success": False,
    "message": "Account is locked"
}
```

## Expected Test Types

The test generator should produce:

- Unit tests for valid login
- Unit tests for invalid password
- Unit tests for unknown user
- Unit tests for locked account
- Unit tests for missing username
- Unit tests for missing password
- Tests that verify response structure
- Tests that verify no sensitive user detail is leaked
