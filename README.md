<div align="center">

```
███████╗████████╗██╗   ██╗██████╗ ███████╗███╗   ██╗████████╗    ███╗   ███╗███████╗
██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝    ████╗ ████║██╔════╝
███████╗   ██║   ██║   ██║██║  ██║█████╗  ██╔██╗ ██║   ██║       ██╔████╔██║███████╗
╚════██║   ██║   ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║       ██║╚██╔╝██║╚════██║
███████║   ██║   ╚██████╔╝██████╔╝███████╗██║ ╚████║   ██║       ██║ ╚═╝ ██║███████║
╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝       ╚═╝     ╚═╝╚══════╝
```

# 🎓 Student Management System

### *A powerful, full-stack Django web application to manage student records with ease*

<br>

[![Django](https://img.shields.io/badge/Django-6.0.5-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![DRF](https://img.shields.io/badge/REST_Framework-3.17-ff1709?style=for-the-badge&logo=django&logoColor=white)](https://django-rest-framework.org)
[![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io)

[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![Pandas](https://img.shields.io/badge/Pandas-Excel_Export-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Pillow](https://img.shields.io/badge/Pillow-Image_Upload-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://pillow.readthedocs.io)

<br>

![GitHub last commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/MyDjango?style=flat-square&color=brightgreen)
![GitHub repo size](https://img.shields.io/github/repo-size/YOUR_USERNAME/MyDjango?style=flat-square&color=blue)
![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/MyDjango?style=flat-square&color=yellow)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)

<br>

[🚀 Live Demo](#) · [📖 Documentation](#-getting-started) · [🐛 Report Bug](../../issues) · [✨ Request Feature](../../issues)

</div>

---

## ✨ Features at a Glance

<div align="center">

| 🔐 Auth | 📋 CRUD | 🔍 Search | 📄 Pagination |
|:---:|:---:|:---:|:---:|
| Login required on all pages | Create · Read · Update · Delete | Search students by name | 5 records per page |

| 🖼️ Image Upload | 📊 Excel Export | 📧 Email | 🌐 REST API |
|:---:|:---:|:---:|:---:|
| Profile photo upload | Download `.xlsx` via Pandas | Django send_mail support | JSON API endpoint |

</div>

---

## 🛠️ Tech Stack

```
🧠 Backend         →   Django 6.0.5
🔌 API             →   Django REST Framework 3.17
🔑 Authentication  →   Django Auth + SimpleJWT
🗄️  Database        →   SQLite (swappable to PostgreSQL)
📊 Data Export     →   Pandas + OpenPyXL
🖼️  Image Handling  →   Pillow
🐍 Language        →   Python 3.13
```

---

## 📁 Project Structure

```
📦 MyDjango/
├── 📄 manage.py
├── 📄 requirements.txt
├── 🗄️  db.sqlite3
│
├── 📂 myDjangoApp/                  ← Project Configuration
│   ├── ⚙️  settings.py
│   ├── 🔗 urls.py
│   ├── 🚪 asgi.py
│   └── 🚪 wsgi.py
│
├── 📂 myapp/                        ← Main Application
│   ├── 🏗️  models.py               ← Student model
│   ├── 👁️  views.py                ← CRUD + API + Export
│   ├── 🔗 urls.py                  ← URL routing
│   ├── 📝 forms.py                 ← StudentForm
│   ├── 🔄 serializer.py            ← DRF Serializer
│   ├── 🛡️  admin.py                ← Admin config
│   ├── 📂 migrations/              ← DB migrations
│   └── 📂 templates/
│       ├── 🏠 index.html           ← Student list
│       ├── ➕ add.html             ← Add / Edit
│       └── 🔐 login.html          ← Login page
│
└── 📂 media/
    └── 📂 students/                ← Uploaded photos
```

---

## ⚡ Getting Started

### 📋 Prerequisites

> Make sure you have these installed before running the project.

- 🐍 **Python 3.10+**
- 📦 **pip**
- 🔧 **Git**

---

### 🔧 Installation

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/MyDjango.git
cd MyDjango
```

**2. Create and activate virtual environment**
```bash
# 🪟 Windows
python -m venv venv
venv\Scripts\activate

# 🐧 Linux / 🍎 macOS
python -m venv venv
source venv/bin/activate
```

**3. Install all dependencies**
```bash
pip install -r requirements.txt
```

**4. Apply database migrations**
```bash
python manage.py migrate
```

**5. Create a superuser (admin)**
```bash
python manage.py createsuperuser
```

**6. Run the development server** 🚀
```bash
python manage.py runserver
```

> 🌐 Open your browser and visit: **http://127.0.0.1:8000**

---

## 🔌 API Reference

### Base URL
```
http://127.0.0.1:8000/
```

### Endpoints

| Method | Endpoint | Description | Auth Required |
|:---:|:---|:---|:---:|
| `GET` | `/api/` | List all students as JSON | ❌ |
| `POST` | `/api/token/` | Get JWT access + refresh token | ✅ Credentials |
| `POST` | `/api/token/refresh/` | Refresh JWT access token | ✅ Refresh token |
| `GET` | `/` | Home — student list | 🔐 Login |
| `GET/POST` | `/add/` | Add a new student | 🔐 Login |
| `GET/POST` | `/update/<id>/` | Edit student record | 🔐 Login |
| `POST` | `/delete/<id>/` | Delete student record | 🔐 Login |

---

### 🔑 Get JWT Token

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "yourpassword"}'
```

**Response:**
```json
{
  "access":  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

### 📦 Students API Response

```json
[
  {
    "id": 1,
    "name": "Raj Patel",
    "email": "raj@example.com",
    "course": "Computer Science",
    "image": "/media/students/raj.jpg"
  }
]
```

---

## 🧩 Student Model

```python
class Student(models.Model):
    name   = models.CharField(max_length=100)       # 👤 Full name
    email  = models.EmailField()                     # 📧 Email address
    course = models.CharField(max_length=100)        # 📚 Course enrolled
    image  = models.ImageField(                      # 🖼️ Profile photo
                upload_to='students/',
                null=True, blank=True
             )
```

---

## 🔒 Environment Variables

> ⚠️ **Security tip:** Move sensitive settings to a `.env` file before deploying!

Create a `.env` file in your project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email settings
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

---

## 🤝 Contributing

Contributions are what make open source amazing! 💪

```
1. 🍴 Fork the project
2. 🌿 Create your branch    →  git checkout -b feature/AmazingFeature
3. 💾 Commit your changes   →  git commit -m "✨ Add AmazingFeature"
4. 📤 Push to the branch    →  git push origin feature/AmazingFeature
5. 🔁 Open a Pull Request
```

---

## 📄 License

Distributed under the **MIT License** — see [`LICENSE`](LICENSE) for details.

---

<div align="center">

## 👨‍💻 Author

**Made with ❤️ and ☕ in India 🇮🇳**

[![GitHub](https://img.shields.io/badge/GitHub-YOUR__USERNAME-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YOUR_USERNAME)

<br>

### ⭐ Star this repo if you found it helpful! ⭐

<br>

<sub>Built with 🐍 Python · 🎸 Django · 💚 Open Source</sub>

</div>
