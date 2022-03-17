from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, Regexp
from flask_wtf.file import FileField, FileRequired, FileAllowed

class ContactForm(FlaskForm):
    propertyTitle = StringField('Property Title', validators = [InputRequired(), Length(min=1, max=60)])
    Description = TextAreaField('Description of Property', validators = [InputRequired(), Length(min=1, max=300)])
    no_rooms = IntegerField('No. of Rooms', validators = [InputRequired(), Regexp("^\d+$")])
    no_bathrooms = IntegerField('No. of Bathrooms', validators = [InputRequired(), Regexp("^\d+$")])
    price = IntegerField('Price', validators = [InputRequired(), Regexp("^\d+$")])
    propertyType = SelectField(label = 'Property Type', choices =[("House", "House"), ("Apartment", "Apartment"), ("Town House", "Town House"), ("Cottage", "Cottage")])
    location = StringField('Location', validators = [InputRequired(), Length(min = 1, max = 300)])
    upload = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'jpeg', 'png'], 'PLease select an Image!')])