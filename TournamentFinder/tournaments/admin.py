from django.contrib import admin

from .models import Member, BowlingCenter, TournamentDirector, Tournament

# Register your models here.
admin.site.register(Member)
admin.site.register(BowlingCenter)
admin.site.register(TournamentDirector)
admin.site.register(Tournament)