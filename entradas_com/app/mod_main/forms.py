# Import Form and RecaptchaField (optional)
from flask.ext.wtf import Form # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField # BooleanField

# Import Form validators
from wtforms.validators import Required

# Define the login form (WTForms)S

class SearchForm(Form):
	search = TextField('Search', [Required(message='Search!')])
