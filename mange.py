from flask.ext.script import Manager,Server
from test import app,db,Conversation

manager = Manager(app)
manager.add_command('server',Server())


@manager.shell
def make_shell_context():
    return dict(app=app,db=db,Conversation=Conversation)

if __name__ == "__main__":
    manager.run()