from django.db import models


# Create your models here.
class Header(models.Model):
    title = models.CharField(max_length=100)

class Sidebar(models.Model):
        content = models.TextField()

class MainContent(models.Model):
      content = models.TextField()

class Footer(models.Model):
      text = models.TextField()
                  