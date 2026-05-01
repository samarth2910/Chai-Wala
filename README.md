# ☕ ChaiWala — Full Stack Tea Store

A full stack e-commerce web application for browsing and ordering premium Indian teas online.

---

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django 5.2 |
| REST API | Django REST Framework |
| Frontend | HTML, Tailwind CSS, Shoelace UI |
| JavaScript | Vanilla JS + React 18 (CDN) |
| Database | SQLite |
| Auth | Django built-in authentication |

---

## ✅ Features

- 🏠 Home page with auto-playing image carousel
- 🍵 Browse all teas with product detail pages
- 🛒 Session-based shopping cart with add, remove, and quantity controls
- 🔐 User authentication — Login, Signup, Logout
- 📦 Order placement tied to logged-in user
- ⚛️ Orders page built in React — fetches data from Django REST API
- 📱 Fully responsive design

---

## ⚛️ React + REST API

The Orders page is built entirely in React. Django serves an empty HTML page and React:
- Fetches order data from the DRF API using `useEffect` + `fetch()`
- Stores the response in `useState`
- Renders `OrderCard` and `OrderItem` components dynamically

**API Endpoints:**

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| GET | `/chai/api/products/` | All teas as JSON | No |
| GET | `/chai/api/orders/` | Logged-in user's orders as JSON | Yes |

---

## 📁 Project Structure

```
Tea-Store/
├── DjangoProject/         ← Main Django project
│   ├── settings.py
│   ├── urls.py
│   └── views.py
│
├── Chai/                  ← Main app
│   ├── models.py          ← Chai, Order, OrderItem
│   ├── views.py           ← All views + DRF API views
│   ├── urls.py            ← All URL routes
│   ├── serializers.py     ← DRF serializers
│   └── templates/Chai/
│       ├── chai_home.html
│       ├── all_chai.html
│       ├── chai_detail.html
│       ├── cart.html
│       ├── react_orders.html  ← React app
│       ├── login.html
│       └── signup.html
│
└── templates/
    └── layout.html        ← Base template with navbar
```

---

## ⚙️ Setup & Run

```bash
# 1. Clone the repository
git clone https://github.com/samarth2910/Chai-Wala.git
cd chaiwala

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install django djangorestframework pillow django-browser-reload

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser (for admin panel)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

---

## 👤 Author

**Samarth Shetty**  
GitHub: [github.com/samarth2910](https://github.com/samarth2910)
