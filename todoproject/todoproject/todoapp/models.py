from django.db import models

# Create your models here.
class TodoItem(models.Model):
	content_title = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	content = models.TextField(null=True)