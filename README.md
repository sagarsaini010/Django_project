# Online Test System (OTS)

A responsive web-based test platform developed using Django and SQLite. This system allows admins to create tests and users to take them in a secure, dynamic environment.

## Features

- User registration and authentication with Django's built-in system
- Admin dashboard for managing tests and questions
- Dynamic rendering of multiple-choice quizzes
- Real-time evaluation and score display
- Responsive UI 
- Secure session and data handling through Django ORM

## Tech Stack

- Frontend: HTML5, CSS3, 
- Backend: Django (Python)
- Database: SQLite

## Project Structure

ots_project/ ├── ots_app/ │   ├── migrations/ │   ├── templates/ │   ├── static/ │   ├── admin.py │   ├── models.py │   ├── views.py │   ├── urls.py ├── ots_project/ │   ├── settings.py │   ├── urls.py ├── db.sqlite3 └── manage.py


## Screenshots

### Registration Page  
_Users sign up and log in securely using Django auth._

<img width="1919" height="1079" alt="Screenshot 2025-08-05 162541" src="https://github.com/user-attachments/assets/428bd8a7-82c5-457b-9948-c1bd7d22055e" />


### Quiz Interface  
_Users answer timed multiple-choice questions._

<img width="1919" height="1077" alt="Screenshot 2025-08-05 162658" src="https://github.com/user-attachments/assets/1b960712-7f53-47b4-bcd7-bcf652200a33" />


### Result Summary  
_Immediate scoring and feedback after quiz completion._

<img width="1919" height="1079" alt="Screenshot 2025-08-05 162730" src="https://github.com/user-attachments/assets/0965bf7e-c7dc-42b4-ba87-d889e33416ed" />


## Installation

1. Clone the repo  
   `git clone https://github.com/sagarsaino010/Django-project.git`

2. Navigate to the project directory  
   `cd Django-project`

3. Install dependencies  
   `pip install -r requirements.txt`

4. Apply migrations  
   `python manage.py migrate`

5. Run server  
   `python manage.py runserver`

## Author

Developed by [Sagar](https://github.com/sagarsaini010)
