from django.contrib import admin
from .models import Domain, Registrar, Cheapest, Price
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, Comment

# Register your models here.


class DomainAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',  'status', 'cate', 'popular',)

class RegistrarAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'name', 'url', 'rating')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'registrar', 'register', 'renewal', 'transfer')

admin.site.register(Domain, DomainAdmin)
admin.site.register(Registrar, RegistrarAdmin)
admin.site.register(Cheapest)
admin.site.register(Price, PriceAdmin)

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'tags')

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
