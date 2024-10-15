#from django.shortcuts import render
from django.http import Http404
# Create your views here.
#from django.http import HttpResponse
# Create your views here.
#def index(request):
  #  return HttpResponse("You're at the movies index.")
from django.shortcuts import render
# i changes models from .models
from .models import Movie

def index(request):
    newest_movies = Movie.objects.order_by('-release_date')[:15]
    context = {'newest_movies': newest_movies}
    return render(request, 'movies/index.html', context)
    
def show(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/show.html', {'movie': movie})