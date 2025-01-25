from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite'
app.config['SECRET_KEY'] = 'Dmoneycode'
db = SQLAlchemy(app)

# Define restaurant model
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    cuisine = db.Column(db.String(80))
    description = db.Column(db.String(80))
    reviews = db.relationship('Review', backref='restaurant', lazy=True)


# Define review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)


# Define user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False, unique=True)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('That username is already taken.', 'error')
            return redirect(url_for('register'))
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Successfully registered your account', 'success')
        return redirect(url_for('login'))  # Redirect to login after registration
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the user and password are real and correct
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            flash('You have successfully logged in', 'success')
            return redirect(url_for('homepage'))  # Redirect to the homepage on success
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')  # Render login page for GET or failed login


# Route to display the homepage
@app.route('/homepage')
def homepage():
    restaurants = Restaurant.query.all()
    return render_template('homepage.html', restaurants=restaurants)


# Route to add a review to a restaurant
@app.route('/restaurant/<int:restaurant_id>/add_review', methods=['GET', 'POST'])
def add_review(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    if request.method == 'POST':
        content = request.form['content']
        rating = int(request.form['rating'])
        if rating < 1 or rating > 5:
            flash('Rating must be between 1 and 5.', 'error')
            return redirect(url_for('add_review', restaurant_id=restaurant_id))

        review = Review(content=content, rating=rating, restaurant_id=restaurant_id)
        db.session.add(review)
        db.session.commit()
        flash('Review added successfully!', 'success')
        return redirect(url_for('restaurant_details', restaurant_id=restaurant_id))

    return render_template('add_review.html', restaurant=restaurant)


# Route to view all reviews for a specific restaurant
@app.route('/reviews/<int:restaurant_id>')
def view_reviews(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    reviews = Review.query.filter_by(restaurant_id=restaurant_id).all()
    return render_template('reviews.html', restaurant=restaurant, reviews=reviews)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Populate restaurants if the database is empty
        if Restaurant.query.count() == 0:
            sample_restaurants = [
                Restaurant(name='Davids Pizza', cuisine='Italian', description='Flamboyant Pizza with the freshest ingredients'),
                Restaurant(name='William Baker Morrisons Bakes', cuisine='English', description='Baked Bread the British way'),
                Restaurant(name='Marian Empanadas', cuisine='Venezuelan', description='Made with Love'),
                Restaurant(name='Jayant Palace', cuisine='Indian', description='Hindi food for all'),
                Restaurant(name='Daniels Taqueria', cuisine='Mexican', description='The true taste of Mexico')
            ]
            db.session.bulk_save_objects(sample_restaurants)
            db.session.commit()
        app.run(debug=True)
