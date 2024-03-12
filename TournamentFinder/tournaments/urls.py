from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bowling-centers', views.BowlingCenterList.as_view(), name='list_bowling_centers'),
    path('bowling-centers/create', views.BowlingCenterCreate.as_view(), name='create_bowling_center'),
    path('bowling-center/update/<pk>', views.BowlingCenterUpdate.as_view(), name='update_bowling_center'),
    path('tournament-directors', views.TournamentDirectorList.as_view(), name='list_tournament_directors'),
    path('tournament-directors/create', views.TournamentDirectorCreate.as_view(), name='create_tournament_director'),
    path('tournament-directors/update/<pk>', views.TournamentDirectorUpdate.as_view(), name='update_tournament_director'),
    path('tournaments', views.TournamentList.as_view(), name='list_tournaments'),
    path('tournaments/create', views.TournamentCreate.as_view(), name='create_tournament'),
    path('tournaments/update/<pk>', views.TournamentUpdate.as_view(), name='update_tournament'),
]