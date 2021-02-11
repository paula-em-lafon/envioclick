from django.db import models
from django.db.models import Q, Count
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
import datetime
import random

class Waiter(models.Model):
    id = models.AutoField(primary_key=True)
    waiter = models.CharField(max_length=200)


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    arrival = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField(null=True, blank=True)
    waiter = models.ForeignKey('Waiter', on_delete=models.CASCADE, blank=True)
    table = models.ForeignKey('Table', on_delete=models.CASCADE, blank=True)
    total_ammount= models.DecimalField(max_digits=15, decimal_places=2)
    
    def save(self, *args, **kwargs):
        if self.id == None:
            time = datetime.datetime.now()

            # check for waiters
            waiters = Waiter.objects.select_related().annotate(num_Service=Count('service', filter=Q(service__exit__gt=time))).all()
            available_waiters = waiters.filter(num_Service__lt=4)
            avalable_waiters_length = len(available_waiters)
            # check for tables
            tables = Table.objects.select_related().annotate(num_Service=Count('service', filter=Q(service__exit__gt=time))).all()
            available_tables = tables.filter(num_Service__lt=1)
            avalable_tables_length = len(available_tables)
            # return exception if a problem arises
            if avalable_tables_length == 0 and avalable_waiters_length == 0:
                raise ValidationError("not enough waiters or tables")
            if avalable_waiters_length == 0:
                raise ValidationError("not enough waiters")
            if avalable_tables_length == 0:
                raise ValidationError("not enough tables")
                return
            # assign waiter and table
            waiter_obj = random.choice(available_waiters)
            self.waiter = waiter_obj
            table_obj = random.choice(available_tables)
            self.table = table_obj

            print(time.time())
            # check if current time is open
            if datetime.time(9,0) < time.time() and time.time()> datetime.time(21, 30):
                raise ValidationError("The restaurant is closed")

            print(time.time())
            # add timedelta to init_time
            if time.time() < datetime.time(17,0):
                print(time + datetime.timedelta(minutes=90))
                self.exit = time + datetime.timedelta(minutes=90)
            if time.time() > datetime.time(17,0):
                self.exit = time + datetime.timedelta(minutes=120)

            #finalize pre_save
            return super(Service, self).save(*args, **kwargs)

class Table(models.Model):
    id = models.AutoField(primary_key=True)
    table_no = models.CharField(max_length=200)


# @receiver(pre_save, sender=Service)
# def prepare_service(sender, instance, *args, **kwargs):
#     if instance.id == None:
#         time = datetime.datetime.now()

#         # check for waiters
#         waiters = Waiter.objects.select_related().annotate(num_Service=Count('service', filter=Q(service__exit__gt=time))).all()
#         available_waiters = waiters.filter(num_Service__lt=4)
#         avalable_waiters_length = len(available_waiters)
#         # check for tables
#         tables = Table.objects.select_related().annotate(num_Service=Count('service', filter=Q(service__exit__gt=time))).all()
#         available_tables = tables.filter(num_Service__lt=1)
#         avalable_tables_length = len(available_tables)
#         # return exception if a problem arises
#         if avalable_tables_length == 0 and avalable_waiters_length == 0:
#             print("not enough waiters or tables")
#         if avalable_waiters_length == 0:
#             print("not enough waiters")
#             return
#         if avalable_tables_length == 0:
#             print("not enough tables")
#             return
#         # assign waiter and table
#         waiter_obj = random.choice(available_waiters)
#         instance.waiter = waiter_obj
#         table_obj = random.choice(available_tables)
#         instance.table = table_obj

#         print(time.time())
#         # check if current time is open
#         if datetime.time(9,0) < time.time() and time.time()> datetime.time(21, 30):
#             print("The restaurant is closed")
#             return
        
#         print(time.time())
#         # add timedelta to init_time
#         if time.time() < datetime.time(17,0):
#             print(time + datetime.timedelta(minutes=90))
#             instance.exit = time + datetime.timedelta(minutes=90)
#         if time.time() > datetime.time(17,0):
#             instance.exit = time + datetime.timedelta(minutes=120)

#         #finalize pre_save
#         pass
