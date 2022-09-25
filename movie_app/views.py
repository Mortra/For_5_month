from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *



#вьюшка список директоров
@api_view(['GET'])#Скрывает вьюшки
def directors_list(request):
    directors = Director.objects.all()
    data = DirectorlistSerializer(directors, many=True).data
    return Response(data=data)


#вьюшка список фильмов
@api_view(['GET'])
def movies_list(request):
    movies = Movie.objects.all()
    data = MovielistSerializer(movies, many=True).data
    return Response(data=data)


#вьюшка обзор
@api_view(['GET'])
def reviews_list(request):
    reviews = Review.objects.all()
    data = ReviewlistSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movies_with_reviews(request):
    movies = Movie.objects.all()
    # movies = Movie.objects.filter().annotate(
    #     middle_star=models.Sum(models.F('rating__star')) * models.Count(models.F('rating')))
    data = MoviewithReviewsSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def one_movie_view(request, id):
    try:
        movie = {
            'title': Movie.objects.get(id=id).title,
            'duration': f"{Movie.objects.get(id=id).duration} мин",
            'description': Movie.objects.get(id=id).description,
            'director': Movie.objects.get(id=id).director.name,
            'like': Movie.objects.get(id=id).rev
        }
        return Response(data=movie)
    except Movie.DoesNotExist:
        return Response(f'Фильм №{id} не найдено')



@api_view(['GET'])
def one_director_view(request, id):
    try:
        director = {
            'name': Director.objects.get(id=id).name
        }
        return Response(data=director)
    except Director.DoesNotExist:
        return Response(f'Директор №{id} еще не зарегистрирован')



@api_view(['GET'])
def one_review_view(request, id):
    try:
        review = {
            'text': Review.objects.get(id=id).text,
            'movie': Review.objects.get(id=id).movie,
        }
        return Response(data=review)
    except Review.DoesNotExist:
        return Response(f'Обзор №{id} не найдено')

