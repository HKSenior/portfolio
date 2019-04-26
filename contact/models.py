from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = PhoneNumberField()
    message = models.TextField()
    submitted = models.DateTimeField(auto_now_add=True)
