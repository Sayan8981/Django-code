# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Position(models.Model):
	title=models.CharField(max_length=50)

class Employee(models.Model): 
	fullname=models.CharField(max_length=100)
	emp_code=models.CharField(max_length=5)
	mobile=models.CharField(max_length=15)
	position=models.ForeignKey(Position,on_delete=models.CASCADE)
	#NOTE: models.CASCADE implies that when to delete the position at the same time the corresponding 
	#data will be deleted from Employee model.