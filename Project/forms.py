from django import forms
from UserProfile.models import Profile, TypeOfUser
from .models import Project,Task

class ProjectForm(forms.ModelForm):

	def setUser(self,user):
		self.user = user

	class Meta:
		model = Project
		fields = ('name','description','project_users',)
		exclude = ('user',)

class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('name','description','end_date','category','priority','users')