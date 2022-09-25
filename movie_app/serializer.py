
from rest_framework import serializers
from .models import *


class ReviewsSerializer(serializers.ModelSerializer):#Чтобы вывести в модельке Movie text и star
    class Meta:
        model = Review
        fields = 'text star'.split()


class DirectorlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'director_name cinema_name'.split()


class ReviewlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'movie_name text star'.split()


class MovielistSerializer(serializers.ModelSerializer):
    # reviews = ReviewsSerializer(many=True)#Передаем наш Reviews сериалайзер если это М2М то many=True обьязательно
    reviews_stars = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title description duration director_name reviews_text reviews_stars'.split()

    def get_reviews_stars(self, obj_movie):
        return [review.star for review in obj_movie.reviews.all()]


class MoviewithReviewsSerializer(serializers.ModelSerializer):
    rai_stars = serializers.SerializerMethodField()
    # middle_star = serializers.FloatField()
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title reviews_text rai_stars middle_star'.split()

    def get_rai_stars(self, obj_movie):
        return [review.star for review in obj_movie.reviews.all()]

    def get_middle_star(self, obj_reviews):
        summ = 0
        for s in obj_reviews.reviews.all():
            summ += s.star
        return round(summ / obj_reviews.reviews.count(), 1) if obj_reviews.reviews.count() else 'No Rating'