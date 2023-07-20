from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Lod)
class LodAdmin(admin.ModelAdmin):
    list_display=['id','name','slug']
    prepopulated_fields={'slug':('name',)}

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display=['id','title','lod','created_at','updated_at','is_published','photo']
    search_fields=['title','content']
    list_editable=['is_published']
    prepopulated_fields={'slug':('title',)}
