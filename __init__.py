from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "heeblog", 'PORT': 27019}  # set DB name
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
db = MongoEngine(app)

api = Api(app)
class PostAPI(Resource):
    # def __init__(self):
    #     self.reqparse = reqparse.RequestParser()
    #     self.reqparse.add_argument('slug', type = str, required = True, help = 'No post', location = 'json')
    #     self.reqparse.add_argument('description', type = str, default = "", location = 'json')
    #     super(PostAPI, self).__init__()

    def get(self):
        return { 'task': 'test' }
    # def post(self, id):
    #     pass

# api.add_resource(PostAPI, '/Posts/<app: int>', endpoint='test')

def register_blueprints(app):
    from views import posts
    from admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)
if __name__ == '__main__':
    app.run()
