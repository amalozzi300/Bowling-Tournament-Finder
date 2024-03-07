from django.db import models

from localflavor.us.models import USStateField, USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class BowlingCenter(models.Model):
    center_name = models.CharField(max_length=75)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = USStateField()
    zip_code = USZipCodeField(max_length=5)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.center_name.title()

class TournamentDirector(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.EmailField(max_length=128)
    phone_number = PhoneNumberField()
    profile_picture = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f'{self.first_name.title()} {self.last_name.title()}'
    
class Tournament(models.Model):
    

    bowling_center = models.ForeignKey(BowlingCenter, on_delete=models.CASCADE)
    tournament_director = models.ForeignKey(TournamentDirector, on_delete=models.CASCADE)
