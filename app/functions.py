from app import app

def trim_all_spaces(theString):
    return theString.replace(' ', '').lower()

def trim_end_spaces(theString):
    return theString.strip().lower()

def username_is_valid(theUsername):
    return True

def email_is_valid(theEmail):
    try:
        return bool(len(theEmail) > 1) and bool(theEmail.index('.', theEmail.rindex('@')))
    except ValueError:
        return False

def name_is_valid(theName):
    return True

def allowed_extensions(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_IMG_EXTENSIONS']
