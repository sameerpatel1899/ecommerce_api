# 🛒 E-Commerce API using Django (No Auth / No Payment)

This is a basic E-Commerce REST API built with **Django** and **Django REST Framework**, supporting the product booking process *till before payment*. No authentication or payment logic is included.

---

## 🚀 Features

✅ Product listing  
✅ Add to cart / view cart / update cart / remove item  
✅ Shipping address submission  
✅ Create order  
✅ Swagger docs for testing APIs

---

## 📦 Tech Stack

- Python 3.13
- Django 4.x
- Django REST Framework
- SQLite (for local dev)
- Swagger (drf-yasg)
- Waitress (Windows WSGI server)
- Nginx (optional for production)

---

## 📁 Folder Structure

ecommerce_api/
│
├── config/ # Django settings, urls, WSGI
├── products/ # Product-related APIs
├── cart/ # Cart handling APIs
├── orders/ # Order-related logic
├── shipping/ # Shipping info API
│
├── manage.py
├── db.sqlite3
└── README.md # ← You're reading this!

yaml
Copy
Edit

---

## 📑 API Endpoints Summary

| Method | Endpoint                  | Description                     |
|--------|---------------------------|---------------------------------|
| GET    | `/products/`              | List all products               |
| POST   | `/products/`              | Add a new product               |
| GET    | `/products/{id}/`         | Get product details             |
| GET    | `/cart/`                  | View cart items                 |
| POST   | `/cart/add/`              | Add item to cart                |
| PUT    | `/cart/update/{id}/`      | Update cart item quantity       |
| DELETE | `/cart/remove/{id}/`      | Remove item from cart           |
| POST   | `/shipping/`              | Submit shipping info            |
| POST   | `/orders/create/`         | Create order from cart items    |
| GET    | `/orders/{id}/`           | View order details              |

---

## 🧪 API Testing (Swagger UI)

Run the Django server:
```bash
python manage.py runserver
Visit:

arduino
Copy
Edit
http://127.0.0.1:8000/swagger/
You can test all endpoints directly from Swagger interface.

🖥️ Run with Waitress (Windows)
bash
Copy
Edit
pip install waitress
waitress-serve --port=8000 config.wsgi:application
🌐 Optional: Setup with Nginx (Advanced)
You can also reverse-proxy this API via Nginx for production deployment. (See full guide in docs or ask.)

🙌 Author
Sameer Patel
GitHub: @sameerpatel1899
Email: sameerpatelgo@gmail.com
