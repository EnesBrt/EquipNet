# EquipNet - Configuration Management Database

EquipNet is a comprehensive Configuration Management Database (CMDB) system built with Django. It helps organizations track, manage, and maintain their IT equipment inventory and configuration items.

## Features

- Equipment tracking and management
- User authentication and authorization
- Dashboard with equipment statistics
- Detailed equipment information and history

## Technology Stack

- Python
- Django
- PostgreSQL
- HTML/CSS
- Bulma for styling

## Installation

1. Clone the repository
```bash
git clone https://github.com/EnesBrt/EquipNet.git
cd EquipNet
```

2. Create and activate a virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure the database in settings.py

5. Run migrations
```bash
python manage.py migrate
```

6. Create a superuser
```bash
python manage.py createsuperuser
```

7. Run the development server
```bash
python manage.py runserver
```

## License

This project is licensed under the MIT License. 
