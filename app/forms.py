from wsgiref.validate import validator
from flask_wtf import FlaskForm
#from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    proprtytitle = StringField('Property Title', validators=[DataRequired()])
    description = StringField('Description',validators=[DataRequired()])
    rooms = StringField('No. of Rooms',validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    propertytype = StringField('Property Type', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])