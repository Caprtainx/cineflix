from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

RATINGS = (
    ('1'),
    ('2'),
    ('3'),
    ('4'),
    ('5'),
    ('6'),
    ('7'),
    ('8'),
    ('9'),
    ('10'),
)

class Favorites(models.Model):
    imdbId = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.id})

class Movie(models.Model):
    imdbId = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    genres = models.CharField(max_length=200, null=True)
    awards = models.CharField(max_length=300, null=True)
    trailer = models.CharField(max_length=300, null=True)
    favorites = models.ManyToManyField(Favorites)
    rating = models.IntegerField(
        # choices=RATINGS,
        null=True
    )

    def __str__(self):
        return f'{self.title} ({self.id})'


class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        Movie, 
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True) 


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'Review for: {self.movie} ({self.id})'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=200, default='https://i.imgur.com/1t8xewY.png')
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} ({self.id})'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.id})

