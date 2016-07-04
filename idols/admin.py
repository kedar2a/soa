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
    print("99999999999999999999999")
    pass
    # fields = ["image",]
    # list_display = ("image","image_img")

    # def image_img(self):
    #     if self.image:
    #         return u'<img src="%s" />' % self.image.url 
    #     else:
    #         return '(No image found)'
    # image_img.short_description = 'Thumb'
    # image_img.allow_tags = True

@admin.register(MurtiStatus)
class MurtiStatusAdmin(admin.ModelAdmin):
	pass

