# Leave Management System

## Project Description
The Leave Management System is a web application developed using Django and Django REST Framework. It allows users to manage employee records and leave applications efficiently. The project uses MySQL as the backend database.

## Features
- Employee Management
- Leave Application Management
- Create, View, Update and Delete Records (CRUD)
- REST API Support
- MySQL Database Integration

## Technologies Used
- Python
- Django
- Django REST Framework
- MySQL
- HTML
- CSS

## Installation

1. Clone the repository:
```bash
git clone https://github.com/prernaveer/LeaveManagement.git
```

2. Go to the project folder:
```bash
cd LeaveManagement
```

3. Create and activate a virtual environment:
```bash
python -m venv myvenv
myvenv\Scripts\activate
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

5. Configure the MySQL database in `settings.py`.

6. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Start the development server:
```bash
python manage.py runserver
```

## API Endpoints

- `/api/employees/`
- `/api/leaves/`

## Database
This project uses **MySQL** as the backend database.

## Author
**Prerna Veer**