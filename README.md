Book Management System

A Django-based Book Management System that allows users to manage libraries, books, authors, and categories. It supports user registration, login, borrowing and returning of books, real-time notifications for book availability, and penalties for overdue returns. The project is Dockerized for easy setup and deployment.
Table of Contents

    Features
    Tech Stack
    Installation
    Environment Variables
    Running Locally
    Docker Setup
    API Endpoints
    Contributing
    License

Features

    User Authentication: Users can register, log in, and recover their passwords.
    Library Management: Manage multiple libraries, books, authors, and categories.
    Book Borrowing and Returning: Users can borrow and return multiple books at once, with real-time availability updates.
    Real-time Notifications: Users are notified about book availability through WebSockets.
    Borrowing Limits: Users can borrow a limited number of books (configurable, e.g., 3 books at a time).
    Overdue Penalties: Automatic penalties for late book returns.
    Distance Calculation: Calculates distances between users and libraries.
    Email Notifications: Sends email confirmations and reminders to users.

Tech Stack

    Backend: Django 4.2+
    Database: PostgreSQL with PostGIS
    Real-time: Django Channels (WebSockets)
    Task Scheduling: Django-cron for scheduled jobs
    Containerization: Docker & Docker Compose
    Cache/Message Broker: Redis

Installation
Prerequisites

    Python 3.10+
    Docker & Docker Compose
    PostgreSQL with PostGIS
    Redis
