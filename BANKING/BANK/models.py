import os
import re
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

from BANKING import settings


class District(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Gender(models.Model):
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.gender


class Materials(models.Model):
    materials = models.CharField(max_length=200)

    def __str__(self):
        return self.materials


class Account_type(models.Model):
    account_type = models.CharField(max_length=200)

    def __str__(self):
        return self.account_type


def validate_phone_number(value):
    """Validate that the phone number is a valid Indian phone number."""
    # Check if the length is 10 digits
    if len(str(value)) != 10:
        raise ValidationError("Phone number should be a 10 digit number.")

    # Check if the number starts with 7, 8, or 9
    if not re.match(r'^[789]\d{9}$', str(value)):
        raise ValidationError('Enter a valid Indian phone number.')


class CreateAccount(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, validators=[validate_phone_number])
    mail_id = models.EmailField(max_length=100)
    address = models.TextField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    account_type = models.ForeignKey(Account_type, on_delete=models.CASCADE, null=True)
    materials_provide = models.ManyToManyField(Materials, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def clean_phone_number(self):
        validate_phone_number(self.phone_number)
        return self.phone_number

    def clean_date_of_birth(self):
        date_of_birth = self.date_of_birth
        if date_of_birth and date_of_birth > datetime.today().date():
            raise ValidationError('Invalid date of birth.')
        return date_of_birth

    def clean_age(self):
        age = self.age
        if age and age < 18:
            raise ValidationError('Age must be 18 or abow.')
        return age


    def __str__(self):
        return self.name
