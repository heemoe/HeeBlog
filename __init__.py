from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "heeblog",'PORT' : 27019} # set DB name
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
db = MongoEngine(app)
def register_blueprints(app):
    from hee.views import posts
    app.register_blueprint(posts)

register_blueprints(app)
if __name__ == '__main__':
    app.run()
