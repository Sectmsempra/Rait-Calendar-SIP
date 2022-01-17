import uuid


from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    category_choices =(
        ("CS", 'CS'),
        ("IT", 'IT'),
        ("EXTC", 'EXTC'),
        ("INSTRU", 'INSTRU'),
    )
    # product_id = models.BigAutoField(primary_key=True)
    # product_id2 = models.CharField(max_length=100, default='')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices= category_choices)
    time = models.DateTimeField()
    desc = models.CharField(max_length=10000000000000)


    class Meta:
         db_table = "Event"

class CSEvent(models.Model):
    category_choices =(
        ("CS", 'CS'),
        ("IT", 'IT'),
        ("EXTC", 'EXTC'),
        ("INSTRU", 'INSTRU'),
    )
    # product_id = models.BigAutoField(primary_key=True)
    # product_id2 = models.CharField(max_length=100, default='')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices= category_choices)
    time = models.DateTimeField()
    desc = models.CharField(max_length=10000000000000)


    class Meta:
         db_table = "CSEvent"

class ITEvent(models.Model):
    category_choices =(
        ("CS", 'CS'),
        ("IT", 'IT'),
        ("EXTC", 'EXTC'),
        ("INSTRU", 'INSTRU'),
    )
    # product_id = models.BigAutoField(primary_key=True)
    # product_id2 = models.CharField(max_length=100, default='')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices= category_choices)
    time = models.DateTimeField()
    desc = models.CharField(max_length=10000000000000)


    class Meta:
         db_table = "ITEvent"

class EXTCEvent(models.Model):
    category_choices =(
        ("CS", 'CS'),
        ("IT", 'IT'),
        ("EXTC", 'EXTC'),
        ("INSTRU", 'INSTRU'),
    )
    # product_id = models.BigAutoField(primary_key=True)
    # product_id2 = models.CharField(max_length=100, default='')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices= category_choices)
    time = models.DateTimeField()
    desc = models.CharField(max_length=10000000000000)


    class Meta:
         db_table = "EXTCEvent"

class INSTRUEvent(models.Model):
    category_choices =(
        ("CS", 'CS'),
        ("IT", 'IT'),
        ("EXTC", 'EXTC'),
        ("INSTRU", 'INSTRU'),
    )
    # product_id = models.BigAutoField(primary_key=True)
    # product_id2 = models.CharField(max_length=100, default='')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices= category_choices)
    time = models.DateTimeField()
    desc = models.CharField(max_length=10000000000000)


    class Meta:
         db_table = "INSTRUEvent"

class KEvent(models.Model):
    category_choices =(
        ("CS", 'CS'),
        ("IT", 'IT'),
        ("EXTC", 'EXTC'),
        ("INSTRU", 'INSTRU'),
    )
    # product_id = models.BigAutoField(primary_key=True)
    # product_id2 = models.CharField(max_length=100, default='')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices= category_choices)
    time = models.DateTimeField()
    desc = models.CharField(max_length=10000000000000)


    class Meta:
         db_table = "KEvent"

class SEvent(models.Model):
    category_choices =(
        ("CS", 'CS'),
        ("IT", 'IT'),
        ("EXTC", 'EXTC'),
        ("INSTRU", 'INSTRU'),
    )
    # product_id = models.BigAutoField(primary_key=True)
    # product_id2 = models.CharField(max_length=100, default='')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices= category_choices)
    time = models.DateTimeField()
    desc = models.CharField(max_length=10000000000000)


    class Meta:
         db_table = "SEvent"

class AEvent(models.Model):
    category_choices =(
        ("CS", 'CS'),
        ("IT", 'IT'),
        ("EXTC", 'EXTC'),
        ("INSTRU", 'INSTRU'),
    )
    # product_id = models.BigAutoField(primary_key=True)
    # product_id2 = models.CharField(max_length=100, default='')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices= category_choices)
    time = models.DateTimeField()
    desc = models.CharField(max_length=10000000000000)


    class Meta:
         db_table = "AEvent"

class GEvent(models.Model):
    category_choices =(
        ("CS", 'CS'),
        ("IT", 'IT'),
        ("EXTC", 'EXTC'),
        ("INSTRU", 'INSTRU'),
    )
    # product_id = models.BigAutoField(primary_key=True)
    # product_id2 = models.CharField(max_length=100, default='')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices= category_choices)
    time = models.DateTimeField()
    desc = models.CharField(max_length=10000000000000)


    class Meta:
         db_table = "GEvent"

