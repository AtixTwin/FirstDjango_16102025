from django.shortcuts import render, get_object_or_404
from .models import Item
from django.http import HttpResponse
from django.http import HttpResponseNotFound

IMAGE_URLS = {
    1: "https://room78.net/wp-content/uploads/2022/06/gukb4qk....jpg",
    2: "https://img.joomcdn.net/02aaa28e02ea36a98dff0d50629eb6b7abb303a2_original.jpeg",
    3: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoB49TGPkGMQeN5BA4Fmv3NH9ZNVTnGJLsfg&s",
    4: "https://marr.ru/upload/resize_cache/webp/iblock/21b/adaj3t6awf7l5bpts8j9tpaedis6wqkc.webp",
    5: "https://vintageleder.ua/upload/products/img/large/kepka_huliganka_kozhanaya_muzhskaya_gatsby_art_23_vintage_leder.jpg",
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5, "img_url":"https://room78.net/wp-content/uploads/2022/06/gukb4qkvixirslxpsa6fcuk9u7qmvmsnpgj3yl1buo2mnrpttbvzatyzvgq5mv923kp-n16bpgtgiwa6enuhsi0k.jpg"},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2, "img_url":"https://img.joomcdn.net/02aaa28e02ea36a98dff0d50629eb6b7abb303a2_original.jpeg"},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12, "img_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoB49TGPkGMQeN5BA4Fmv3NH9ZNVTnGJLsfg&s"},
   {"id": 7, "name": "Картофель фри" ,"quantity":0, "img_url":"https://marr.ru/upload/resize_cache/webp/iblock/21b/adaj3t6awf7l5bpts8j9tpaedis6wqkc.webp"},
   {"id": 8, "name": "Кепка" ,"quantity":124, "img_url":"https://vintageleder.ua/upload/products/img/large/kepka_huliganka_kozhanaya_muzhskaya_gatsby_art_23_vintage_leder.jpg"},
]

def main(request):
    context = {
        "name": "Алексеев Антон Юрьевич",
        "email": "atix.wind@gmail.com"
    }
    return render(request, "index.html", context)

def about(request):
    
    author = {
        "name": "Антон",
        "midle_name": "Юрьевич",
        "last_name": "Алексеев",
        "contact_number": "+7 (926) 655-52-20",
        "email": "atix.wind@gmail.com"
    }
    
    context = {
        "author": author,
    }

    return render(request, "about.html", context)

def item_page(request, id: int):

    """ TODO: get item by id from db <-- DONE!!"""

    item = get_object_or_404(Item, pk=id)
    image_url = IMAGE_URLS.get(item.id)    
    return render(request, "item_page.html", {"item": item, "image_url": image_url})
    

def items_def(request):
    
    """ TODO: get all items from db <-- DONE!!"""

    items_qs = Item.objects.all().order_by('id')
    return render(request, "items_list.html", {"SKU_List": items_qs})
