from django.contrib import admin
from idols.models import *

# Register your models here.

@admin.register(MurtiCategory)
class MurtiCategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(Murti)
class MurtiAdmin(admin.ModelAdmin):
	pass

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
	pass

@admin.register(MaterialCategory)
class MaterialCategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(MurtiTag)
class MurtiTagAdmin(admin.ModelAdmin):
	pass

@admin.register(MurtiImage)
class MurtiImageAdmin(admin.ModelAdmin):
	fields = ( 'image_tag', )
	readonly_fields = ('image_tag',)
	list_display = ('idol_image', 'image_tag',)

@admin.register(MurtiStatus)
class MurtiStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
	pass

