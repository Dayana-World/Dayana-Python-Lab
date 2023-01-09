from django.contrib import admin
from . import  models

# Register your models here.

admin.site.register(models.Article)
admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Massage)
admin.site.register(models.Like)