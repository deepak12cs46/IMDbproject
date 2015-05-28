import sys
import os

your_djangoproject_home= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'imdbproject.settings'
import django
django.setup()

import urllib.request
import re
from imdb.models import Rating,Cast,Storyline

url='http://www.imdb.com/chart/top?ref_=nv_wl_img_3'
headhtmlfile=urllib.request.urlopen(url)
headhtmltext=str(headhtmlfile.read())
url_regex='<td class="posterColumn"><a href="(.+?)"'
url_pattern=re.compile(url_regex)
movie_url=re.findall(url_pattern,headhtmltext)
j=0 
while j<50:
    url='http://www.imdb.com'+movie_url[j]
    htmlfile = urllib.request.urlopen(url)
    htmltext=str(htmlfile.read())

    name_regex = '<title>(.+?)- IMDb</title>'
    name_pattern = re.compile(name_regex)
    movie_name = re.findall(name_pattern,htmltext)
    print(movie_name)

    rating_regex='<div class="titlePageSprite star-box-giga-star">(.+?) </div>'
    rating_pattern = re.compile(rating_regex)
    movie_rating = re.findall(rating_pattern,htmltext)
    print (movie_rating)
                            
    rate=Rating()
    rate.movie_name=movie_name
    rate.movie_rating=movie_rating
    rate.save()

    cast_regex='<span class="itemprop" itemprop="name">(.+?)</span>'
    cast_pattern = re.compile(cast_regex)
    cast_name= re.findall(cast_pattern,htmltext)
    cast=Cast()
    cast.movie_name=movie_name
    cast.movie_rating=movie_rating
    cast.cast1=cast_name[7]
    cast.cast2=cast_name[8]
    cast.cast3=cast_name[9]
    cast.cast4=cast_name[10]
    cast.cast5=cast_name[11]
    cast.cast6=cast_name[12]
    cast.cast7=cast_name[13]
    cast.save()

    storyline_regex='<div class="inline canwrap" itemprop="description">[^.]*<p>(.+?)<em class="nobr">'
    storyline_pattern=re.compile(storyline_regex)
    movie_storyline=re.findall(storyline_pattern,htmltext)
    #print(movie_storyline)
    story=Storyline()
    story.movie_name=movie_name
    story.movie_rating=movie_rating
    story.movie_story=movie_storyline
    story.save()
    j+=1
