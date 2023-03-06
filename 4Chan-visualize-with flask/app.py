from flask import Flask, render_template, request
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from mongopass import mongopass
import subprocess as sp
import sys
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField
from wtforms.validators import DataRequired,Length, Email,EqualTo, ValidationError
import os

import pandas as pd
import json
import plotly
import plotly.express as px

SECRET_KEY = os.urandom(32)


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
client = MongoClient(mongopass)
db = client.fourchan
coll =db.Democrats
coll2 =db.Republics

print("CONNecTED")
class BasicForm(FlaskForm):
    ids = StringField("ID",validators=[DataRequired()])
    submit = SubmitField("Submit")


labels = [
    '+Democrtas', '+Republicans', '-Democrtas', '-Republicans'
]

values = [
    16300, 7700,9300,4800
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",]



@app.route('/')
def fourchan():
    date=sp.getoutput("date")
    # dat =  "April "
    return render_template("fourchan.html", date=date)

@app.route("/response",methods =['POST','GET'])
def response():
    posts = []
    form = BasicForm()
    data=[]
    if request.method == "POST":
        data=[]
        searchKey = request.form['ids']
        for dat in coll.find():
            if dat['Subject'].lower().__contains__(searchKey):
                data.append(dat["Subject"])
    if len(data) == 0: 
        data=[]
        for dat in coll.find().limit(10):
            data.append(dat["Subject"])
    return render_template('response.html', data=data, form=form)


@app.route("/republic",methods =['POST','GET'])
def response2():
    posts = []
    form = BasicForm()
    data=[]
    if request.method == "POST":
        data=[]
        searchKey = request.form['ids']
        for dat in coll2.find():
            if dat['Subject'].lower().__contains__(searchKey):
                data.append(dat["Subject"])
    if len(data) == 0: 
        data=[]
        for dat in coll2.find().limit(10):
            data.append(dat["Subject"])
    return render_template('republic.html',  data=data, form=form)

@app.route("/results")
def results():
    bar_labels=labels
    bar_values=values

    return render_template('results.html', title='Election analysis', max=17000, labels=bar_labels, values=bar_values)


if __name__ == '__main__':
    app.run(debug=True)
