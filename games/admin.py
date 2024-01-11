from django.contrib import admin
from .models import Game, Platform, Genre

# Register your models here.

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Genre)
