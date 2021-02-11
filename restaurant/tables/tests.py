from django.test import TestCase
from .models import Waiter, Service, Table
from django.core.exceptions import ValidationError
import datetime
import mock

class CreationBeforeFiveTestCase(TestCase):
    def mock_now():
        return datetime.datetime(2021, 1, 1, 11, 0, 0)
    def setUp(self):
        print("----------------CASE 1----------------")
        self.waiter = Waiter.objects.create(waiter="juan")
        self.table = Table.objects.create(table_no="table 1")

    @mock.patch('django.utils.timezone.now', mock_now)
    def test_creation(self):
        import datetime
        class NewDateTime(datetime.datetime):
            @classmethod
            def now(cls):
                return cls(2021, 1, 1, 11, 0, 0)
        datetime.datetime = NewDateTime
        #actualTests
        self.service = Service.objects.create(tip=19.5)
        self.assertTrue(isinstance(self.service.waiter, Waiter))
        arrival = self.service.arrival
        exit = self.service.exit
        self.assertTrue(abs((exit-arrival).seconds/60) >= 90)

class CreationAfterFiveTestCase(TestCase):
    def mock_now():
        return datetime.datetime(2021, 1, 1, 18, 0, 0)
    def setUp(self):
        print("------------CASE 2-----------------")
        self.waiter = Waiter.objects.create(waiter="juan")
        self.table = Table.objects.create(table_no="table 1")

    @mock.patch('django.utils.timezone.now', mock_now)
    def test_creation(self):
        import datetime
        class NewDateTime(datetime.datetime):
            @classmethod
            def now(cls):
                return cls(2021, 1, 1, 18, 0, 0)
        datetime.datetime = NewDateTime
        #actualTests
        self.service = Service.objects.create(tip=19.5)
        self.assertTrue(isinstance(self.service.waiter, Waiter))
        arrival = self.service.arrival
        exit = self.service.exit
        self.assertTrue(abs((exit-arrival).seconds/60) >= 120)

class CreationBeforeOpenTestCase(TestCase):
    def mock_now():
        return datetime.datetime(2021, 1, 1, 0, 30, 0)
    def setUp(self):
        print("----------------CASE 3----------------")
        self.waiter = Waiter.objects.create(waiter="juan")
        self.table = Table.objects.create(table_no="table 1")

    @mock.patch('django.utils.timezone.now', mock_now)
    def test_creation(self):
        import datetime
        class NewDateTime(datetime.datetime):
            @classmethod
            def now(cls):
                return cls(2021, 1, 1, 0, 30, 0)
        datetime.datetime = NewDateTime
        #actualTests
        with self.assertRaises(ValidationError):
            Service.objects.create(tip=19.5)


class CreationNoTablesTestCase(TestCase):
    def mock_now():
        return datetime.datetime(2021, 1, 1, 18, 0, 0)
    def setUp(self):
        print("------------CASE 4-----------------")
        self.waiter = Waiter.objects.create(waiter="juan")
        self.table = Table.objects.create(table_no="table 1")

    @mock.patch('django.utils.timezone.now', mock_now)
    def test_creation(self):
        import datetime
        class NewDateTime(datetime.datetime):
            @classmethod
            def now(cls):
                return cls(2021, 1, 1, 18, 0, 0)
        datetime.datetime = NewDateTime
        #actualTests
        self.service = Service.objects.create(tip=19.5)
        with self.assertRaises(ValidationError):
            Service.objects.create(tip=19.5)

class CreationNoTablesNoWaitersTestCase(TestCase):
    def mock_now():
        return datetime.datetime(2021, 1, 1, 18, 0, 0)
    def setUp(self):
        print("------------CASE 5-----------------")
        self.waiter = Waiter.objects.create(waiter="juan")
        self.table = Table.objects.create(table_no="table 1")
        self.table2 = Table.objects.create(table_no="table 2")
        self.table3 = Table.objects.create(table_no="table 3")
        self.table4 = Table.objects.create(table_no="table 4")
        

    @mock.patch('django.utils.timezone.now', mock_now)
    def test_creation(self):
        import datetime
        class NewDateTime(datetime.datetime):
            @classmethod
            def now(cls):
                return cls(2021, 1, 1, 18, 0, 0)
        datetime.datetime = NewDateTime
        #actualTests
        self.service = Service.objects.create(tip=19.5)
        self.service2 = Service.objects.create(tip=19.5)
        self.service3 = Service.objects.create(tip=19.5)
        self.service4 = Service.objects.create(tip=19.5)
        with self.assertRaises(ValidationError):
            Service.objects.create(tip=19.5)

class CreationNoWaitersTestCase(TestCase):
    def mock_now():
        return datetime.datetime(2021, 1, 1, 18, 0, 0)
    def setUp(self):
        print("------------CASE 6-----------------")
        self.waiter = Waiter.objects.create(waiter="juan")
        self.table = Table.objects.create(table_no="table 1")
        self.table2 = Table.objects.create(table_no="table 2")
        self.table3 = Table.objects.create(table_no="table 3")
        self.table4 = Table.objects.create(table_no="table 4")
        self.table5 = Table.objects.create(table_no="table 4")
        

    @mock.patch('django.utils.timezone.now', mock_now)
    def test_creation(self):
        import datetime
        class NewDateTime(datetime.datetime):
            @classmethod
            def now(cls):
                return cls(2021, 1, 1, 18, 0, 0)
        datetime.datetime = NewDateTime
        #actualTests
        self.service = Service.objects.create(tip=19.5)
        self.service2 = Service.objects.create(tip=19.5)
        self.service3 = Service.objects.create(tip=19.5)
        self.service4 = Service.objects.create(tip=19.5)
        with self.assertRaises(ValidationError):
            Service.objects.create(tip=19.5)