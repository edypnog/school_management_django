# School Management System

The School Management System is a web application built with Django that allows users to manage students and courses for a school or educational institution. 
It provides a user-friendly interface to perform various CRUD (Create, Read, Update, Delete) operations on student and course data.

## Features

- Add, view, edit, and delete students with their details such as name, age, and other relevant information.
- Add, view, edit, and delete courses with their title, description, and other related data.
- Easily manage student enrollment in courses.
- User-friendly admin interface to manage students and courses efficiently.

## Requirements

- Python 3.x
- Django 4.x

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/edypnog/school_management_django.git
cd school_management_api
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # For Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations to set up the database:

```bash
python manage.py migrate
```

5. Create a superuser to access the admin interface:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Access the application in your web browser:

Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage

- Sign in to the admin interface using the credentials of the superuser you created during installation.
- Use the admin dashboard to manage students and courses by adding, editing, or deleting records.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue.

## Acknowledgments

Special thanks to the Django community and contributors for the amazing tools and resources that made this project possible.

---
