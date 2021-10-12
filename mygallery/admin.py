from django.contrib import admin

from mygallery.models import Image,categories,Location

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)

admin.site.register(Image,ImageAdmin)
admin.site.register(categories)
admin.site.register(Location)