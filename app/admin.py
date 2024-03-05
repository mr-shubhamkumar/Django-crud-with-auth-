from django.contrib import admin
from .models import (
    Product,
    Category,
    SubCategory,
)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','cat_name']


@admin.register(SubCategory)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','subcat_name', 'cat' ]

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'discription', 'image', 'cat', 'subcat']


