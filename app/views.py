"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os, random, datetime, psycopg2
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask import session, abort, send_from_directory, jsonify, make_response
from werkzeug.utils import secure_filename
from app.forms import ContactForm
from app.models import propertyInfo 

conn = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'])

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Shenor Anglin")

@app.route('/property', methods= ['POST', 'GET'])
def newProperty():
    """Render's the website's Property form"""
    # instatiate form class
    form = form()

    # validate file upload on submit
    if request.method =='POST' and form.validate_on_submit():

        # getting form data
        propertyTitle = form.propertyTitle.data
        description = form.description.data
        no_rooms = form.no_rooms.data
        no_bathrooms = form.no_bathrooms.data
        price = form.price.data
        propertyType = form.propertyType.data
        location = form.location.data

        # retrieve and save photo of property to uploads folder
        userfile = request.files['upload']
        filename = secure_filename(userfile.filename)
        userfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # retrieve and save photo of property
        userfile = request.files['upload']
        filename = secure_filename(userfile.filename)
        userfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # generate propertyID and date created
        propertyID = genID(propertyTitle, filename)
        date_created = datetime.date.today()

        # database entry 
        newProperty = propertyInfo(propertyID = propertyID, propertyTitle = propertyTitle, description = description, no_rooms = no_rooms, 
        no_bathrooms = no_bathrooms, price = price, propertyType = propertyType, location = location, upload = filename,  
        date_created = date_created)

        #add entry to database and commit changes
        db.session.add(newProperty)
        db.session.commit()

        # flash message
        flash ('Property uploaded sucessfully', 'success')
        return redirect(url_for('properties'))

        # flash error message
        flash_errors(form)
        """renders the website's newProperty page."""
    return render_template('newProperty.html', form = form)

# route for displaying a file's url
@app.route('/uploads/<filename>')
def genID(propertyTitle, filename):
    id = []
    for x in propertyTitle:
        id.append(str(ord(x)))
    for x in filename:
        id.append(str(ord(x)))
    random.shuffle(id)
    res = ''.join(id)
    return int(res[:5])

# route for displaying all properties
@app.route('/properties/', methods =["GET", "POST"])
def properties():
    properties = propertyInfo.query.all()
    if request.method == "GET":
        return render_template('properties.html', properties = properties)
    elif request.method == "POST":
        response = make_response(jsonify(properties))
        response.headers['Content-Type'] = 'application/json'
        return response

# route for displaying a specific or selected property
@app.route('/property/<propertyID>', methods= ["GET", "POST"])
def getProperty(propertyID):
    proprty = propertyInfo.query.filter_by(propertyID = propertyID).first()
    if request.method == "GET":
        return render_template('viewProperty.html', proprty = proprty)
    elif request.method == "POST":
        if proprty is not None:
            response = make_response(jsonify(propertyID = proprty.propertyID, propertyTitle = proprty.propertyTitle, no_rooms = proprty.no_rooms,
            description = proprty.description, upload = proprty.filename, date_created = proprty.date_created))
            response.headers['Content-Type'] = 'application/json'
            return response
        else:
            flash ('Property Not Found!', 'danger')
            return redirect(url_for("home"))

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
