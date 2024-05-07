from flask import Flask
from flask import render_template

import pandas as pd # for csv
import requests     # for api
import sqlite3      # for sql

from datetime import datetime
from PIL import Image
from io import BytesIO
import base64

my_app = Flask(__name__)

CSV_DATA = 'nutritions.csv'
URL_ENDPOINT = 'https://www.themealdb.com/api/json/v1/1/random.php'
sql_for_table1 = 'SELECT field1, field2 FROM table1'

my_database = 'commonfood.db'
my_df = pd.read_csv(CSV_DATA, skipfooter=1, engine='python')

import requests
from datetime import datetime

def get_api_data(url_endpoint):
    response = requests.get(url_endpoint)
    
    if response.status_code == 200:
        data = response.json()
        meal = data['meals'][0]
        
        meal_name = meal['strMeal']
        category = meal['strCategory']
        area = meal['strArea']
        instructions = meal['strInstructions']
        meal_thumb = meal['strMealThumb']
        youtube_link = meal['strYoutube']
        
        # Download the image and encode it as base64
        image_response = requests.get(meal_thumb)
        image_base64 = base64.b64encode(image_response.content).decode('utf-8')
        
        # Construct meal data dictionary
        meal_data = {
            'meal_name': meal_name,
            'category': category,
            'area': area,
            'instructions': instructions,
            'image_base64': image_base64,
            'youtube_link': youtube_link
        }
        
        return meal_data
    else:
        return None   

def get_csv_data(my_df):
    my_df_top_ten = my_df.head(10)
    return my_df_top_ten.to_html()

def get_calories(food_name, my_df):
    food_data = my_df[my_df['Item'].str.lower() == food_name.lower()]
    if not food_data.empty:
        calories = food_data['Calories'].iloc[0]
        return calories
    else:
        return "Calories not found for {}".fortmat(food_name)    

def get_sql_data(sql_statement):
    con = sqlite3.connect(my_database)
    cur = con.cursor() 
    cur.execute(sql_statement)
    result = cur.fetchall()
    con.close()
    table = pd.DataFrame(result)  
    return table.to_html()

#------------------------------------------------------------------------------

@my_app.route('/')
def index():
    return render_template('index.html', csv_table=get_csv_data(my_df))

@my_app.route('/calculate', methods=['POST'])
def calculate():
    food_name = requests.form['food_name']
    my_df = get_csv_data(CSV_DATA)
    calories = get_calories(food_name, my_df)
    return render_template('result.html', food_name=food_name, calories=calories)

@my_app.route('/api1')
def api1():
    meal_data = get_api_data(URL_ENDPOINT)
    if meal_data:
        return render_template('api1.html', meal_data=meal_data)
    else:
        return 'Failed to fetch meal data'

@my_app.route('/sql')
def sql():
    return render_template('sql.html', sql_data=get_sql_data(sql_for_table1))

if __name__ == '__main__':  3
my_app.run()