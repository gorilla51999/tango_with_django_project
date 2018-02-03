from django.contrib import admin
<<<<<<< HEAD
from rango.models import Category, Page
#from .models import Choice, Question



class PageAdmin(admin.ModelAdmin):
   list_display = ('title','category','url')
class CategoryAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug':('name',)}
#admin.site.register(Choice)
#admin.site.register(Category)
admin.site.register(Page,PageAdmin)
admin.site.register(Category,CategoryAdmin)

# Register your models here.
#admin.site.register()
=======

# Register your models here.
>>>>>>> 007098d90f8d7150dd6e76a93cba8f4c055e7ee9
