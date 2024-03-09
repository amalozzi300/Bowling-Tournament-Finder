from django.db import models

from localflavor.us.models import USStateField, USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class BowlingCenter(models.Model):
    center_name = models.CharField(max_length=75)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state = USStateField()
    zip_code = USZipCodeField(max_length=5)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.center_name.title()
    
    # def get_absolute_url(self):
    #     return '/bowling-centers'
    
    class Meta:
        verbose_name = 'Bowling Center'
        ordering = ['state', 'center_name']

class TournamentDirector(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.EmailField(max_length=128)
    phone_number = PhoneNumberField()
    profile_picture = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return f'{self.first_name.title()} {self.last_name.title()}'
    
    # def get_absolute_url(self):
    #     return '/tournament-directors'
    
    class Meta:
        verbose_name = 'Tournament Director'
        ordering = ['first_name', 'last_name']
    
class Tournament(models.Model):
    tournament_name = models.CharField(max_length=128)
    start_time = models.DateTimeField()
    bowling_center = models.ForeignKey(BowlingCenter, on_delete=models.CASCADE)
    tournament_director = models.ForeignKey(TournamentDirector, on_delete=models.CASCADE)

    def __str__(self):
        return self.tournament_name
    
    # def get_absolute_url(self):
    #     return '/tournaments'
    
    class Meta:
        ordering = ['start_time']