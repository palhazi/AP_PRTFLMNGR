from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, User, Investment, InvestmentSnapshot
from . import db
import json
from datetime import datetime

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
    db.session.commit()
    flash('User deleted!', category='success')
    return redirect(url_for('views.all_users'))


# Definiáljuk a befektetés létrehozásának útvonalát.
@views.route('/create-investment', methods=['GET', 'POST'])
@login_required
def create_investment():
    users = User.query.all()
    user_investments = Investment.query.all()
    if request.method == 'POST':
        
        user_id = request.form.get('user')

        asset_name = request.form.get('assetName')
        asset_type = request.form.get('assetType')
        purchase_date = request.form.get('purchaseDate')
        purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        purchase_price = request.form.get('purchasePrice')
        quantity = request.form.get('quantity')
        current_price = request.form.get('currentPrice')
        expected_interest_amount = request.form.get('expectedInterestAmount')
        interest_payment_date = request.form.get('interestPaymentDate')
        interest_payment_date = datetime.strptime(interest_payment_date, "%Y-%m-%d")
        maturity_date = request.form.get('maturityDate')
        maturity_date = datetime.strptime(maturity_date, "%Y-%m-%d")

        new_investment = Investment(asset_name=asset_name, asset_type=asset_type, purchase_date=purchase_date, purchase_price=purchase_price, quantity=quantity, current_price=current_price, expected_interest_amount=expected_interest_amount, interest_payment_date=interest_payment_date, maturity_date=maturity_date, user_id=user_id)
        db.session.add(new_investment)
        db.session.commit()
        flash('Investment created!', category='success')
        return redirect(url_for('views.create_investment'))
    
    return render_template("create_investment.html", user_investments=user_investments, user=current_user, users=users)



# Definiáljuk a befektetés szerkesztésémek útvonalát.
@views.route('/edit-investment/<int:investment_id>', methods=['GET', 'POST'])
@login_required
def edit_investment(investment_id):
    investment = Investment.query.get_or_404(investment_id)
    users = User.query.all()  
    if request.method == 'POST':
    
        investment.asset_name = request.form.get('assetName')
        investment.asset_type = request.form.get('assetType')
        
        purchase_date = request.form.get('purchaseDate')  
        purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        investment.purchase_date = purchase_date  
        
        investment.purchase_price = request.form.get('purchasePrice')
        investment.quantity = request.form.get('quantity')
        investment.current_price = request.form.get('currentPrice')
        investment.expected_interest_amount = request.form.get('expectedInterestAmount')
        
        interest_payment_date = request.form.get('interestPaymentDate')  
        interest_payment_date = datetime.strptime(interest_payment_date, "%Y-%m-%d")
        investment.interest_payment_date = interest_payment_date  
        
        maturity_date = request.form.get('maturityDate')  
        maturity_date = datetime.strptime(maturity_date, "%Y-%m-%d")
        investment.maturity_date = maturity_date

        user_id = request.form.get('user') 
        investment.user_id = user_id  

        db.session.commit()
        flash('Investment updated!', category='success')
        return redirect(url_for('views.create_investment'))

    return render_template('edit_investment.html', investment=investment, user=current_user, users=users)  # Módosítva



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

# Definiáljuk az admin_dashboard útvonalát.
@views.route('/admin_dashboard')
@login_required
def admin_dashboard():
    users = User.query.filter_by(is_approved=False).all()
    return render_template("admin_dashboard.html", user=current_user, users=users)

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
                interest_payment_date=investment.interest_payment_date,
                maturity_date=investment.maturity_date,
                snapshot_group_id=new_snapshot_group_id  # Folytonos sorszám hozzáadása
            )
            db.session.add(snapshot)
        db.session.commit()
        return jsonify({"message": "Snapshots created successfully"}), 200
    else:
        return jsonify({"message": "No investments found"}), 404


