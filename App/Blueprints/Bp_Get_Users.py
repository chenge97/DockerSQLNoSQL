from App import app,db
import json
from flask import make_response,request,Blueprint

UserBlueprint = Blueprint('UserBlueprint', __name__)

def get():
    users = db.session.execute("SELECT * FROM Users").fetchall()

    json_list = []

    for u in users:
        json_dict =  {
            'userName':u[1],
            'lastName':u[2],
            'age':u[3]
        }

        json_list.append(json_dict)
    
    return make_response(json.dumps(json_list))

@UserBlueprint.route('/GetPostUsers',methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return get()
    






    