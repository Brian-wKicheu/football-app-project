from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(null=True, blank=True, max_length=15)
    joined_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"