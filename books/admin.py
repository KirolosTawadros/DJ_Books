from django.contrib import admin

# Register your models here.
from .models import Book,Author,Review

class ProductAdmin(admin.ModelAdmin):
    list_display=['title']
    
    


admin.site.register(Book,ProductAdmin)    
admin.site.register(Author)    
admin.site.register(Review)    