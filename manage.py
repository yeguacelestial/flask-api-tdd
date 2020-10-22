import os

from flask_script import Manager  # Class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app import models


app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)

# Handle commands
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
