from django.contrib import admin
from .models import Category, FoodItem

class AutomateCategory(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('Category_name',)}
    list_display = ('Category_name', 'vendor', 'updated_at')
    search_fields = ('Category_name', 'vendor__vendor_name')
    
    
class FoodTemadmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('food_title',)}
    list_display = ('food_title', 'category','vendor' , 'price' , 'is_available', 'updated_at')
    search_fields = ('food_title', 'category__Category_name')
    list_filter = ('is_available',)
    
# Register your models here.
admin.site.register(Category, AutomateCategory)
admin.site.register(FoodItem, FoodTemadmin)
