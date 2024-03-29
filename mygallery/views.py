from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Location,categories

# Create your views here.
def main_gallery(request):
    images = Image.all_images()
    locations = Location.objects.all()
    return render(request, 'index.html', {"images":images,"locations":locations})


def single(request,category_name,image_id):

    title = 'Image'
    locations = Location.objects.all()
    # category = Category.get_category_id(id = image_category)
    categories = Image.objects.filter(image_category__name = category_name)
    try:
        image = Image.objects.get(id = image_id)
    except:
        raise Http404()
    return render(request,"single.html",{'title':title,"image":image, "locations":locations, "categories":categories})



# def location(request,location):
#     locations = Location.objects.all()
#     selected_location = Location.objects.get(id = location)
#     images = Image.objects.filter(location = selected_location.id)
#     return render(request, 'location.html', {"location":selected_location,"locations":locations,"images":images})

def search_location(request):
    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        category = Location.objects.filter (name = search_term)
        print()
        searched_images = Image.filter_by_location(category[0])
        print(searched_images)
        messages = f'{search_term}'
        return render(request,'location.html',{"images":searched_images,'messages':messages})
    else :
        messages="That location does not exist"
        return render(request,'location.html',{'messages':messages})
 

def search(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        category = categories.objects.filter (name = search_term)
        print(category)
        searched_images = Image.search_by_category(category[0])
        print(searched_images)
        messages = f'{search_term}'
        return render(request,'search.html',{"images":searched_images,"category":search_term,'messages':messages})
    else :
        messages="That Category does not exist"
        return render(request,'search.html',{'messages':messages})

