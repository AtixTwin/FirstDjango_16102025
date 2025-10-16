from django.shortcuts import render
from django.http import HttpResponse

author = {
    'name': "Антон",
    'midle_name': "Юрьевич",
    'last_name': "Алексеев",
    'contact_number': "+7 (926) 655-52-20",
    'email': "atix.wind@gmail.com"
}

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