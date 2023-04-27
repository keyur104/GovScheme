from django.db import models

# Create your models here.

class Schemesgov(models.Model):
	scheme = models.CharField(max_length = 500)
	ministry =  models.CharField(max_length = 100)
	'''dol =  models.DateField(auto_now=False, default='<%Y-%m-%d>')'''
	
	sector = models.CharField(max_length = 200)
	provisions = models.TextField()
	state_status=models.CharField(max_length = 50)
	central_status=models.CharField(max_length = 50)
	funds=models.IntegerField()
	rejreason=models.TextField()
	centralminfundstatus=models.CharField(max_length = 50)
	stateminfundstatus=models.CharField(max_length = 50)
	stateauthfundstatus=models.CharField(max_length = 50)
	centralauthfundstatus=models.CharField(max_length = 50)
	docs=models.FileField()
	reminstall=models.IntegerField()
	install=models.IntegerField()

class StateAuth(models.Model):
	scheme = models.CharField(max_length = 500)
	ministry =  models.CharField(max_length = 100)
	efficiency = models.CharField(max_length = 100)
	repcan = models.TextField()
	suggestion = models.TextField()
	remark = models.TextField()
	docs=models.FileField()
	

class Modify(models.Model):
	scheme = models.CharField(max_length = 500)
	provisions = models.TextField()
	funds=models.IntegerField()
	ministry =  models.CharField(max_length = 100)	
	sector = models.CharField(max_length = 200)
	state_status=models.CharField(max_length = 50)
	central_status=models.CharField(max_length = 50)
	rejreason=models.TextField()
	



class Department(models.Model):
	code=models.IntegerField()
	dept_name=models.CharField(max_length=100)	

