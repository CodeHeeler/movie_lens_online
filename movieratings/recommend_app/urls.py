from django.conf.urls import url

from . import views

urlpatterns = [
    # GET /polls/
    url(r'^$', views.index, name='index'),
    # GET /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # GET /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
]
