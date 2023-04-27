from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   # Az __init__.py modulból importáljuk a db változót.
from flask_login import login_user, login_required, logout_user, current_user

# Létrehozzuk az 'auth' Blueprint-ot.
auth = Blueprint('auth', __name__)


# Definiáljuk a bejelentkezési útvonalat és a hozzá tartozó függvényt.
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # Ellenőrizzük, hogy létezik-e már ilyen email című felhasználó.
        user = User.query.filter_by(email=email).first()
        if user:
            # Ha a jelszó helyes és a felhasználó jóvá van hagyva, akkor bejelentkeztetjük a felhasználót.
            if check_password_hash(user.password, password) and user.is_approved:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            elif not user.is_approved:
                flash('Your account is not approved yet. Please wait for approval.', category='error')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


# Definiáljuk a kijelentkezési útvonalat és a hozzá tartozó függvényt.
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Definiáljuk a regisztrációs útvonalat és a hozzá tartozó függvényt.
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        second_name = request.form.get('secondName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(second_name) < 2:
            flash('Second name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, second_name=second_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created! Please wait for admin approval before logging in.', category='success')
            return redirect(url_for('auth.login'))

    return render_template("sign_up.html", user=current_user)


# Regsiztráció jóváhagyása
@auth.route('/approve_user/<int:user_id>', methods=['POST'])
@login_required
def approve_user(user_id):
    user = User.query.get(user_id)

    if user and not user.is_approved:
        user.is_approved = True
        db.session.commit()
        flash(f'User {user.email} has been approved.', category='success')

    return redirect(url_for('views.admin_dashboard'))
