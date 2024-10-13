# Book Management System

A **Django-based Book Management System** that allows users to manage libraries, books, authors, and categories. The system supports user registration, borrowing, returning books, real-time notifications for book availability, and enforcement of overdue penalties. The project is containerized with Docker for easy deployment and setup.

## Features

- **User Authentication**: Registration, login.
- **Library Management**: Add and manage libraries, books, authors, and categories.
- **Book Borrowing/Returning**: Borrow and return multiple books with real-time availability updates.
- **Real-time Notifications**: Receive real-time updates on book availability via WebSockets (Django Channels).
- **Penalties**: Automatically applies penalties for overdue book returns.
- **Distance Calculation**: Calculate the distance between users and libraries.
- **Email Notifications**: Send confirmation emails and reminders for overdue returns.

## Technology Stack

- **Backend**: Django 4.2+
- **Database**: PostgreSQL with PostGIS for geographic functionality
- **Real-time**: Django Channels (WebSockets)
- **Containerization**: Docker and Docker Compose

## Installation

### Prerequisites

- Python 3.10+
- Docker & Docker Compose
- PostgreSQL with PostGIS extension
- Redis

### Steps to Set Up Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/book-management-system.git
   cd book-management-system
🐳 Docker Setup

To run the application in a containerized environment:

    Build and start Docker containers:

    bash

docker-compose up --build

Run migrations inside the container:

bash

docker-compose exec django python manage.py migrate

Collect static files:

bash

docker-compose exec django python manage.py collectstatic --noinput

Access the application: The app will be available at http://localhost:8000.
