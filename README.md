# Restaurant Reviews App

This is a Flask-based web application that allows users to browse restaurants, read reviews,
and write their own reviews. It includes user authentication to ensure only registered users can submit reviews.

---

## Features

- **Browse Restaurants:** View a list of restaurants with their cuisine and description.
- **Read Reviews:** Access detailed reviews for each restaurant.
- **Write Reviews:** Authenticated users can submit reviews with a rating and comments.
- **User Authentication:** Register and log in securely to access certain features.
- **Dynamic Routing:** Seamlessly navigate between restaurants and their respective reviews.

---

## Installation

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.7+
- Flask and its dependencies
- SQLite (used as the database backend)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd restaurant-reviews

2. Required dependencies:
   ```bash
   pip install -r requirements.txt

3. Initialize the database
   ```bash
   flask shell
   from app import db
   db.create_all()

4. run the app
   ```bash
    flask run
Access the app in your prefered browser at http://127.0.0.1:5000.

6. Project structure:
   ```bash
   restaurant-reviews/
   │
   ├── app.py                  # Main Flask application
   ├── templates/              # HTML templates for rendering views
   │   ├── homepage.html       # Homepage displaying restaurants
   │   ├── add_review.html     # Page for submitting new reviews
   │   ├── reviews.html        # Page for displaying reviews
   │   ├── login.html          # Login page
   │   └── register.html       # Registration page
   ├── static/                 # Static files (e.g., CSS, JS, images)
   ├── requirements.txt        # List of required Python libraries
   └── README.md               # Project documentation


Overview of the routes:

/register	User registration page

/login	User login page

/homepage	List of restaurants

/restaurant/<int:restaurant_id>	Details and reviews for a restaurant

/restaurant/<int:restaurant_id>/add_review	Add a review for a restaurant

/reviews/<int:restaurant_id>	View all reviews for a restaurant



Database Models

Restaurant

id: Unique identifier for the restaurant.

name: Name of the restaurant.

cuisine: Type of cuisine.

description: Short description of the restaurant.

reviews: Relationship to Review model.

Review

id: Unique identifier for the review.

content: Review content.

rating: Rating (1-5).

restaurant_id: Foreign key linking to a restaurant.

User

id: Unique identifier for the user.

username: User's unique username.

password: User's hashed password.


The app depends on the following Python libraries:

Flask

Flask-SQLAlchemy

Flask-Login

Install all dependencies using:

pip install -r requirements.txt




