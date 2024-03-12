from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import BowlingCenter, TournamentDirector, Tournament
from .forms import (
    BowlingCenterCreateForm, TournamentDirectorCreateForm, TournamentCreateForm,
    BowlingCenterUpdateForm, TournamentDirectorUpdateForm, TournamentUpdateForm,
)

def home(request):
    return HttpResponse("This is a response")

class BowlingCenterList(ListView):
    model = BowlingCenter
    context_object_name = 'bowling_centers'
    template_name = 'tournaments/bowling_centers/center_list.html'

class BowlingCenterCreate(CreateView):
    model = BowlingCenter
    form_class = BowlingCenterCreateForm
    template_name = 'tournaments/bowling_centers/center_create.html'
    success_url = reverse_lazy('list_centers')

class BowlingCenterUpdate(UpdateView):
    model = BowlingCenter
    form_class = BowlingCenterUpdateForm
    template_name = 'tournaments/bowling_centers/center_update.html'
    success_url = reverse_lazy('list_centers')

class BowlingCenterDelete(DeleteView):
    model = BowlingCenter
    context_object_name = 'center'
    template_name = 'tournaments/bowling_centers/center_delete.html'
    success_url = reverse_lazy('list_centers')

class TournamentDirectorList(ListView):
    model = TournamentDirector
    context_object_name = 'tournament_directors'
    template_name = 'tournaments/tournament_directors/director_list.html'

class TournamentDirectorCreate(CreateView):
    model = TournamentDirector
    form_class = TournamentDirectorCreateForm
    template_name = 'tournaments/tournament_directors/director_create.html'
    success_url = reverse_lazy('list_directors')

class TournamentDirectorUpdate(UpdateView):
    model = TournamentDirector
    form_class = TournamentDirectorUpdateForm
    template_name = 'tournaments/tournament_directors/director_update.html'
    success_url = reverse_lazy('list_directors')

class TournamentDirectorDelete(DeleteView):
    model = TournamentDirector
    context_object_name = 'director'
    template_name = 'tournaments/tournament_directors/director_delete.html'
    success_url = reverse_lazy('list_directors')

class TournamentList(ListView):
    model = Tournament
    context_object_name = 'tournaments'
    template_name = 'tournaments/tournament_list.html'

class TournamentCreate(CreateView):
    model = Tournament
    form_class = TournamentCreateForm
    template_name = 'tournaments/tournament_create.html'
    success_url = reverse_lazy('list_tournaments')

class TournamentUpdate(UpdateView):
    model = Tournament
    form_class = TournamentUpdateForm
    template_name = 'tournaments/tournament_update.html'
    success_url = reverse_lazy('list_tournaments')

class TournamentDelete(DeleteView):
    model = Tournament
    context_object_name = 'tournament'
    template_name = 'tournaments/tournament_delete.html'
    success_url = reverse_lazy('list_tournaments')