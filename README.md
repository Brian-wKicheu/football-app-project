# Football Club Website

A simple web-based football club management website built with **Django, JavaScript, HTML, and CSS**. The system allows football club members to register their details and provides a simple interface for managing and displaying registered members.

## Features

- Member registration
- Member information management
- Responsive web interface
- Form validation
- Django-based backend
- Dynamic frontend interactions using JavaScript
- Clean and simple HTML/CSS interface
- SQLite database for development
- Django admin panel for managing members

## Tech Stack

### Backend
- **Python**
- **Django**
- **SQLite**

### Frontend
- **HTML5**
- **CSS3**
- **JavaScript**

## Project Structure

```text
football-club/
│
├── manage.py
├── requirements.txt
│
├── football_club/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── members/
│   ├── migrations/
│   ├── templates/
│   │   └── members/
│   │       ├── home.html
│   │       ├── register.html
│   │       └── members.html
│   ├── static/
│   │   └── members/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── js/
│   │           └── script.js
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
└── db.sqlite3
```

## Member Registration

The registration form can collect information such as:

- Full name
- Email address
- Phone number
- Date of birth
- Playing position
- Jersey number
- Emergency contact
- Registration date

Registered members are stored in the Django database and can be managed through the Django admin interface.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Brian-wKicheu/football-app-project
cd football-app-project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an admin account

```bash
python manage.py createsuperuser
```

Follow the prompts to create the administrator account.

### 6. Start the development server

```bash
python manage.py runserver
```

Open the website at:

```text
http://127.0.0.1:8000/
```

The Django administration panel is available at:

```text
http://127.0.0.1:8000/admin/
```

## How It Works

1. A visitor opens the football club website.
2. The visitor selects **Register**.
3. The registration form is displayed.
4. The visitor enters their details.
5. Django validates and processes the submitted information.
6. The member's information is stored in the database.
7. Administrators can view and manage registered members through the Django admin panel.

## Future Improvements

Possible future enhancements include:

- Member login and authentication
- Player profiles
- Team and squad management
- Match fixtures and results
- League standings
- Online announcements
- Training schedules
- Member profile photos
- Email notifications
- Payment and membership tracking
- REST API integration

## Purpose

This project is designed as a simple demonstration of building a **full-stack web application using Django and frontend web technologies**, with a focus on football club member registration and basic club management.

## License

This project is intended for educational and demonstration purposes.
