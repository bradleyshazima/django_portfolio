from django.db import models

# Create your models here.

class About(models.Model):
    bio = models.TextField()
    experience = models.IntegerField()
    projects = models.IntegerField()
    sites_online = models.IntegerField()

    def __str__(self):
        return self.bio

class Contact(models.Model):
    phone = models.CharField(max_length=15)
    mail = models.EmailField()

    def __str__(self):
        return self.phone
    
class Contact_Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"