from django.db import models

# Create your models here.

class textBox(models.Model):
    text = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.text

class Image(models.Model):
    image = models.ImageField(upload_to='myimages/')
    imgText = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.imgText
