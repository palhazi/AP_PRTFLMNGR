from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, abort
from flask_login import login_required, current_user
from .models import Note, User, Investment, InvestmentSnapshot, Asset
from . import db
import json
from datetime import datetime
from functools import wraps
from sqlalchemy.exc import IntegrityError
import yfinance as yf

# Létrehozzuk a views Blueprint-et.
views = Blueprint('views', __name__)


# Definiáljuk a főoldal útvonalát.
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note') 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  
            db.session.add(new_note)  
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


# Definiáljuk a feljegyzés törlésének útvonalát.
@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


# Definiáljuk az összes felhasználót megjelenítő útvonalat.
@views.route('/all-users', methods=['GET'])
@login_required
def all_users():
    users = User.query.all()
    return render_template("all_users.html", users=users, user=current_user)


# Definiáljuk a felhasználó szerkesztésének útvonalát.
@views.route('/edit-user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.email = request.form.get('email')
        user.first_name = request.form.get('firstName')
        user.second_name = request.form.get('secondName')
        db.session.commit()
        flash('User updated!', category='success')
        return redirect(url_for('views.all_users'))

    return render_template("edit_user.html", user=user)


# Definiáljuk a felhasználó törlésének útvonalát.
@views.route('/delete-user/<int:user_id>', methods=['GET'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    try:
        db.session.commit()
        flash('User deleted!', category='success')
    except IntegrityError:
        db.session.rollback()
        flash('Integrity error!', category='error')

    return redirect(url_for('views.all_users'))


# Definiáljuk a befektetés létrehozásának útvonalát.
@views.route('/create-investment', methods=['GET', 'POST'])
@login_required
def create_investment():
    users = User.query.all()
    user_investments = Investment.query.all()
    assets = Asset.query.all()
    if request.method == 'POST':
        
        user_id = request.form.get('user')
        asset_id = request.form.get('asset')
        asset = Asset.query.get(asset_id)

        purchase_date = request.form.get('purchaseDate')
        purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        purchase_price = request.form.get('purchasePrice')
        quantity = request.form.get('quantity')
        current_price = request.form.get('currentPrice')
        expected_interest_amount = request.form.get('expectedInterestAmount')

        new_investment = Investment(asset_id=asset.id, asset_name=asset.name, asset_type=asset.type, purchase_date=purchase_date, purchase_price=purchase_price, quantity=quantity, current_price=current_price, expected_interest_amount=expected_interest_amount, user_id=user_id)
        
        db.session.add(new_investment)
        db.session.commit()
        flash('Investment created!', category='success')
        return redirect(url_for('views.create_investment'))
    
    return render_template("create_investment.html", user_investments=user_investments, user=current_user, users=users, assets=assets)



# Definiáljuk a befektetés szerkesztésémek útvonalát.
@views.route('/edit-investment/<int:investment_id>', methods=['GET', 'POST'])
@login_required
def edit_investment(investment_id):
    investment = Investment.query.get_or_404(investment_id)
    users = User.query.all()
    assets = Asset.query.all()
    if request.method == 'POST':
    
        investment.asset_id = request.form.get('asset')
        
        purchase_date = request.form.get('purchaseDate')  
        purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        investment.purchase_date = purchase_date  
        
        investment.purchase_price = float(request.form.get('purchasePrice'))
        investment.quantity = float(request.form.get('quantity'))
        investment.current_price = float(request.form.get('currentPrice'))
        investment.expected_interest_amount = float(request.form.get('expectedInterestAmount'))
        
        user_id = request.form.get('user') 
        investment.user_id = user_id  

        db.session.commit()
        flash('Investment updated!', category='success')
        return redirect(url_for('views.create_investment'))

    # Itt adjuk át az assets változót a sablonnak
    return render_template('edit_investment.html', investment=investment, user=current_user, users=users, assets=assets)  


# Definiáljuk a befektetés törlésének útvonalát.
@views.route('/delete-investment/<int:investment_id>', methods=['GET'])
@login_required
def delete_investment(investment_id):
    investment = Investment.query.get_or_404(investment_id)
    if investment.user_id == current_user.id:
        db.session.delete(investment)
        db.session.commit()
        flash('Investment deleted!', category='success')
    return redirect(url_for('views.create_investment'))

# Definiáljuk a jelszó ellenőrző függvényt
def check_password(password):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            error = None
            if request.method == 'POST':
                provided_password = request.form.get('password')
                if provided_password == password:
                    return f(*args, **kwargs)
                error = "Incorrect password. Please try again."
            return render_template('password_protected.html', user=current_user, error=error)
        return decorated_function
    return decorator


# Definiáljuk az admin_dashboard útvonalát.
@views.route('/admin_dashboard', methods=['GET', 'POST'])
@login_required
@check_password('123456')  # Replace 'your_password_here' with the desired password
def admin_dashboard():
    if request.method == 'POST':
        users = User.query.filter_by(is_approved=False).all()
        return render_template("admin_dashboard.html", user=current_user, users=users)
    users = User.query.filter_by(is_approved=False).all()
    return render_template("password_protected.html", user=current_user, users=users)

# Definiáljuk a snapshot útvonalát.
@views.route('/create_snapshots', methods=['POST'])
def create_snapshots():
    investments = Investment.query.all()

    if investments:
        current_time = datetime.utcnow()

        # Új sorszám létrehozása
        max_snapshot_group_id = db.session.query(db.func.max(InvestmentSnapshot.snapshot_group_id)).scalar()
        if max_snapshot_group_id is None:
            new_snapshot_group_id = 1
        else:
            new_snapshot_group_id = max_snapshot_group_id + 1

        for investment in investments:
            snapshot = InvestmentSnapshot(
                investment_id=investment.id,
                snapshot_date=current_time,
                purchase_price=investment.purchase_price,
                quantity=investment.quantity,
                current_price=investment.current_price,
                expected_interest_amount=investment.expected_interest_amount,
                snapshot_group_id=new_snapshot_group_id  # Folytonos sorszám hozzáadása
            )
            db.session.add(snapshot)
        db.session.commit()
        return jsonify({"message": "Snapshots created successfully"}), 200
    else:
        return jsonify({"message": "No investments found"}), 404

# Definiáljuk a kalkulátor útvonalát és működését.
from flask import request

@views.route('/calculator', methods=['GET', 'POST'])
@login_required
def calculator():
    result = None
    if request.method == 'POST':
        num1 = float(request.form.get('num1', 0))
        num2 = float(request.form.get('num2', 0))
        operation = request.form.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "A nullával való osztás nem megengedett!"

    return render_template("calculator.html", user=current_user, result=result)

# Definiáljuk az útvonalat a részvényárak lekérdezéséhez és megjelenítéséhez.

@views.route('/stock', methods=['GET', 'POST'])
def stock():
    if request.method == 'POST':
        ticker = request.form['ticker']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        data = yf.download(ticker, start=start_date, end=end_date)
        return render_template('stock_data.html', data=data.to_html(), user=current_user)

    return render_template('stock_form.html', user=current_user)

# Definiáljuk az útvonalat az eszközök létrehozásához és megjelenítéséhez.

@views.route('/create-asset', methods=['GET', 'POST'])
@login_required
def create_asset():
    assets = Asset.query.all()

    if request.method == 'POST':
        name = request.form.get('name')
        long_name = request.form.get('long_name')
        type = request.form.get('type')
        
        interest_payment_date = request.form.get('interestPaymentDate')
        if interest_payment_date:
         interest_payment_date = datetime.strptime(interest_payment_date, "%Y-%m-%d")
        else:
         interest_payment_date = None  

        maturity_date = request.form.get('maturityDate')
        if maturity_date:
         maturity_date = datetime.strptime(maturity_date, "%Y-%m-%d")
        else:
         maturity_date = None  

        description = request.form.get('description')
        location = request.form.get('location')
        link = request.form.get('link')
        
        costs = request.form.get('costs')
        if costs:
         costs = float(costs)
        else:
         costs = None 

        new_asset = Asset(name=name,long_name=long_name,type=type, interest_payment_date=interest_payment_date, maturity_date=maturity_date, description=description, location=location, link=link, costs=costs)
        db.session.add(new_asset)
        db.session.commit()
        flash('Asset created!', category='success')
        return redirect(url_for('views.create_asset'))
    
    return render_template("create_asset.html", user=current_user, assets=assets)

# Definiáljuk az útvonalat az eszközök szerkesztéséhez.

@views.route('/edit-asset/<int:asset_id>', methods=['GET', 'POST'])
@login_required
def edit_asset(asset_id):
    asset = Asset.query.get_or_404(asset_id)

    if request.method == 'POST':
        asset.name = request.form.get('name')
        asset.long_name = request.form.get('long_name')
        asset.type = request.form.get('type')

        interest_payment_date = request.form.get('interestPaymentDate')
        if interest_payment_date:
            interest_payment_date = datetime.strptime(interest_payment_date, "%Y-%m-%d")
        else:
            interest_payment_date = None
        asset.interest_payment_date = interest_payment_date

        maturity_date = request.form.get('maturityDate')
        if maturity_date:
            maturity_date = datetime.strptime(maturity_date, "%Y-%m-%d")
        else:
            maturity_date = None
        asset.maturity_date = maturity_date

        asset.description = request.form.get('description')
        asset.location = request.form.get('location')
        asset.link = request.form.get('link')

        costs = request.form.get('costs')
        if costs:
            asset.costs = float(costs)
        else:
            asset.costs = None

        db.session.commit()
        flash('Asset updated!', category='success')
        return redirect(url_for('views.create_asset'))

    return render_template('edit_asset.html', asset=asset, user=current_user)

# Definiáljuk az útvonalat az eszközök törléséhez.

@views.route('/delete-asset/<int:asset_id>', methods=['GET', 'POST', 'DELETE'])
@login_required
def delete_asset(asset_id):
    asset = Asset.query.get_or_404(asset_id)
    db.session.delete(asset)
    try:
        db.session.commit()
        flash('Asset deleted!', category='success')
    except IntegrityError:
        db.session.rollback()
        flash('Integrity Error!', category='error')

    return redirect(url_for('views.create_asset'))
