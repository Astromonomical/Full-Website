from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, jsonify
from . import db
from .models import Train
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

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
    return render_template("schedule.html")