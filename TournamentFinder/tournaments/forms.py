from django import forms

from .models import BowlingCenter, TournamentDirector, Tournament

class BowlingCenterForm(forms.ModelForm):
    class Meta:
        model = BowlingCenter
        fields = '__all__'

class TournamentDirectorForm(forms.ModelForm):
    class Meta:
        model = TournamentDirector
        fields = '__all__'

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'