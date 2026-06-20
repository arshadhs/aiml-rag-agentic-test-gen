# Requirements

## Project Demo Domain

This sample application is a small authentication service used to demonstrate the AIML RAG Agentic Test Generator.

The service provides basic login functionality and account status checks.

## Functional Requirements

### FR-001: Successful Login

The system shall allow a registered user to log in using a valid username and password.

Acceptance Criteria:

- Given a registered user exists
- And the user provides the correct password
- When the login function is called
- Then the system returns a successful login response
- And the response message should be `Login successful`

### FR-002: Invalid Password

The system shall reject login attempts where the username is valid but the password is incorrect.

Acceptance Criteria:

- Given a registered user exists
- And the user provides an incorrect password
- When the login function is called
- Then the system returns a failed login response
- And the response message should be `Invalid username or password`

### FR-003: Unknown User

The system shall reject login attempts for usernames that do not exist.

Acceptance Criteria:

- Given the username does not exist
- When the login function is called
- Then the system returns a failed login response
- And the response message should be `Invalid username or password`

### FR-004: Locked Account

The system shall not allow a locked account to log in, even if the password is correct.

Acceptance Criteria:

- Given a registered user account is locked
- And the user provides the correct password
- When the login function is called
- Then the system returns a failed login response
- And the response message should be `Account is locked`

### FR-005: Empty Input Validation

The system shall reject empty username or password values.

Acceptance Criteria:

- Given the username or password is empty
- When the login function is called
- Then the system returns a failed login response
- And the response message should be `Username and password are required`

## Non-Functional Requirements

### NFR-001: Testability

The authentication logic should be simple to unit test without requiring a real database.

### NFR-002: Maintainability

The business logic should be separated from API or user-interface code.

### NFR-003: Security

Error messages should not reveal whether the username or password was incorrect.

## Test Generation Goals

The AI system should generate tests covering:

- Positive login path
- Invalid password path
- Unknown username path
- Locked account path
- Empty username path
- Empty password path
- Boundary and negative scenarios
