from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


#Директор
class Director(models.Model):
    director_name = models.CharField(verbose_name='Имя', max_length=50)
    film = models.ManyToManyField(to='Movie', related_name='cinema')

    def __str__(self):
        return self.director_name

    @property
    def cinema_name(self):
        return [cinema.title for cinema in self.film.all()]

    class Meta:
        verbose_name_plural = 'Режисеры'#относиться только к множ-чис
        verbose_name = 'Режисер'


#Фильмы
class Movie(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100, blank=False, null=False)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    duration = models.IntegerField(verbose_name="Продолжительность")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name='Режисер', null=True)
    reviews = models.ManyToManyField(to='Review', related_name='like', null=True)

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        try:
            return self.director.director_name
        except:
            return ''

    @property
    def reviews_text(self):
        return [review.text for review in self.reviews.all()]

    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'


#Обзор
class Review(models.Model):
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм', null=True, related_name='rating')
    star = models.IntegerField(validators=[MaxValueValidator(5),
                                           MinValueValidator(1)], null=True, blank=True,)

    def __str__(self):
        return self.text

    @property
    def movie_name(self):
        try:
            return self.movie.title
        except:
            return ''


    class Meta:
        verbose_name_plural = 'Обзоры'
        verbose_name = 'Обзор'

