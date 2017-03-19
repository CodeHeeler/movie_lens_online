from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# from django.template import loader
# from django.db.models import Count, Avg
# from .models import Movies, Rater, Ratings


def index(request):
    return render(request, 'recommender/index.html')


def movie_detail(request, movie_id):
    return HttpResponse("You're looking at movie %s." % movie_id)


def rate_detail(request, rater_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % rater_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
