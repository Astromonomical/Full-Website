from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, jsonify
from . import db
from .models import Train, Customer, Quote
import json
import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('/customer', methods=['GET'])
def customer():
    return render_template("customer.html", customer_list=Customer.query.all())

@views.route('/addcustomer', methods=['GET', 'POST'])
def add_customer():
    if request.method == "POST":
        name = request.form.get('name')
        address_one = request.form.get('address_one')
        address_two = request.form.get('address_two')
        address_three = request.form.get('address_three')
        postcode = request.form.get('postcode')

        new_customer = Customer(name=name, address_one=address_one, address_two=address_two, address_three=address_three, postcode=postcode)
        db.session.add(new_customer)
        db.session.commit()
        flash("Customer added!", category="success")

        return redirect(url_for("views.customer"))

    return render_template("addcustomer.html")

@views.route('/trains', methods=['GET'])
def trains():
    if request.method == 'GET':
        return render_template("trains.html", trains_list=Train.query.all())

    return render_template("trains.html")

@views.route('/addmachine', methods=['GET', 'POST'])
def add_train():
    if request.method == "POST":
        name = request.form.get('name')
        rate = request.form.get('rate')
        classification = request.form.get('classification')

        new_train = Train(name=name, rate=rate, classification=classification)
        db.session.add(new_train)
        db.session.commit()
        flash("Train added!", category="success")

        return redirect(url_for("views.trains"))

    return render_template("addmachine.html")

@views.route('/delete-train', methods=['POST'])
def delete_train():
    train = json.loads(request.data)
    trainId = train['machineId']
    train = Train.query.get(trainId)
    
    db.session.delete(train)
    db.session.commit()

    return jsonify({})

@views.route('/editmachine', methods=['POST', 'GET'])
def edit_train():
    if request.method == "POST":
        return redirect(url_for("views.trains"))
    return render_template("editmachine.html")


@views.route('/schedule', methods=['GET'])
def schedule():
    date = datetime.date.today()

    return render_template("schedule.html", date=date)

@views.route('/createquote', methods=['GET', 'POST'])
def create_quote():
    date = datetime.date.today()
    year, week_num, day = date.isocalendar()

    if request.method == "POST":
        pla = request.form.get('pla')
        cost = request.form.get('cost')
        cust_id = request.form.get('customer')
        train_id = request.form.get('train')
        week = request.form.get('week')
        year = request.form.get('year')

        new_quote = Quote(PLA=pla, cost=cost, cust_id=cust_id, train_id=train_id, week=week, year=year)
        db.session.add(new_quote)
        db.session.commit()
        flash("Quote created!", category="success")

        return render_template("createquote.html", trains_list=Train.query.all(), customer_list=Customer.query.all(), quote_list=Quote.query.all(), now=date, week=week_num)
    else:
        return render_template("createquote.html", trains_list=Train.query.all(), customer_list=Customer.query.all(), quote_list=Quote.query.all(), now=date, week=week_num)

@views.route('/delete-quote', methods=['POST'])
def delete_quote():
    quote = json.loads(request.data)
    quoteId = quote['quoteId']
    quote = Quote.query.get(quoteId)
    
    db.session.delete(quote)
    db.session.commit()

    return jsonify({})