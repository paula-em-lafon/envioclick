from app import app as app
import unittest
from models import db, Waiter, Table, Service
from freezegun import freeze_time
import datetime
import pytz


class UserTest(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///test.db'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    dt = datetime.datetime(2018,1,1,11,0,0,tzinfo=pytz.timezone('America/Mexico_City'))
    @freeze_time(dt)
    def test_models(self):
        #Create a Table and a Waiter
        table = Table(table_no="table1")
        db.session.add(table)
        waiter = Waiter(name="Juan")
        db.session.add(waiter)
        db.session.commit()
        service = Service(tip=90.80)
        db.session.add(service)
        db.session.commit()
        
        query =  Service.query.all()
        #Check that all users exist
        assert len(query) == 1
        assert query[0].table_id == 1
        assert query[0].waiter_id == 1
        assert ((query[0].exit-query[0].arrival).seconds/60) >= 90
