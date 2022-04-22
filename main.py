import os

import mysql
from flask import Flask, render_template, url_for, session, redirect, request
from restful_api import get_categories_from_mysql
import json

app = Flask("__main__")
app.secret_key = 'TMP_SECRET_KEY'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/backend/categories')
def input_categories():
    categories_json = get_categories_json()
    categories = json.loads(categories_json)
    s = sprint_categories(categories)
    return render_template('categories.html', data=s)


def sprint_categories(categories):
    s_ret = ""
    for id in categories:
        s_ret += sprint_category(categories[id], 0)
    return s_ret


def sprint_category(category, level):
    s_ret = "<div>"
    for i in range(level):
        s_ret += "&nbsp;&nbsp;&nbsp;"
    s_ret += "<a>" + str(category['id']) + ":" + category['name'] + "</a><br>"
    for sub in category['children']:
        s_ret += sprint_category(sub, level + 1)
    s_ret += "</div>"
    return s_ret


@app.route('/secrete/categories')
def get_categories_json():
    return get_categories_from_mysql()


@app.route('/api/category/add', methods=['GET', 'POST'])
def add_category():
    categories = {}
    cnx = mysql.connector.connect(user='walmart', database='walmart', password='walmart')
    curs = cnx.cursor(buffered=True)
    curs.execute("insert into categories (name, description, link) values ('{}','{}','{}')".format(
        request.form.get('cat_name'), request.form.get('cat_desc'), request.form.get('cat_link')
    ))
    cnx.commit()
    return redirect("/backend/categories")


@app.route('/api/category/set_relation', methods=['GET', 'POST'])
def add_set_relation():
    categories = {}
    cnx = mysql.connector.connect(user='walmart', database='walmart', password='walmart')
    curs = cnx.cursor(buffered=True)
    curs.execute("insert into categoryrelation (parent, child) values ({},{})".format(
        request.form.get('parent_id'), request.form.get('child_id')
    ))
    cnx.commit()
    return redirect('/backend/categories')


if __name__ == '__main__':
    app.run(debug=True)
