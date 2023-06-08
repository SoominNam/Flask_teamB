from flask_script import Manager
from attendance_manage import app
from attendance_manage.scripts.db import InitDB

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())
    manager.run()