from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bowling-centers', views.BowlingCenterListView.as_view(), name='bowling-centers'),
    path('tournament-directors', views.TournamentDirectorListView.as_view(), name='tournament_directors'),
]