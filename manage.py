import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask_script import Manager, Server
from __init__ import app

manager = Manager(app)
# sever = Server(app.wsgi_app)
# sever.serve(port="80",host="127.0.0.1")
# sever.serve()
# manager.add_command("run",sever.serve(
#     port=80
# ))
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='127.0.0.1',
    port=80
)
                    )
from livereload import Server

server = Server(app.wsgi_app)
manager.add_command("dev", server.serve())

if __name__ == "__main__":
    manager.run()
