from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bowling-centers', views.BowlingCenterList.as_view(), name='bowling-centers'),
    path('tournament-directors', views.TournamentDirectorList.as_view(), name='tournament_directors'),
    path('tournaments', views.TournamentList.as_view(), name='tournaments'),
]