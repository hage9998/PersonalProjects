from create_app import create_app
import json
import base64

app = create_app()
client = app.test_client()
query_create = 'CREATE TABLE house (name_id INTEGER AUTO_INCREMENT PRIMARY KEY, id BIGINT, date DATE, price integer, grade integer, bedrooms integer, bathrooms integer, floors integer, waterfront integer, yr_built integer, condition_house integer);'
query_insert = 'INSERT INTO houses.house (id, date, price, grade, bedrooms, bathrooms, floors, waterfront, yr_built, condition_house) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
hostname = 'localhost'
login_user = 'root'
pass_user = '2311'
databse = 'houses'
dataset = 'home_data.csv'

response = client.post('/route', json={
    'query_create': query_create,
    'query_insert': query_insert,
    'hostname': hostname,
    'login_user': login_user,
    'pass_user': pass_user,
    'databse':databse,
    'dataset': dataset
}) 


