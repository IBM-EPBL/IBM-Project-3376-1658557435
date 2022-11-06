from datetime import datetime
import json
from flask import Blueprint, redirect, render_template, request, session
from random import randint
import os

from controllers import auth_controller, user_controller, main_controller
from models.food import Food

from utils.jwt_token import validate_token

main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')


@main_bp.route('/', methods = ['POST', 'GET'])
@main_bp.route('/my_history', methods = ['POST', 'GET'])
@validate_token
def main():
  try:  
    return render_template('homepage.html', nutrition_details=main_controller.fetch_food(session['user']['userid']))
  except Exception as e:
    print(e)
    return "null"


@main_bp.route('/add_food')
def add_food():    
    return render_template('add_food/actions.html')


@main_bp.route('/upload_image', methods=['GET', 'POST'])
def upload_image(): 
    if request.method == 'POST':
        if 'food_image' not in request.files:
            return render_template("add_food/upload_image.html", error="food image is not given")

        image_file_from_client = request.files['food_image']

        nutrition_details = main_controller.analyze_image(image_file_from_client)

        query_str = '?'
        query_str += 'name=' + nutrition_details['name'] + '&'
        query_str += 'accuracy=' + str(nutrition_details['accuracy']) + '&'
        query_str += 'calories=' + str(nutrition_details['calories']) + '&'
        query_str += 'fat=' + str(nutrition_details['fat']) + '&'
        query_str += 'protein=' + str(nutrition_details['protein']) + '&'
        query_str += 'carbs=' + str(nutrition_details['carbs'])

        return redirect('add_details' + query_str)

    return render_template('add_food/upload_image.html')



@main_bp.route('/add_details', methods=['GET', 'POST'])
def add_details():
    name = ''
    accuracy = ''
    calories = ''
    fat = ''
    protein = ''
    carbs = ''

    if request.method == 'POST':
        try:
            # collect details
            name = request.form['food_name']    
            calories = request.form['calories']    
            fat = request.form['fat']    
            protein = request.form['protein']    
            carbs = request.form['carbs']    

            # store in db
            user = session['user']
            food = Food(name, datetime.today().timestamp(), calories, fat, protein, carbs)
            main_controller.save_food(user['userid'], food) 

            # return to home page
            return redirect('/')               

        except Exception as e:
            return render_template('add_food/add_details.html', name=name, accuracy=accuracy, calories=calories, fat=fat, protein=protein, carbs=carbs, error=str(e))
            

        

    try:
        name = request.args['name'] or ''
        accuracy = float(request.args['accuracy'] or '0')
        calories = float(request.args['calories'] or '0')
        fat = float(request.args['fat'] or '0')
        protein = float(request.args['protein'] or '0')
        carbs = float(request.args['carbs'] or '0')
    except:
        pass
        

    return render_template('add_food/add_details.html', name=name, accuracy=accuracy, calories=calories, fat=fat, protein=protein, carbs=carbs)
