from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import BowlingCenter, TournamentDirector, Tournament

def home(request):
    return HttpResponse("This is a response")

class BowlingCenterListView(ListView):
    model = BowlingCenter
    context_object_name = 'bowling_centers'
    template_name = 'tournaments/bowling_centers.html'