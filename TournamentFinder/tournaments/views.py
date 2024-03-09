from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import BowlingCenter, TournamentDirector, Tournament

def home(request):
    return HttpResponse("This is a response")

class BowlingCenterListView(ListView):
    model = BowlingCenter
    context_object_name = 'bowling_centers'
    template_name = 'tournaments/bowling_centers/centers_list.html'

class TournamentDirectorListView(ListView):
    model = TournamentDirector
    context_object_name = 'tournament_directors'
    template_name = 'tournaments/tournament_directors/directors_list.html'

class TournamentListView(ListView):
    model = Tournament
    context_object_name = 'tournaments'
    template_name = 'tournaments/tournaments_list.html'