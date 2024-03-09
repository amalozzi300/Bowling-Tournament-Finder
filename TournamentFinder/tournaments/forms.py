from django import forms

from .models import BowlingCenter, TournamentDirector, Tournament

class BowlingCenterCreateForm(forms.ModelForm):
    class Meta:
        model = BowlingCenter
        fields = '__all__'

class TournamentDirectorCreateForm(forms.ModelForm):
    class Meta:
        model = TournamentDirector
        fields = '__all__'

class TournamentCreateForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'