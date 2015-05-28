from django.contrib import admin
from .models import Rating,Cast,Storyline

class RatingAdmin(admin.ModelAdmin):
    list_display=('movie_name','movie_rating')
admin.site.register(Rating,RatingAdmin)

class CastAdmin(admin.ModelAdmin):
    list_display = ('movie_name','movie_rating', 'cast1','cast2','cast3','cast4','cast5','cast6','cast7')
admin.site.register(Cast,CastAdmin)

class StorylineAdmin(admin.ModelAdmin):
    list_display = ('movie_name','movie_rating','movie_story')
admin.site.register(Storyline,StorylineAdmin)
