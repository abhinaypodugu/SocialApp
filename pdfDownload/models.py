from django.db import models

# Create your models here.

class textBox(models.Model):
    text = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.text

