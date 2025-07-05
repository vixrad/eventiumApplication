A Django-based web application for managing events and organizer profiles. Eventium is a lightweight event management platform where users can create and manage events, as well as build and update their organizer profiles. The app follows Django best practices with a clear structure, validations, and clean template rendering. It includes dynamic navigation, conditional rendering based on organizer status, and simple relational database logic using Django ORM.

## Features

- Create, view, edit, and delete events  
- Organizer profile management  
- Custom field validations and error messages  
- Dynamic navigation links based on profile state  
- Form handling using class- and function-based views  
- UI using HTML (Django Template Language) and CSS (Bootstrap)

## Models

### Organizer

- `company_name`: required, unique, 2–110 characters, alphanumeric + spaces and hyphens only  
- `phone_number`: required, unique, digits only, max 15 characters  
- `secret_key`: required, 4 unique digits  
- `website`: optional URL

### Event

- `slogan`: required, 2–120 characters  
- `location`: required, 2–120 characters  
- `start_time`: required datetime, defaults to now  
- `available_tickets`: required, integer ≥ 0  
- `key_features`: optional text  
- `banner_url`: optional URL  
- `organizer`: foreign key to Organizer (hidden in forms)

## Routes

- `/` – Index  
- `/events/` – Event list  
- `/events/create/` – Create event  
- `/events/<event_pk>/details/` – Event details  
- `/events/<event_pk>/edit/` – Edit event  
- `/events/<event_pk>/delete/` – Delete event  
- `/organizer/create/` – Create organizer  
- `/organizer/details/` – Organizer profile  
- `/organizer/edit/` – Edit organizer  
- `/organizer/delete/` – Delete organizer

## Setup

```bash
git clone https://github.com/vixrad/eventiumApplication.git
cd eventiumApplication
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver

eventiumApplication/
├── common/                  # Shared mixins, base views, and utilities
├── eventiumApplication/     # Django project settings and URLs
├── events/                  # Event model, forms, views, templates
├── organizers/              # Organizer model, views, forms, and validators
├── static/                  # CSS and image assets
├── templates/               # HTML templates (base, event, organizer)
├── manage.py                # Django entry point
└── db.sqlite3               # Local SQLite database (used for development)

## Possible extensions

- Add user authentication and support for multiple organizer accounts  
- Use PostgreSQL instead of SQLite for production  
- Integrate image/file uploads with Django’s media storage  
- Add filtering, sorting, and search functionality for events  
- Display ticket availability in real-time  
- Create an API with Django REST Framework  
- Connect to a React, Vue, or mobile frontend  
- Deploy on platforms like Heroku, Render, or with Docker  
