from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model) :  
	title = models.CharField(max_length=200)
	url = models.TextField()
	date = models.DateTimeField()
	author = models.ForeignKey(User)
	votes = models.IntegerField(default=0)
