from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_safe
from django.core import serializers
from django.core.paginator import Paginator
from .models import Movie
from django.http import HttpResponse, JsonResponse

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    movie_num_in_page = 10
    page_num = Movie.objects.count() // movie_num_in_page + 1
    paginator = Paginator(movies, movie_num_in_page)

    cur_page = request.GET.get('page')
    page_obj = paginator.get_page(cur_page)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if int(cur_page) < page_num:
            data = serializers.serialize('json', page_obj)
            return HttpResponse(data, content_type='applictaion/json')
        else:
            context = {

            }
        return HttpResponse()
    else:
        context = {
            'movies': page_obj,
        }
        return render(request, 'movies/index.html', context)



@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    top_movies = Movie.objects.order_by('-vote_average', 'vote_count')[:10]
    context = {
        'top_movies': top_movies,
    }
    return render(request, 'movies/recommended.html', context)