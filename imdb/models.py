from django.db import models

# Create your models here.

class Rating(models.Model):
    movie_name=models.CharField(primary_key=True,max_length=300)
    movie_rating = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.movie_name+self.movie_rating
    
class Cast(models.Model):
    movie_name=models.CharField(primary_key=True,max_length=300)
    movie_rating = models.CharField(max_length=10,null=True)
    cast1 = models.CharField(max_length=100,null=True)
    cast2 = models.CharField(max_length=100,null=True)
    cast3 = models.CharField(max_length=100,null=True)
    cast4 = models.CharField(max_length=100,null=True)
    cast5 = models.CharField(max_length=100,null=True)
    cast6 = models.CharField(max_length=100,null=True)
    cast7 = models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.movie_name)+str(self.movie_rating)+str(self.cast1)+(self.cast2)+str(self.cast3)+str(self.cast4)+str(self.cast5)+str(self.cast6)+str(self.cast7)

class Storyline(models.Model):
    movie_name=models.CharField(primary_key=True,max_length=300)
    movie_rating = models.CharField(max_length=10,null=True)
    movie_story=models.CharField(max_length=5000,null=True)
    def __str__(self):
        return str(self.movie_name)+str(self.movie_rating)+str(self.movie_story)
