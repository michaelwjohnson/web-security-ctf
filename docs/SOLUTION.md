# Web Security CTF - Challenge Walkthrough

This document provides a detailed walkthrough of the Web Security CTF challenge. This is meant for educational purposes and to help understand common web security vulnerabilities.

## Challenge Overview

This CTF challenge focuses on two main security concepts:

1. SQL Injection vulnerabilities
2. Privilege Escalation

## Challenge Goals

1. Successfully authenticate into the application
2. Escalate privileges to admin level
3. Access and retrieve the flag

## Available Information

The application provides the following endpoints:

- `/` - Home page
- `/login` - Login interface
- `/dashboard` - User dashboard (requires authentication)
- `/flag` - Flag endpoint (requires admin privileges)

A guest account is available for initial access.

## Solution Path

### Step 1: Initial Reconnaissance

1. Examine the login page at `/login`
2. Note the hint: "Sometimes the simplest approach works best..."
3. Try the guest credentials to access basic functionality

### Step 2: Login Bypass through SQL Injection

The login form is vulnerable to SQL injection. There are multiple ways to exploit this:

#### Method 1: Using Admin Credentials

The admin account uses weak, easily guessable credentials that could be discovered through common password lists or brute force attempts.

#### Method 2: SQL Injection

The SQL query used is:

```sql
SELECT * FROM users WHERE username = ? AND password = ?
```

You can bypass this using SQL injection techniques such as:

- Using the OR operator to make the WHERE clause always evaluate to true: `' or 1=1--`, `' or 1=1#`, `' or 1=1/*`
- Using comment syntax to ignore the rest of the query: `admin' --`, `admin' #`, `admin'/*`
- Modifying the query structure to authenticate as a specific user without knowing their password: ') or `'1'='1--, ')` or `('1'='1--`

### Step 3: Accessing the Flag

1. Once logged in as admin, navigate to the dashboard
2. Click the "Get Flag" link
3. The flag will be displayed upon successful access

## Security Lessons

This CTF demonstrates several important security concepts:

1. **Weak Passwords**: Using easily guessable passwords for privileged accounts is dangerous
2. **SQL Injection**: Always use parameterized queries and proper input validation
3. **Access Control**: Implement proper authorization checks for sensitive endpoints
4. **Session Management**: Verify user roles and permissions on each sensitive request

## Note

This is an educational CTF challenge. The vulnerabilities demonstrated here are intentional for learning purposes. Never implement these patterns in production applications.
