# Django Project Setup Guide

This guide provides instructions for setting up and running the Django project.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

## Creating a Superuser

To create a superuser for accessing the Django admin panel, use the following command:

```bash
python manage.py createsuperuser
```

You will be prompted to enter:
- Username
- Email address
- Password (entered twice for confirmation)

### Example:
```bash
$ python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: 
Password (again): 
Superuser created successfully.
```

### Alternative - Non-interactive Mode:
```bash
python manage.py createsuperuser --username admin --email admin@example.com --noinput
```
(You'll need to set the password separately using Django shell)

## Running the Application

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application:**
   - Homepage: http://127.0.0.1:8000/
   - Login: http://127.0.0.1:8000/registration/login/
   - Admin panel: http://127.0.0.1:8000/admin/
   - API endpoints:
     - User registration: http://127.0.0.1:8000/registration/api/register/
     - User list: http://127.0.0.1:8000/registration/api/users/
     - Students: http://127.0.0.1:8000/registration/api/students/

## Running Tests

To run the test suite:

```bash
python manage.py test
```

For verbose output:

```bash
python manage.py test --verbosity=2
```

## Project Structure

```
Lab3_backend/
├── MyProject/              # Main project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── templates/         # Project-level templates
├── registration/          # Registration app
│   ├── models.py          # UserRegistration model
│   ├── views.py           # Views for login, user list, API
│   ├── urls.py            # App URL patterns
│   ├── templates/         # App templates
│   │   └── registration/
│   │       ├── login.html
│   │       └── users_list.html
│   └── tests.py           # Test suite
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Features

- User registration and login
- User list view (requires login)
- REST API for user management
- Student management API endpoints
- Secure password hashing
- CSRF protection
- Session management

## Notes

- The application is configured to run on multiple hosts (localhost, 127.0.0.1, production URL)
- Templates are properly configured in both MyProject/templates and registration/templates
- Database file (db.sqlite3) is excluded from version control
- All tests pass successfully with comprehensive coverage
