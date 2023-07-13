from django.shortcuts import render
from testapp.forms import MovieModel
from testapp.forms import Movie

# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')
def addmovie_view(request):
    form=MovieModel()
    if request.method=='POST':
        form=MovieModel(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index_view(request)
    return render(request,'testapp/addmovie.html',{'form':form})
def listmovie_view(request):
    movie_list=Movie.objects.all()
    return render(request,'testapp/listmovie.html',{'movie_list':movie_list})