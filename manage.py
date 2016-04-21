import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from flask_script import Manager
from livereload import Server
from __init__ import app

manager = Manager(app)
sever = Server(app.wsgi_app)
# sever.serve(port="80",host="127.0.0.1")
# sever.serve()
manager.add_command("run",sever.serve(

))
# manager.add_command("runserver",Server(
#     use_debugger= True,
#     use_reloader= True,
#     host= '0.0.0.0')
# )
# manager.add_command("dev",Server(
# ))

if __name__ == "__main__":
    manager.run()
