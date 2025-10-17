from django.shortcuts import render
from django.http import HttpResponse

author = {
    'name': "Антон",
    'midle_name': "Юрьевич",
    'last_name': "Алексеев",
    'contact_number': "+7 (926) 655-52-20",
    'email': "atix.wind@gmail.com"
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5, "img-url":"https://room78.net/wp-content/uploads/2022/06/gukb4qkvixirslxpsa6fcuk9u7qmvmsnpgj3yl1buo2mnrpttbvzatyzvgq5mv923kp-n16bpgtgiwa6enuhsi0k.jpg"},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2, "img-url":"https://img.joomcdn.net/02aaa28e02ea36a98dff0d50629eb6b7abb303a2_original.jpeg"},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12, "img-url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoB49TGPkGMQeN5BA4Fmv3NH9ZNVTnGJLsfg&s"},
   {"id": 7, "name": "Картофель фри" ,"quantity":0, "img-url":"https://marr.ru/upload/resize_cache/webp/iblock/21b/adaj3t6awf7l5bpts8j9tpaedis6wqkc.webp"},
   {"id": 8, "name": "Кепка" ,"quantity":124, "img-url":"https://vintageleder.ua/upload/products/img/large/kepka_huliganka_kozhanaya_muzhskaya_gatsby_art_23_vintage_leder.jpg"},
]


def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Алексеев А.Ю.</i>
    """
    return HttpResponse(text)

def about(request):
    text = f"""
    <h1>"Автор проекта"</h1>
    <small>Имя:</small> <strong>{author['name']}</strong> <br>
    <small>Отчество:</small> <strong>{author['midle_name']}</strong> <br>
    <small>Фамилия:</small> <strong>{author['last_name']}</strong> <br>
    <small>Телефон:</small> <strong>{author['contact_number']}</strong> <br>
    <small>Почта:</small> <strong>{author['email']}</strong>
    """
    return HttpResponse(text)

def item(request, id: int):

    if id > 5:
        
        url_not_found = "https://elements-resized.envatousercontent.com/elements-cover-images/41ce1856-ce64-47eb-9cc9-d50c75ba936b?w=2038&cf_fit=scale-down&q=85&format=auto&s=c54070f24dcaa94cc414ea7eca94fe5c7ba4b8e8f8878ff1eb64517021daf0a6"  
        
        text = f"""
        <!doctype html>
        <html lang="ru">
        <meta charset="utf-8">
        <title>Товар не найден</title>
        <h1>Tовар с ID #{id} не найден</h1>
        <style>
            .img-fixed {{
                width: 360px;       
                height: 360px;      
                object-fit: cover;  
                object-position: center; 
                border-radius: 10px; 
            }}
            </style>
        <img class="img-fixed" src="{url_not_found}" alt="NOT FOUND">
        <br>
        <br>
        <a href="http://127.0.0.1:8000/items/">Назад к списку товаров</a>
        """
    
    else:
        text = f"""
        <!doctype html>
        <html lang="ru">
        <meta charset="utf-8">
        <h1>Товар ID #{id}</h1>
        <h2>{items[id-1]['name']}</h2>
        <head>
            <title>{items[id-1]['name']}</title>
            <style>
            .img-fixed {{
                width: 360px;       
                height: 360px;      
                object-fit: cover;  
                object-position: center; 
                border-radius: 10px; 
            }}
            </style>
        </head>
        <body>
            <img class="img-fixed" src="{items[id-1]['img-url']}" alt="{items[id-1]['name']}">
        </body> 
        <br>
        <br>
        Всего на складе: <strong>{items[id-1]['quantity']}</strong>
        <br>
        <br>
        <a href="http://127.0.0.1:8000/items/">Назад к списку товаров</a>
        </html>
        """
       
    return HttpResponse(text)

def items_def(request):

    text = f"""
    <!doctype html>
    <html lang="ru">
    <meta charset="utf-8">
    <title>Список товаров</title>
    <h1>Список товаров</h1>
    """
    SKU_List = ""
    
    for SKU_index in range(len(items)):
        SKU_Text = f"""
        №{SKU_index+1} <a href="http://127.0.0.1:8000/item/{SKU_index+1}"><strong>{items[SKU_index]['name']}</strong></a><br>
        <hr style="border:none;height:1px;background:#ddd;margin:8px 0">
        """
        SKU_List += SKU_Text

    text += SKU_List    

    return HttpResponse(text)
