from django.db import models

class Item(models.Model):
    name=models.CharField()
    description = models.TextField()


    def __str__(self):
        return self.name