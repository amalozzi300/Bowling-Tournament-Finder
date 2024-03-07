from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import BowlingCenter, TournamentDirector, Tournament

# Create your views here.
def home(request):
    return HttpResponse("This is a response")

def bowling_centers(request):
    context = {'bowling_centers': BowlingCenter.objects.all()}
    return render(request, 'tournaments/bowling_centers.html', context)

