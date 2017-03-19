from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Movies, Rater, Ratings

admin.site.register(Movies)
admin.site.register(Rater)
admin.site.register(Ratings)
