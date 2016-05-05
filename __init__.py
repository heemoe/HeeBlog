from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "heeblog", 'PORT': 27019}  # set DB name
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
db = MongoEngine(app)

# Apis
api = Api(app)
from models import Post as Article

# TODOS = {
#     'todo1': {'task': 'build an API'},
#     'todo2': {'task': '?????'},
#     'todo3': {'task': 'profit!'},
# }
articles = Article.objects.all()
alist = dict()
for one in articles:
    myComments = dict()
    if one.comments is None:
        myComments = {}
    else:
        for comment in one.comments:
            myComments = {
                'created_at': str(comment.created_at),
                'body': str(comment.body),
                'author' : str(comment.author),
            }
    json_dict = {
        'created_at' : str(one.created_at),
        'title' : one.title,
        'slug' : one.slug,
        'body' : str(one.body),
        'comments' : myComments
    }
    alist.setdefault(one.slug, json_dict)


def abord_if_slug_not_exist(slug):
    if slug not in alist.keys():
        abort(404, message="Slug {} doesn't exist".format(slug))

parser = reqparse.RequestParser()
parser.add_argument('slug')

class Post(Resource):
    def get(self, slug):
        abord_if_slug_not_exist(slug)
        return alist[slug]

class Posts(Resource):
    def get(self):
        print(alist)
        return {"posts":alist}

    # def post(self):
    #     args = parser.parse_args()
    #     print(args)
    #     todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
    #     todo_id = 'todo%i' % todo_id
    #     TODOS[todo_id] = {'task', args['task']}
    #     return TODOS[todo_id],201

api.add_resource(Posts, '/posts/')
api.add_resource(Post, '/posts/<slug>')

def register_blueprints(app):
    from views import posts
    from admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)
if __name__ == '__main__':
    app.run()
