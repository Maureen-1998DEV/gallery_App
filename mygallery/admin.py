from django.contrib import admin

from mygallery.models import Image,categories,Location

# Register your models here.
admin.site.register(Image)
admin.site.register(categories)
admin.site.register(Location)