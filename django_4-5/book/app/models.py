from django.db import models

class Book(models.Model):
    title = models.CharField(default="Unknown")
    author=models.CharField(default="Unknown")
    language = models.CharField(default="Unknown")
    type = models.CharField(default="Unknown")
    comment = models.TextField(default="Unknown")

    def __str__(self):
        return self.title

class Readership(models.Model):
    name = models.CharField(null=True)
    email = models.CharField(null=True)
    gender = models.CharField(null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.gender} - {self.age} years old"


