from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    # 'user',
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'display', 'order', 'created', 'updated']
    list_filter = ['display', 'created', 'updated', 'category']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stock', 'display', 'order']


admin.site.register(Product, ProductAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Type, TypeAdmin)

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Size, SizeAdmin)

class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Attribute, AttributeAdmin)

class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Facility, FacilityAdmin)

class RuleAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Rule, RuleAdmin)

class SafetyAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Safety, SafetyAdmin)