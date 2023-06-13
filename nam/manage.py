from flask_script import Manager
from attendance_management import app
from attendance_management.scripts.db import InitDB

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())
    manager.run()