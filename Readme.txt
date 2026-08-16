=========================================================
Little Lemon Web Application
Back-End Developer Capstone Project
=========================================================

API PATHS TO TEST (base URL: http://127.0.0.1:8000)

1) Static HTML home page:
   GET  /restaurant/

2) Menu API:
   GET     /restaurant/menu/              List all menu items
   POST    /restaurant/menu/              Create a new menu item
   GET     /restaurant/menu/<id>/         Retrieve one item
   PUT     /restaurant/menu/<id>/         Update one item
   DELETE  /restaurant/menu/<id>/         Delete one item

3) Table Booking API (token required):
   GET     /restaurant/booking/tables/        List all bookings
   POST    /restaurant/booking/tables/        Create a booking
   PUT     /restaurant/booking/tables/<id>/   Update a booking
   DELETE  /restaurant/booking/tables/<id>/   Delete a booking

4) Registration and Authentication:
   POST  /auth/users/                   Register a new user
   POST  /auth/token/login/             Login and get a token
   POST  /restaurant/api-token-auth/    Get token with username and password
   POST  /auth/token/logout/            Logout

HOW TO TEST SECURED ENDPOINTS (Insomnia):
   1. POST /auth/users/  (username, password, re_password) to register a user
   2. POST /restaurant/api-token-auth/ with username and password
   3. Copy the returned token
   4. Add header: Authorization: Token <your_token>
   5. Send requests to /restaurant/booking/tables/

SETUP INSTRUCTIONS:
   1. pip install django djangorestframework djoser pymysql
   2. Start MySQL server and run: CREATE DATABASE littlelemon;
   3. Edit littlelemon/settings.py -> DATABASES -> set your MySQL password
   4. python manage.py migrate
   5. python manage.py runserver

UNIT TESTS:
   python manage.py test