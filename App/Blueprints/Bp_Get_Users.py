from App import app,db
import json
from flask import make_response,request,Blueprint,request

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
def post():
    db.session.execute("CREATE TABLE IF NOT EXISTS Users (id SERIAL PRIMARY KEY, name VARCHAR(100),lastname VARCHAR(100),age VARCHAR(50))")
    json_list = request.get_json(force=True)
    if isinstance(json_list,str):
        json_list = json.loads(json_list)

    for json_data in json_list:
        db.session.execute("INSERT INTO Users (name,lastname,age) VALUES (:name,:lastname,:age)",{"name":json_data["name"],"lastname":json_data["lastname"],"age":json_data["age"]})

    return "Success"

@UserBlueprint.route('/GetPostUsers',methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return get()
    elif request.method == 'POST':
        return post()
    






    