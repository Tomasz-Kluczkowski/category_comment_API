from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from model import db
from run import create_app


app = create_app('config')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

# python migrate.py db init   -  to run migration initialization
# python migrate.py db migrate  - to create tables
# python migrate.py db upgrade  - apply migration to the database

# When the models / database changes run migrate and upgrade commands!
