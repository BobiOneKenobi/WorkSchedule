# WorkSchedule

WorkSchedule is a Django web application for managing employees, shifts, leave requests, and company holidays.

It was developed as part of the Django Basics course and demonstrates core Django concepts such as models, forms, class-based views, validation, template inheritance, and clean modular project structure.

## Features

- Employee management (full CRUD functionality)

- Shift scheduling system with:
  - automatic shift type assignment (morning / afternoon / night)
  - validation to prevent overlapping shifts
  - maximum shift duration of 12 hours

- Leave request management:
  - automatic "pending" status on creation
  - validation to prevent overlapping leave requests
  - approval handled via Django admin

- Company holiday listing

- Filtered views for morning, afternoon, and night shifts

- Custom template filter for displaying employee full names

- Custom 404 error page

- Reusable templates (base template, navbar, footer) with a consistent layout

## Technologies

- Python

- Django

- PostgreSQL

- HTML & CSS

- Git & GitHub for version control

## Setup Instructions
### 1. Clone the repository

```
git clone https://github.com/BobiOneKenobi/WorkSchedule.git
cd WorkSchedule
```
### 2. Create a virtual environment
Windows:
```
python -m venv .venv
```
Activate it:

 Windows:
```
.venv\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Configure PostgreSQL

Update the database settings in:
```
WorkSchedule/settings.py
```
Example configuration:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Make sure PostgreSQL is installed and running.

### 5. Apply migrations
```
python manage.py migrate
```
### 6. Create superuser
```
python manage.py createsuperuser
```
Access the admin panel at:
```
http://127.0.0.1:8000/admin/
```
### 7. Run the project
```
python manage.py runserver
```
Open in the browser:
```
http://127.0.0.1:8000/
```

## Project Structure

The project is organized into three main Django apps with clearly defined responsibilities:

### common
- Home page
- Custom 404 error page
- Custom template filters

### employees
- Department and Employee models
- Employee management (full CRUD functionality)

### scheduling
- Shift management (CRUD functionality with validation and automatic shift type assignment)
- Leave request management (with validation and admin-based approval workflow)
- Company holiday listing

## Main Pages

- Home page

- Employees:
  - List
  - Create
  - Detail
  - Edit
  - Delete

- Shifts:
  - List
  - Create
  - Detail
  - Edit
  - Delete

- Leave Requests:
  - List
  - Create

- Holidays:
  - List

- Filtered Shift Views:
  - Morning shifts
  - Afternoon shifts
  - Night shifts
## Purpose
- This project is developed as part of the Django Basics course at SoftUni.
## Notes

Departments are managed through the Django admin panel

The application is designed to run locally with PostgreSQL

You may need to adjust the database credentials according to your local PostgreSQL setup.
### Initial Data

After running the project, you can:

- Create a superuser and access the admin panel
- Add Departments, Skills, and Holidays through the admin interface
- Then use the application UI to create Employees, Shifts, and Leave Requests