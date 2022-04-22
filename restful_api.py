import mysql.connector
import json


def get_categories_from_mysql():
    categories = {}
    cnx = mysql.connector.connect(user='walmart', database='walmart', password='walmart')
    all_categories = readin_all_categories(connection=cnx)

    curs = cnx.cursor(buffered=True)
    query = "Select parent, child from categoryrelation"
    curs.execute(query)

    sub_categories = []
    for parent_id, child_id in curs:
        parent = all_categories[parent_id]
        child = all_categories[child_id]
        parent['children'].append(child)
        sub_categories.append(child_id)

    for sub_id in sub_categories:
        del all_categories[sub_id]

    return json.dumps(all_categories)


def readin_all_categories(connection):
    categories = {}
    curs = connection.cursor(buffered=True)
    query = 'Select id,name,description,link from categories'
    curs.execute(query)

    for (id, name, desc, link) in curs:
        category = {'id': id, 'name': name, 'description': desc, 'link': link, 'children': []}
        categories[id] = category

    return categories






