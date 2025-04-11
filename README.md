# Art Gallery Management System

A comprehensive web application for managing an art gallery, including artwork sales, event management, auctions, and delivery services.

## Overview

The Art Gallery Management System is a Django-based web application designed to facilitate the operations of an art gallery. It provides a platform for artists to showcase their artwork, users to browse and purchase art, administrators to manage the gallery operations, and delivery personnel to handle the logistics of artwork delivery.

## Features

### User Management
- **Multiple User Roles**:
  - **Admin**: Manages the entire system, including users, artists, events, and categories
  - **User**: Browses artwork, books events, purchases artwork, and provides feedback
  - **Artist**: Uploads and manages artwork, participates in events, and conducts auctions
  - **Delivery Boy**: Manages the delivery of purchased artwork

### Artwork Management
- Artists can upload and manage their artwork
- Artwork categorization by type
- Detailed artwork descriptions and pricing
- Artwork status tracking (available, sold, etc.)

### Event Management
- Create and manage art events
- Event ticket booking system
- Seat allocation for events
- Event status tracking

### Auction System
- Artists can put artwork up for auction
- Time-based auction system
- Bidding functionality
- Auction completion and winner determination

### Booking and Purchasing
- Users can book/purchase artwork
- Booking status tracking
- Delivery assignment and tracking

### Communication
- Complaint management system
- Feedback system
- Chat functionality between users and artists

### Location Management
- District and place management
- Location-based delivery assignment

## Technology Stack

### Core Technologies
- **Backend**: Django 5.1.3+
- **Database**: SQLite (default), supports MySQL/PostgreSQL
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5

### Key Dependencies
```plaintext
# Core Requirements
Django>=5.1.3
Pillow>=10.1.0          # For image handling
python-dotenv>=1.0.0    # Environment variables

# Forms and UI
django-crispy-forms>=2.1
django-widget-tweaks>=1.5.0

# Database (Optional - based on choice)
mysqlclient>=2.2.1      # For MySQL
psycopg2-binary>=2.9.9  # For PostgreSQL

# Development Tools
django-debug-toolbar>=4.2.0

# Production
gunicorn>=21.2.0        # Production server
whitenoise>=6.6.0       # Static file handling
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv MainEnv
   source MainEnv/bin/activate  # On Windows: MainEnv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create environment variables file (.env):
   ```plaintext
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://127.0.0.1:8000/`

## Development Setup

For development, additional packages can be installed:
```bash
pip install -r requirements-dev.txt
```

This includes:
- django-debug-toolbar
- coverage (for testing)
- flake8 (for linting)

## Project Structure

The project is organized into several Django apps:

- **Mainproject**: The main Django project configuration
- **Admin**: Handles administrative functions and system management
- **Guest**: Manages public-facing pages and user registration
- **User**: Handles user-specific functionality
- **Artist**: Manages artist-specific functionality
- **DeliveryBoy**: Handles delivery management

## User Workflows

### User Registration and Login
1. Users can register as regular users, artists, or delivery personnel
2. Each user type provides specific information during registration
3. Login system with role-based redirection

### Artwork Management
1. Artists upload artwork with details and pricing
2. Admins approve artwork
3. Users browse and purchase artwork
4. Delivery personnel handle artwork delivery

### Event Management
1. Admins create events with details, capacity, and pricing
2. Users book event tickets
3. Artists participate in events

### Auction System
1. Artists put artwork up for auction
2. Users place bids
3. System determines winners based on highest bid
4. Payment and delivery process follows

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Bootstrap templates from [HTML Codex](https://htmlcodex.com/)
- Various JavaScript libraries and plugins used in the project

