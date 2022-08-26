from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os


class Post(models.Model):

	title = models.CharField(max_length=200)
	file = models.FileField(null=True,blank=True,upload_to='Files')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def get_file_name(self):
		name, extension = os.path.splitext(self.file.name)
		return name.split('/')[1] + extension
