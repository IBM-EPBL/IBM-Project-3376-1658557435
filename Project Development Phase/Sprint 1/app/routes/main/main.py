import os
from flask import Blueprint, request

from utils.jwt_token import validate_token

main_bp = Blueprint('main_bp', __name__, template_folder='templates')

@main_bp.route('/', methods = ['POST', 'GET'])
@validate_token
def main():
  token = request.cookies.get('access-token') 
  return str(token)

@main_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join('./upload', file1.filename)
        file1.save(path)
        return path

        return 'ok'
    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''

from flask import send_file

@main_bp.route('/get_image')
def get_image():    
    return send_file('./upload/' + request.args.get('name'), mimetype='image/gif')
