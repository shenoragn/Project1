from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, Regexp
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    propertyTitle = StringField('Property Title', validators = [InputRequired(), Length(min=1, max=60)])
    description = TextAreaField('Description of Property', validators = [InputRequired(), Length(min=1, max=600)])
    no_rooms = IntegerField('No. of Rooms', validators = [InputRequired()])
    no_bathrooms = IntegerField('No. of Bathrooms', validators = [InputRequired()])
    price = StringField('Price', validators = [InputRequired(), Length(min=1, max=100)])
    propertyType = SelectField(label = 'Property Type', choices =[("House", "House"), ("Apartment", "Apartment"), ("Town House", "Town House"), ("Cottage", "Cottage")])
    location = StringField('Location', validators = [InputRequired(), Length(min = 1, max = 300)])
    upload = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'jpeg', 'png'], 'PLease select an Image!')])