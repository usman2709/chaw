from django.contrib import admin
# from .models import Category, Dish
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat_name', 'cat_image']
    list_editable = ['cat_name', 'cat_image']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = [ 'id','name', 'category_id','category', 'max','image', 'breakfast', 'special','lunch', 'dinner','drink','appetizer', 'dessert', 'price', 'min', 'in_stock', ]
    list_editable = ['special']

@admin.register(Showcase)
class ShowcaseAdmin(admin.ModelAdmin):
    list_display = ['id','show_image','show_name','show_txt']
    # list_editable = ['show_name','show_txt']


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Dish, DishAdmin)
