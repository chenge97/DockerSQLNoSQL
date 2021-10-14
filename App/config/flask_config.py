from App.config import POSTGRES_USER,POSTGRES_PASSWORD,POSTGRES_HOST,POSTGRES_DB,SECRET_KEY

class FlaskConfig(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@{host}/{db}'.format(username = POSTGRES_USER,password = POSTGRES_PASSWORD,host = POSTGRES_HOST,db = POSTGRES_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = SECRET_KEY
    DEBUG = True
    TEST = True