from django.contrib import admin
from .models import Song,Artist,Rating
from django.db import models

# Register your models here.


class SongAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Song',{"fields":["Name",'Date_of_Release','artist','rating']})
        #('Artist',{'field':['artist','DOB'.'Bio']})

    ]

class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [

        ('Artist',{'fields':['artist','DOB','Bio']})

    ]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)