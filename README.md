<div align="center">

# 🎓 Student Management System

### A full-featured Django web application for managing student records

![Django](https://img.shields.io/badge/Django-6.0.5-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.17-ff1709?style=for-the-badge&logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

</div>

---

## 📌 About The Project

**MyDjango** is a clean and powerful **Student Management System** built with Django. It allows authenticated users to manage student records — add, view, update, delete, and even export data to Excel. The app also exposes a REST API secured with JWT tokens, making it ready for integration with any frontend or mobile client.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **Login Required** | All pages protected with Django's `@login_required` |
| 📋 **Student CRUD** | Create, Read, Update, Delete student records |
| 🔍 **Search** | Live search students by name |
| 📄 **Pagination** | 5 students per page |
| 🖼️ **Image Upload** | Upload student profile photos |
| 📊 **Excel Export** | Download all student data as `.xlsx` using Pandas |
| 📧 **Email Support** | Send test emails via Django's `send_mail` |
| 🌐 **REST API** | JSON API endpoint to list all students |
| 🔑 **JWT Auth** | Token obtain & refresh via `djangorestframework-simplejwt` |

---

## 🗂️ Project Structure

```
MyDjango/
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── myDjangoApp/               # Project config
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── myapp/                     # Main application
│   ├── models.py              # Student model
│   ├── views.py               # All views (CRUD + API + Export)
│   ├── urls.py                # URL routing
│   ├── forms.py               # StudentForm
│   ├── serializer.py          # DRF Serializer
│   ├── admin.py               # Admin panel config
│   ├── migrations/            # DB migrations
│   └── templates/
│       ├── index.html         # Student list
│       ├── add.html           # Add / Edit form
│       └── login.html         # Login page
│
└── media/
    └── students/              # Uploaded student images
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/MyDjango.git
cd MyDjango

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (for admin & login)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Then open 👉 **http://127.0.0.1:8000** in your browser.

---

## 🔌 API Endpoints

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `GET` | `/api/` | List all students (JSON) | None |
| `POST` | `/api/token/` | Get JWT access & refresh token | Credentials |
| `POST` | `/api/token/refresh/` | Refresh JWT access token | Refresh token |

### Example: Get JWT Token
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "yourpassword"}'
```

---

## 📦 Tech Stack

- **Backend:** Django 6.0, Django REST Framework
- **Auth:** Django Auth + SimpleJWT
- **Database:** SQLite (easily switchable to PostgreSQL)
- **Data Processing:** Pandas, OpenPyXL
- **File Handling:** Pillow (image uploads)

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
Made with ❤️ using Django
</div>
