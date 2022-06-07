from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from markupsafe import escape
import csv
from form import Format
import requests
import dotenv

values = dotenv.dotenv_values()


app = Flask(__name__)
app.config['SECRET_KEY'] = values["FLASK_SECRET_KEY"]
Bootstrap(app)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = Format()
    try:
        if request.form['email']:
            if request.form['email'] == values["CAFE_MAIL"] and request.form['Password'] == values["CAFE_PASSWORD"]:
                return render_template('add.html', form=form)
            else:
                return render_template('denied.html')
    except KeyError:
        new_row = []
        if form.validate_on_submit():
            keys = list(form.data.keys())
            for key in range(len(keys)-2):
                new_row.append(form.data[keys[key]])
            with open("cafe-data.csv", newline='', encoding="utf-8", mode='a') as file:
                data = csv.writer(file)
                data.writerow(new_row)
            form = Format(formdata=None)
        # Exercise:
        # Make the form write a new row into cafe-data.csv
        # with   if form.validate_on_submit()
        return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('data_cafes.csv', newline='',encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
