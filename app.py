from flask import Blueprint
from flask_restful import Api
from resources.hello import Hello
api_bp = Blueprint('api', __name__)  # create a master route /api
api = Api(api_bp)  # create an instance of that /api

# Adds a new route
api.add_resource(Hello, '/hello')  # Hello is similar to a class based view in Django, add child route /hello to /api
