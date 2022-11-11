from datetime import date, datetime
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
        nds = main_controller.fetch_food(session['user']['userid'])
        for nd in nds:
            nd['time'] = nd['time'].strftime('%d %b %I %p')

        print(nds)

        return render_template('my_history.html', nd_len=len(nds), nutrition_details=nds)
    except Exception as e:
        print(e)
        return "null"


@main_bp.route('/stats')
@validate_token
def overview():
    try:
        nutrition_details = main_controller.fetch_food(session['user']['userid'])

        time_arr = []
        calories_arr = []
        fat_arr = []
        protein_arr = []
        carbs_arr = []

        calories=0
        fat=0
        protein=0
        carbs=0        

        for nd in nutrition_details:
            time_arr.append(nd['time'].strftime("%d/%m/%Y %H:%M:%S"))
            calories_arr.append(nd['calories'])
            fat_arr.append(nd['fat'])
            protein_arr.append(nd['protein'])
            carbs_arr.append(nd['carbs'])
            
            calories = nd['calories']
            fat = nd['fat']
            protein = nd['protein']
            carbs = nd['carbs']

        nd_len = len(nutrition_details)
        if nd_len <= 0:
            nd_len = 1
        calories=calories/nd_len
        fat=fat/nd_len
        protein=protein/nd_len
        carbs=carbs/nd_len
        
        return render_template('stats.html', calories=calories, fat=fat, protein=protein, carbs=carbs, time_arr=time_arr, calories_arr=calories_arr, fat_arr=fat_arr, protein_arr=protein_arr, carbs_arr=carbs_arr)
    except Exception as e:
        print(e)
        return "null"


@main_bp.route('/add_food')
@validate_token
def add_food():    
    return render_template('add_food/actions.html')


@main_bp.route('/upload_image', methods=['GET', 'POST'])
@validate_token
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
@validate_token
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
            return redirect('/main')               

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
