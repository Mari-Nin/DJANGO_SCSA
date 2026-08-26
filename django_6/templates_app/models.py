from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    position = models.CharField(max_length=100)

    class Meta:
        db_table = 'templates_app_empployee'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title=models.CharField(max_length=200)
    description = models.CharField(max_length=100,null=True)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description = models.CharField(max_length=200,null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on post -{self.title}"

class Rates(models.Model):
    GENDER_CHOICES = [
        ('male','Male'),('female','Female'),('other','Other')
    ]
    user = models.CharField(max_length=20)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    rate = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.rate}"