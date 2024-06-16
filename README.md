
# eCommerce Website

An eCommerce web application built with Django that offers a seamless online shopping experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication:** Secure login and registration system.
- **Product Management:** Browse and search for products with detailed descriptions.
- **Shopping Cart:** Add, update, and remove items from the cart.
- **Coupon System:** Apply discount coupons to orders.
- **Order Management:** Track order history and status.
- **Payment Integration:** Secure payment processing with popular payment gateways.
- **Responsive Design:** User-friendly interface on both desktop and mobile devices.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/ecommerce-website.git
   cd ecommerce-website
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```sh
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

7. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

- **User Authentication:** Register a new account or login with an existing one.
- **Browse Products:** Search and browse through the available products.
- **Shopping Cart:** Add products to your cart, update quantities, or remove items.
- **Apply Coupons:** Enter discount codes at checkout to receive discounts.
- **Place Orders:** Complete the purchase using integrated payment gateways.
- **Track Orders:** View your order history and track the status of your current orders.

## Technologies Used

- **Django:** Web framework for the backend.
- **HTML/CSS:** For the frontend structure and styling.
- **JavaScript:** For interactive features.
- **Bootstrap:** Responsive design framework.
- **SQLite/PostgreSQL:** Database for storing data.
- **Stripe/PayPal API:** Payment gateway integration.

