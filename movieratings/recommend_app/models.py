from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Rater(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)

    def __repr__(self):
        return "{} - {}({})".format(self.name, self.age, self.gender)

    def __str__(self):
        return self.__repr__()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Rater.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Movies(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.CharField(max_length=15)
    video_release = models.CharField(max_length=15)
    imdb = models.URLField(max_length=200)

    def __repr__(self):
        return "{}: {}".format(self.title, self.release_date)

    def __str__(self):
        return self.__repr__()


class Ratings(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    rating = models.IntegerField()
    rate_date = models.IntegerField()

    def __repr__(self):
        return "{} - {}: ({}/5)".format(self.movie.title, self.rater.name, self.rating)

    def __str__(self):
        return self.__repr__()


class Genre(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    genres = models.TextField()

    def __repr__(self):
        return "{} - {}".format(self.movie.title, self.genres)

    def __str__(self):
        return self.__repr__()
