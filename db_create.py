from app import db
from app.users.models import User

# create the database and the db table
db.create_all()

# commit the changes
# db.session.commit()