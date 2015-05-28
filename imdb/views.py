from django.shortcuts import render
from imdb.models import Rating,Cast,Storyline
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    return render(request,'home.html',{})

def home(request):
    return render(request,'home.html',{})

def rating(request):
    dlist=[]
    rate= [i for i in Rating.objects.order_by('-movie_rating').all()]
    i=1
    for rating in rate:
        dic = {'id':i,'movie_name': rating.movie_name,'movie_rating':rating.movie_rating}
        dlist.append(dic)
        i+=1
    ddic={'rrate':dlist}
    return render(request,'imdb/rating.html',ddic)

def cast(request):
    ccast=[]
    cast= [i for i in Cast.objects.order_by('-movie_rating').all()]
    i=1
    for cast_obj in cast:
        dic = {'id':i,'movie_name': cast_obj.movie_name,'movie_rating':cast_obj.movie_rating,'cast1':cast_obj.cast1,'cast2':cast_obj.cast2,'cast3':cast_obj.cast3,'cast4':cast_obj.cast4,'cast5':cast_obj.cast5,'cast6':cast_obj.cast6,'cast7':cast_obj.cast7}
        ccast.append(dic)
        i+=1
    ddic={'cast':ccast}
    return render(request,'imdb/cast.html',ddic)

def storyline(request):
    sstory=[]
    storyline= [i for i in Storyline.objects.order_by('-movie_rating').all()]
    i=1
    for story_obj in storyline:
        dic = {'id':i,'movie_name':story_obj.movie_name,'movie_rating':story_obj.movie_rating,'movie_story':story_obj.movie_story}
        sstory.append(dic)
        i+=1
    sdic={'storyline':sstory}
    return render(request,'imdb/storyline.html',sdic)
