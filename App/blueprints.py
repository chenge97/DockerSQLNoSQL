from App import app
from App.Blueprints.Bp_Get_Users import UserBlueprint


app.register_blueprint(UserBlueprint)