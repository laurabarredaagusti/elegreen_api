from flask import Flask
from flask_cors import CORS

from classes.category import *
from classes.calculate import *
from functions import *
from variables import *

application = Flask(__name__)
CORS(application)

@application.route('/')
def hello_world():
    return 'Desafio API test'

@application.route('/category', methods=['GET'])
def category():
    category = get_argument('category')
    if category == None:
        return 'Missing argument'
    else:
        query = Category(category)
        return query.json

@application.route('/calculate', methods=['GET'])
def calculate():
    brand = get_argument('brand')
    model = get_argument('model')
    price = get_argument('price')
    hours_month = float(get_argument('hours_month'))
    hours_day = float(get_argument('hours_day'))

    if brand == None or model == None or hours_month == None or hours_day == None:
        return 'Missing argument'
    else:
        price, current_datetime = check_today_price_exist()
        calculator = Calculate([brand, model, price, hours_month, hours_day, current_datetime])
        return calculator.json

@application.route('/calculate_from_id', methods=['GET'])
def calculate_from_id():
    id = get_argument('id')
    return id
