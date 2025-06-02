from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)

class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(100), nullable=False)
    item_delivered = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    delivery_date = db.Column(db.DateTime, nullable=False)

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    disciplinary_records = db.Column(db.Text, nullable=True)
    attendance = db.Column(db.String(50), nullable=True)

class ExtraJob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    job_type = db.Column(db.String(100), nullable=False)
    hours_worked = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    last_maintenance = db.Column(db.DateTime, nullable=False)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 