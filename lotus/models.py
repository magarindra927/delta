from django.db import models

# Create your models here.

class Lod(models.Model):
    name=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Info(models.Model):
    lod=models.ForeignKey(Lod, on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, unique=True)
    
    description=models.TextField()
    is_published=models.BooleanField(default=True)
    photo=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    views=models.IntegerField(default=0)

    def __str__(self):
        return self.title