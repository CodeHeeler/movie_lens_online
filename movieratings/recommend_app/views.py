from django.shortcuts import render
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
from django.db.models import Count, Avg
from recommend_app.models import Movies, Rater  # , Ratings


def index(request):
    top = Movies.objects.annotate(avg=Avg('ratings'), rate_count=Count('ratings')).order_by('-rate_count', 'avg')[:20]

    return render(request, 'recommend_app/index.html', {'top20': top})


def movie(request, movie_id):
    m = get_object_or_404(Movies, pk=movie_id)
    avg_rating = m.ratings_set.aggregate(Avg('rating'))['rating__avg']
    count = m.ratings_set.aggregate(Count('rating'))['rating__count']
    all_movie_rating = m.ratings_set.all().order_by('rate_date')

    return render(request, 'recommend_app/movie.html', {'m': m, 'avg_rating': round(avg_rating, 2), 'all_movie_rating': all_movie_rating, 'count': count})


def rater(request, rater_id):
    u = get_object_or_404(Rater, pk=rater_id)
    movies_reviewed = u.ratings_set.aggregate(Count('rating'))['rating__count']
    top = u.ratings_set.order_by('-rating', 'rate_date')
    return render(request, 'recommend_app/rater.html', {'u': u, 'movies_reviewed': movies_reviewed, 'top10': top})

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
