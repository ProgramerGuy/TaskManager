from __future__ import unicode_literals

from django.db import models
from UserProfile.models import Profile
from datetime import datetime    

class TaskPriority(models.Model):
	identifier = models.CharField(max_length=100)
	color_identifier = models.CharField(max_length=10)

	def __str__(self):
		return self.identifier

	class Meta:
		verbose_name_plural = "Task Priorities"

class UserCategory(models.Model):
	user = models.OneToOneField(Profile)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "User Categories"


class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Categories"

class Task(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	created_date = models.DateField()
	end_date = models.DateField()
	notify = models.BooleanField()
	category = models.ForeignKey(Category)
	priority = models.ForeignKey(TaskPriority)
	users = models.ManyToManyField(Profile, related_name='users')

	def __str__(self):
		return self.name

class DailyTask(models.Model):
	user = models.OneToOneField(Profile)
	name = models.CharField(max_length=100)
	description = models.TextField()
	created_date = models.DateField(default=datetime.now)
	category = models.ForeignKey(UserCategory)

	def __str__(self):
		return self.name

class Project(models.Model):
	user = models.ForeignKey(Profile)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	created_date = models.DateField(auto_now=True)
	project_users = models.ManyToManyField(Profile,related_name='project_users',blank=True)
	tasks = models.ManyToManyField(Task,blank=True)

	def __str__(self):
		return self.name

