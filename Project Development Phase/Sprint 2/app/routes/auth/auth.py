from flask import Blueprint, jsonify, make_response, redirect, request, render_template

import controllers.auth_controller as auth_controller
import controllers.user_controller as user_controller

from models.user import User

from keys import SERVER_SECRET

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', static_folder='static')

@auth_bp.route('/register', methods = ['POST', 'GET'])
def register():
  if request.method == 'GET':  
    return render_template('register.html')

  elif request.method == 'POST':        
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    retyped_password = request.form["retyped_password"]

    if password != retyped_password:
      return render_template('register.html', error="password is not matching")

    user = user_controller.fetch_user_by_email(email)

    if not user:
      user = user_controller.create_user(User(userid=None, name=name, email=email, password=password))
      auth_controller.send_verification_mail(user)
    
    user = user_controller.fetch_user_by_email(email)      

    if user.password == password:
      token = auth_controller.gen_access_token(user)

      res = make_response(redirect("/main"))
      res.set_cookie('access-token', token)
      return res            
    else:
      return render_template('register.html', error="user already exists")

@auth_bp.route('/login', methods = ['POST', 'GET'])
def login():
  if request.method == 'GET':  
    return render_template('login.html')

  elif request.method == 'POST':  
    email = request.form["email"]
    password = request.form["password"]

    user = user_controller.fetch_user_by_email(email)
    
    if user:
      if user.password == password:
        token = auth_controller.gen_access_token(user)

        res = make_response(redirect("/main"))
        res.set_cookie('access-token', token)
        return res 
      else: 
        return render_template('login.html', error="password is wrong")
    else:
        return render_template('login.html', error="user is not exists")


@auth_bp.route('/verify')
def verify():
  vcode = request.args.get('vcode') or ''
  nonce = request.args.get('nonce') or ''

  try:
    decoded_vcode = auth_controller.decode_token(vcode)

    if nonce == decoded_vcode['nonce']:
      return render_template('verify.html', msg=decoded_vcode['email'] + " is verified, Thank you!")
    else:
      return render_template('verify.html', msg="error occured! Not verified")
  except Exception as error:
      return render_template('verify.html', msg=error)


@auth_bp.route('/isvalid')
def isvalid():
  try:
    token = request.args.get('token') or ''
    ss = request.args.get('ss') or ''

    if ss != SERVER_SECRET:
      return jsonify({
        'status': True,
        'error': 'Not Authorized'
      })

    user = auth_controller.decode_token(token)
    return jsonify({
      'status': True,
      'user': user
    })
  except Exception as error:
    return jsonify({
      'status': False,
      'error': str(error)
    })

