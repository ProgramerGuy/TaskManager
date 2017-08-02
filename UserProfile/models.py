from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class TypeOfUser(models.Model):
	userType = models.CharField(max_length=30)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.userType

class Profile(models.Model):
	userType = models.ForeignKey(TypeOfUser,null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='profileImg')

	def __str__(self):
		return self.user.username
"""	class Meta:
		permissions = (
		    ('ver_cosas', 'Friendly permission description'),
		) """
