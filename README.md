# Django E-Commerce Backend with Cart

A simple E-Commerce Web Application built with Django.
Users can browse products, view product details, add items to a cart, update quantities, remove items, and complete a checkout process.

This project was built to practice **Django relational modeling, business logic, cart management, REST APIs, AJAX interactions, and deployment**.

---

## 🚀 Live Demo

Live Application:
https://django-ecommerce-cart.onrender.com

GitHub Repository:
https://github.com/selvakalusu003/django-ecommerce-cart

---

## ✨ Features

- Product listing page
- Product detail page
- Add products to cart
- Update cart item quantity
- Remove items from cart
- Checkout process
- Automatic order creation
- Stock management system
- Prevent purchasing out-of-stock products
- Django Admin panel for managing store data
- REST API for product data
- AJAX-based Add-to-Cart functionality
- Responsive UI using Bootstrap

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* HTML
* CSS
* Bootstrap
* JavaScript
* AJAX
* SQLite
* Git & GitHub
* Render (Deployment)

---

## 📂 Project Structure

```
django-ecommerce-cart
│
├── ecommerce
│   ├── ecommerce
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── store
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── admin.py
│   │   └── urls.py
│   │
│   ├── templates
│   │   └── store
│   │       ├── base.html
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       ├── cart.html
│   │       └── checkout.html
│   │
│   └── manage.py
│
├── requirements.txt
├── build.sh
└── Procfile
```

---

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/selvakalusu003/django-ecommerce-cart.git
```

Go to project folder

```
cd django-ecommerce-cart/ecommerce
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows:

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run migrations

```
python manage.py migrate
```

Create superuser

```
python manage.py createsuperuser
```

Run the server

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000
```

## ☁️ Deployment

This application is deployed on **Render**.

### Build Command

```
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

### Start Command

```
gunicorn ecommerce.wsgi
```

---

## 🧠 Challenges Faced

* Configuring relational models for products, carts, and orders
* Implementing cart logic and quantity updates
* Preventing negative stock values
* Implementing AJAX-based Add-to-Cart functionality
* Fixing deployment issues on Render
* Managing production database and static files

---

## 📚 What I Learned

* Django relational database modeling
* Implementing shopping cart logic
* Managing product stock and orders
* Using Django REST Framework for APIs
* Using AJAX with Django views
* Customizing Django admin panel
* Deploying Django applications on Render
* Git & GitHub workflow

---

## 🔮 Future Improvements

* User authentication system
* User-specific carts
* Order history for users
* Payment gateway integration
* Product search and filtering
* Pagination for product listings
* PostgreSQL database for production

---

## 👨‍💻 Author

Selva Kalusalingam R

GitHub:
https://github.com/selvakalusu003
