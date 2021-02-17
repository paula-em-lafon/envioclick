from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import func
from sqlalchemy.exc import IntegrityError
import datetime
import pytz
import random
mx = pytz.timezone('America/Mexico_City')

db = SQLAlchemy(app)

class Waiter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    services = db.relationship("Service", back_populates="waiter")

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_no = db.Column(db.String(128))
    services = db.relationship("Service", back_populates="table")
    
class Service(db.Model):

    def __init__(self, tip):
        time = datetime.datetime.now(mx)
        self.tip = tip
        # check for waiters
        waiters = db.session.query(Waiter, func.count(Service.id).\
            filter(Service.exit>time)).\
                outerjoin(Service).group_by(Waiter).all()
        print(waiters)
        available_waiters= [i for i in waiters if i[1] < 4]
        available_waiters_length = len(available_waiters)
        # Check for tables
        tables = db.session.query(Table, func.count(Table.id).\
            filter(Service.exit>time)).\
                outerjoin(Service).group_by(Table).all()
        print(tables)
        available_tables= [i for i in tables if i[1] < 1]
        available_tables_length = len(available_tables)
        #check if available 
        if available_tables_length == 0 and available_waiters_length == 0:
            raise Exception("not enough waiters or tables")
        if available_waiters_length == 0:
            raise Exception("not enough waiters")
        if available_tables_length == 0:
            raise Exception("not enough tables")
        # add waiter and table
        waiter_obj = random.choice(available_waiters)
        self.waiter_id = waiter_obj[0].id
        table_obj = random.choice(available_tables)
        self.table_id = table_obj[0].id

        
        # check if current time is open
        if time.time() < datetime.time(9,0) or time.time()> datetime.time(23, 30):
            raise Exception("The restaurant is closed")
        # add timedelta to init_time
        if time.time() < datetime.time(17,0):
            self.exit = time + datetime.timedelta(minutes=90)
        if time.time() > datetime.time(17,0):
            self.exit = time + datetime.timedelta(minutes=120)

    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))
    table = db.relationship("Table", back_populates="services")
    waiter_id = db.Column(db.Integer, db.ForeignKey('waiter.id'))
    waiter = db.relationship("Waiter", back_populates="services")
    arrival = db.Column(db.DateTime, default=datetime.datetime.now(mx))
    exit = db.Column(db.DateTime)
    tip = db.Column(db.Numeric(10,2))

        

