from django.db import models
from cloudinary.models import CloudinaryField

class categories(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

class Meta:
    ordering = ['first_name']    


class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name


    @classmethod
    def filter_by_location(cls,search_id):
        images = cls.objects.filter(location = search_id)
        
        return images

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    categories = models.ForeignKey(categories,on_delete=models.CASCADE,default = 1)
    # image_url = models.ImageField(upload_to = 'images/',blank=True)
    image_url = CloudinaryField('image')

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_id):
        images = cls.objects.filter(categories = search_id)
        
        return images
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.get(id = id)
        return image

    @classmethod
    def filter_by_location(cls,search_term):
        location = Location.objects.get(name = search_term)
        images = cls.objects.filter(location = location)
        return images