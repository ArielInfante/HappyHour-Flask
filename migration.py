from app import app, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


'''
    CONFIGURE APP
'''
from config import config
app.config.from_object(config['development'])

'''
    INIT EXTENSIONS/PACKAGES
'''
migrate = Migrate(app, db)
manager = Manager(app)


'''
    ADD COMMANDS
'''
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
