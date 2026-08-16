# 🍋 Little Lemon Web Application

**Back-End Developer Capstone Project – Meta Back-End Developer Professional Certificate**

A full back-end web application for the Little Lemon restaurant, built with **Django** and **Django REST Framework**. The app serves a static HTML home page, connects to a **MySQL** database, and exposes REST APIs for the menu and table bookings with **token-based authentication**, user registration via **Djoser**, and automated **unit tests**.

---

## 🛠️ Technologies Used

- Python 3.12
- Django 6.0
- Django REST Framework
- Djoser (registration & token authentication)
- PyMySQL (MySQL driver)
- MySQL 8

---

## 📦 Installation & Setup

```bash
# 1. Clone the repository
git clone <YOUR-REPO-URL>
cd little-lemon

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start MySQL server and create the database
mysql -u root -p
CREATE DATABASE littlelemon;

# 5. Set your MySQL password in littlelemon/settings.py (DATABASES section)

# 6. Apply migrations
python manage.py migrate

# 7. (Optional) Create a superuser
python manage.py createsuperuser

# 8. Run the development server
python manage.py runserver
```

---

## 🌐 API Paths to Test

Base URL: `http://127.0.0.1:8000`

### Static HTML Content
| Method | Endpoint | Description |
|---|---|---|
| GET | `/restaurant/` | Home page (static HTML + static assets) |

### Menu API
| Method | Endpoint | Description |
|---|---|---|
| GET | `/restaurant/menu/` | List all menu items |
| POST | `/restaurant/menu/` | Create a new menu item |
| GET | `/restaurant/menu/<id>/` | Retrieve a single item |
| PUT | `/restaurant/menu/<id>/` | Update an item |
| DELETE | `/restaurant/menu/<id>/` | Delete an item |

### Table Booking API (🔒 token required)
| Method | Endpoint | Description |
|---|---|---|
| GET | `/restaurant/booking/tables/` | List all bookings |
| POST | `/restaurant/booking/tables/` | Create a booking |
| PUT | `/restaurant/booking/tables/<id>/` | Update a booking |
| DELETE | `/restaurant/booking/tables/<id>/` | Delete a booking |

### Registration & Authentication
| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/users/` | Register a new user |
| POST | `/auth/token/login/` | Login and obtain a token |
| POST | `/restaurant/api-token-auth/` | Obtain a token (username + password) |
| POST | `/auth/token/logout/` | Logout (invalidate the token) |

---

## 🔐 How to Test Secured Endpoints (Insomnia)

1. Register a user — `POST /auth/users/`:
   ```json
   { "username": "reviewer", "password": "Review@123", "re_password": "Review@123" }
   ```
2. Obtain a token — `POST /restaurant/api-token-auth/`:
   ```json
   { "username": "reviewer", "password": "Review@123" }
   ```
3. Add this header to your requests:
   ```text
   Authorization: Token <your_token>
   ```
4. Send requests to `/restaurant/booking/tables/`.

---

## 🧪 Running the Unit Tests

```bash
python manage.py test
```

- `restaurant/tests/test_models.py` – Menu model string representation
- `restaurant/tests/test_views.py` – Menu API GET endpoint

---

## 📁 Project Structure

```text
little-lemon/
├── manage.py
├── Readme.txt               # API paths for peer review (assignment requirement)
├── README.md                # This file
├── requirements.txt
├── templates/
│   └── index.html
├── littlelemon/
│   ├── settings.py
│   └── urls.py
└── restaurant/
    ├── models.py            # Menu & Booking models
    ├── serializers.py       # MenuSerializer & BookingSerializer
    ├── views.py             # API views + BookingViewSet
    ├── urls.py              # App routes + token endpoint
    ├── admin.py
    └── tests/
        ├── test_models.py
        └── test_views.py
```

---

## ✅ Grading Checklist

- [x] Django serves static HTML content
- [x] Project committed to a Git repository
- [x] Backend connected to a MySQL database
- [x] Menu and table booking APIs implemented (GET / POST / PUT / DELETE)
- [x] User registration and token authentication
- [x] Unit tests included and passing
- [x] API testable with the Insomnia REST client

---

*Author: AMIN – Meta Back-End Developer Capstone*