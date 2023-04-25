from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, User, Investment
from . import db
import json
from datetime import datetime

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/all-users', methods=['GET'])
@login_required
def all_users():
    users = User.query.all()
    return render_template("all_users.html", users=users, user=current_user)

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

@views.route('/delete-user/<int:user_id>', methods=['GET'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted!', category='success')
    return redirect(url_for('views.all_users'))

# Befektetések létrehozása
@views.route('/create-investment', methods=['GET', 'POST'])
@login_required
def create_investment():
    investments = Investment.query.filter_by(user_id=current_user.id).all()
    if request.method == 'POST':
        # Adatok beszerzése az űrlapból
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

        # Befektetés létrehozása és mentése
        investment = Investment(asset_name=asset_name, asset_type=asset_type, purchase_date=purchase_date, 
                                purchase_price=purchase_price, quantity=quantity, current_price=current_price, 
                                expected_interest_amount=expected_interest_amount, interest_payment_date=interest_payment_date,
                                maturity_date=maturity_date, user_id=current_user.id)
        db.session.add(investment)
        db.session.commit()
        flash('Investment added!', category='success')
        return redirect(url_for('views.home'))
    user_investments = Investment.query.filter_by(user_id=current_user.id)  # Hozzáadtuk ezt a sort
    return render_template('create_investment.html', user_investments=user_investments, user=current_user)

# Befektetések módosítása
@views.route('/edit-investment/<int:investment_id>', methods=['GET', 'POST'])
@login_required
def edit_investment(investment_id):
    investment = Investment.query.get_or_404(investment_id)
    if request.method == 'POST':
        # Adatok frissítése az űrlap alapján
        investment.asset_name = request.form.get('assetName')
        investment.asset_type = request.form.get('assetType')
        
        purchase_date = request.form.get('purchaseDate')  # Add hozzá ezt a sort
        purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
        investment.purchase_date = purchase_date  # És ezt is
        
        investment.purchase_price = request.form.get('purchasePrice')
        investment.quantity = request.form.get('quantity')
        investment.current_price = request.form.get('currentPrice')
        investment.expected_interest_amount = request.form.get('expectedInterestAmount')
        
        interest_payment_date = request.form.get('interestPaymentDate')  # Add hozzá ezt a sort
        interest_payment_date = datetime.strptime(interest_payment_date, "%Y-%m-%d")
        investment.interest_payment_date = interest_payment_date  # És ezt is
        
        maturity_date = request.form.get('maturityDate')  # Add hozzá ezt a sort
        maturity_date = datetime.strptime(maturity_date, "%Y-%m-%d")
        investment.maturity_date = maturity_date  # És ezt is

        db.session.commit()
        flash('Investment updated!', category='success')
        return redirect(url_for('views.home'))

    return render_template('edit_investment.html', investment=investment, user=current_user)



# Befektetések törlése
@views.route('/delete-investment/<int:investment_id>', methods=['GET'])
@login_required
def delete_investment(investment_id):
    investment = Investment.query.get_or_404(investment_id)
    if investment.user_id == current_user.id:
        db.session.delete(investment)
        db.session.commit()
        flash('Investment deleted!', category='success')
    return redirect(url_for('views.create_investment'))
