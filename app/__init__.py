from flask import Flask, request, g
from mysql_pandas.db.pysql import db_admin
import pandas as pd

def call_data():
    data = pd.read_csv ("./mysql_pandas/" + g.dataset)   
    df = pd.DataFrame(data, columns = ['id', 'date', 'price', 'grade', 'bedrooms', 'bathrooms', 'floors', 'waterfront', 'yr_built', 'condition'])
    db_instance = db_admin(g.hostname, g.login_user, g.pass_user, g.databse)
    db_instance.init_db()
    db_instance.init_query(g.query_create, None)
    db_instance.init_query(g.query_insert, df)
    return 'OK'

def request_arguments():
    envelope = request.get_json()
    g.query_create = envelope.get('query_create')
    g.query_insert = envelope.get('query_insert')
    g.hostname = envelope.get('hostname')
    g.login_user = envelope.get('login_user')
    g.pass_user = envelope.get('pass_user')
    g.databse = envelope.get('databse')
    g.dataset = envelope.get('dataset')

def create_app():
    app = Flask(__name__)
    app.before_request(request_arguments)
    app.add_url_rule('/route', None, call_data, methods=['POST'])
    return app