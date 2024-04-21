from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .utils import get_login_status
from .models import BowlingCenter, TournamentDirector, Tournament
from .forms import (
    BowlingCenterCreateForm, TournamentDirectorCreateForm, TournamentCreateForm,
    BowlingCenterUpdateForm, TournamentDirectorUpdateForm, TournamentUpdateForm,
)

def home(request):
    context = {'logged_in': get_login_status(request)}
    return redirect('/tournaments')
    return render(request, 'tournamentfinder/base.html', context)

def login_view(request):
    context = {'login_view': 'active'}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Invalid credentials!')
        
    return render(request, 'registration/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

class BowlingCenterList(ListView):
    model = BowlingCenter
    context_object_name = 'bowling_centers'
    template_name = 'tournamentfinder/list_centers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_in'] = get_login_status(self.request)
        return context

class BowlingCenterCreate(LoginRequiredMixin, CreateView):
    model = BowlingCenter
    form_class = BowlingCenterCreateForm
    template_name = 'tournamentfinder/generic_model_create.html'
    success_url = reverse_lazy('list_centers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Bowling Center'
        return context

class BowlingCenterUpdate(LoginRequiredMixin, UpdateView):
    model = BowlingCenter
    form_class = BowlingCenterUpdateForm
    context_object_name = 'object'
    template_name = 'tournamentfinder/generic_model_update.html'
    success_url = reverse_lazy('list_centers')

class BowlingCenterDelete(LoginRequiredMixin, DeleteView):
    model = BowlingCenter
    context_object_name = 'object'
    template_name = 'tournamentfinder/generic_model_delete.html'
    success_url = reverse_lazy('list_centers')

class TournamentDirectorList(ListView):
    model = TournamentDirector
    context_object_name = 'tournament_directors'
    template_name = 'tournamentfinder/list_directors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_in'] = get_login_status(self.request)
        return context

class TournamentDirectorCreate(LoginRequiredMixin, CreateView):
    model = TournamentDirector
    form_class = TournamentDirectorCreateForm
    template_name = 'tournamentfinder/generic_model_create.html'
    success_url = reverse_lazy('list_directors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Tournament Director'
        return context

class TournamentDirectorUpdate(LoginRequiredMixin, UpdateView):
    model = TournamentDirector
    form_class = TournamentDirectorUpdateForm
    context_object_name = 'object'
    template_name = 'tournamentfinder/generic_model_update.html'
    success_url = reverse_lazy('list_directors')

class TournamentDirectorDelete(LoginRequiredMixin, DeleteView):
    model = TournamentDirector
    context_object_name = 'object'
    template_name = 'tournamentfinder/generic_model_delete.html'
    success_url = reverse_lazy('list_directors')

class TournamentList(ListView):
    model = Tournament
    context_object_name = 'tournaments'
    template_name = 'tournamentfinder/list_tournaments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_in'] = get_login_status(self.request)
        return context

class TournamentCreate(LoginRequiredMixin, CreateView):
    model = Tournament
    form_class = TournamentCreateForm
    template_name = 'tournamentfinder/generic_model_create.html'
    success_url = reverse_lazy('list_tournaments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Tournament'
        return context

class TournamentUpdate(LoginRequiredMixin, UpdateView):
    model = Tournament
    form_class = TournamentUpdateForm
    context_object_name = 'object'
    template_name = 'tournamentfinder/generic_model_update.html'
    success_url = reverse_lazy('list_tournaments')

class TournamentDelete(LoginRequiredMixin, DeleteView):
    model = Tournament
    context_object_name = 'object'
    template_name = 'tournamentfinder/generic_model_delete.html'
    success_url = reverse_lazy('list_tournaments')
