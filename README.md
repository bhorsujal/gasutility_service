# Gas Utility Service Portal

A Django-based web application for managing gas service requests with role-based access.

## Features
* Customer service request submission and tracking
* **MULTIPLE File attachments support**
* Role-based dashboard and navigation
* Secure authentication
* Basic HTML pages for ease of usage

## Installation
1. Clone the repository
   ```bash
   git clone https://github.com/bhorsujal/gasutility_service.git
   cd gasutility_service
   ```

2. Set up virtual environment
   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. Install dependencies and run migrations
   ```bash
   pip install django
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser # for admin panel access at http://localhost:8000/admin
   ```

4. Run the server
   ```bash
   python manage.py runserver
   ```

## User Guide

### For Customers
1. **Register**: Create account at `/accounts/register/`
2. **Login**: Use credentials at `/accounts/login/`
3. **Create Request**: 
   * Navigate to `/requests/new/`
   * Select service type
   * Add description
   * Optional file upload **(*Multiple file uploads supported*)**
4. **Track Requests**: View all requests at `/requests/`
5. **Logout**: Use logout button in navigation bar

### For Support/Admin Users
1. **Login**: Use admin/support credentials
2. **Dashboard**: Automatically redirected to `/support/`
3. **Manage Requests**: 
   * View details
   * Update request status
   * Review attachments
4. **Logout**: Use logout button in navigation bar
