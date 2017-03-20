from django.conf.urls import url

from . import views

urlpatterns = [
    # GET /recommend_app/ -> top 20
    url(r'^$', views.index, name='index'),
    # GET /recommend_app/movie_id/ -> show the movie and its avg_rating
    url(r'^(?P<movie_id>[0-9]+)/$', views.movie, name='movie'),
    # # GET /recommend_app/movie_id/rater_id/
    # # -> show the raters name and rating for movie
    url(r'^rater/(?P<rater_id>[0-9]+)/$', views.rater, name='rater'),
    # url(r'^(?P<movie_id>[0-9]+)/rate/$', views.rate, name='rate'),
]
