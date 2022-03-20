from . import db

class propertyInfo(db.Model):
    __tablename__ = 'property_info'

    propertyID = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    propertyTitle = db.Column(db.String(50), nullable=False)
    no_rooms = db.Column(db.Integer, nullable=False)
    no_bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(50), nullable=False)
    propertyType = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    upload = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.Date, nullable=False)

    def __init__(self, propertyTitle, description, no_rooms, no_bathrooms, price, 
    propertyType, location, upload, date_created):
        self.propertyTitle = propertyTitle
        self.description = description
        self.no_rooms = no_rooms
        self.no_bathrooms = no_bathrooms
        self.price = price
        self. propertyType = propertyType
        self.location = location
        self.upload = upload
        self.date_created = date_created

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.propertyType)