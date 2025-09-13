<<<<<<< HEAD
🛒 Shop - Django E-commerce Project
Shop is a simple and functional e-commerce platform built with Django. It includes features like product listing, shopping cart, and order management. The project also provides an admin panel for managing products and orders efficiently.

✨ Key Features
User authentication (login/register).
Product management with categories and images.
Shopping cart and checkout system.
Responsive design using Bootstrap.
=======
# Django E-commerce Project

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://example.com) [![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE) \[![Version](https://img.shields.io/badge/version-1.0.0-lightgrey)]

A simple **Django-based e-commerce web application** with frontend templates and backend logic. It allows users to browse products, view product details, add items to a shopping cart, and complete checkout with their information. Includes user authentication (register, login, logout) and an admin dashboard for managing products and orders.

---

## Table of Contents

* [About](#about)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Getting Started](#getting-started)

  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Environment Variables](#environment-variables)
  * [Running Locally](#running-locally)
* [Usage](#usage)
* [Templates (Frontend)](#templates-frontend)
* [URL Routes](#url-routes)
* [File Structure](#file-structure)
* [Testing](#testing)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)

---

## About

This project is a **basic online shopping system** built with Django 5.1.3. It demonstrates how to integrate authentication, shopping cart functionality, order handling, and HTML templates into a single cohesive e-commerce application.

---

## Features

* **User Authentication**: Register, login, logout
* **Product Management**: Name, description, price, image, creation date
* **Shopping Cart**: Add, view, and remove products
* **Checkout**: Place orders with full name, address, phone, and notes
* **Admin Panel**: Manage products, users, and orders
* **Frontend Templates**: Responsive HTML pages styled with Bootstrap
* **Media Support**: Product images stored in `/media/`

---

## Tech Stack

* **Framework:** Django 5.1.3
* **Language:** Python 3.11+
* **Database:** SQLite (default, configured in `settings.py`)
* **Frontend:** Django Templates (HTML, CSS, Bootstrap)
* **Other:** Django Authentication, Django Forms

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

* Python >= 3.11
* pip (Python package manager)
* Git

### Installation

```bash
# clone repository
git clone https://github.com/<your-org>/<repo>.git
cd <repo>

# create virtual environment
python -m venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate      # on Windows

# install dependencies
pip install -r requirements.txt

# run migrations
python manage.py migrate

# create superuser for admin panel
python manage.py createsuperuser
```

### Environment Variables

The project uses **SQLite** by default and doesn’t require environment variables for setup. However, for production you should define:

| Variable        | Example Value                       | Description                                    |
| --------------- | ----------------------------------- | ---------------------------------------------- |
| `SECRET_KEY`    | `super-secret`                      | Django secret key (change for production)      |
| `DEBUG`         | `True`                              | Debug mode flag (set to `False` in production) |
| `ALLOWED_HOSTS` | `example.com, localhost, 127.0.0.1` | Allowed domains/IPs                            |

### Running Locally

```bash
python manage.py runserver
```

The app will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Usage

* `/home/` — View all products
* `/product/<id>/` — Product details
* `/add-to-cart/<id>/` — Add product to cart
* `/cart/` — View cart
* `/remove-from-cart/<id>/` — Remove item from cart
* `/checkout/` — Place an order
* `/login/` — Login
* `/register/` — Register
* `/logout/` — Logout

---

## Templates (Frontend)

The application includes several **Django templates** for frontend pages:

* `base.html` — Base template with navbar/footer
* `home.html` — Product listing page
* `product_detail.html` — Individual product page
* `cart_view.html` — Shopping cart page
* `checkout.html` — Checkout page with order form
* `login.html` — Login form
* `register.html` — User registration form

---

## URL Routes

Defined in `shop/urls.py` and `project/urls.py`:

| Path                      | View               | Description           |
| ------------------------- | ------------------ | --------------------- |
| `/home/`                  | `home_view`        | Show all products     |
| `/product/<id>/`          | `product_detail`   | Product details       |
| `/add-to-cart/<id>/`      | `add_to_cart`      | Add product to cart   |
| `/cart/`                  | `cart_view`        | View shopping cart    |
| `/remove-from-cart/<id>/` | `remove_from_cart` | Remove item from cart |
| `/checkout/`              | `checkout`         | Place an order        |
| `/login/`                 | `login_view`       | Login user            |
| `/register/`              | `register_view`    | Register new user     |
| `/logout/`                | `logout_view`      | Logout user           |

---

## File Structure

```
/ (project root)
├─ project/            # Django project config
│  ├─ settings.py      # Project settings
│  ├─ urls.py          # Global routes
│  ├─ wsgi.py
├─ shop/               # Main app
│  ├─ models.py        # Product, CartItem, Order models
│  ├─ forms.py         # OrderForm
│  ├─ views.py         # Views for products, cart, checkout, auth
│  ├─ urls.py          # Shop routes
├─ templates/          # Frontend HTML templates
│  ├─ base.html
│  ├─ home.html
│  ├─ product_detail.html
│  ├─ cart_view.html
│  ├─ checkout.html
│  ├─ login.html
│  ├─ register.html
├─ static/             # CSS/JS/Images
├─ media/              # Uploaded product images
├─ manage.py
├─ requirements.txt

```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repo
2. Create a new branch (`git checkout -b feature/awesome`)
3. Commit changes (`git commit -m "Add awesome feature"`)
4. Push to branch (`git push origin feature/awesome`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## Authors

* **arash** — *Initial Work* — [arashey](https://github.com/arashey)

>>>>>>> 4757732 (added requirements.txt and README.md)
