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
    <h1>"Автор проекта:"</h1>
    <small>Имя:</small> {author['name']}
    <small>Отчество:</small> {author['midle_name']}
    <small>Фамилия:</small> {author['last_name']}
    <small>Телефон:</small> {author['contact_number']}
    <small>Почта:</small> {author['email']}
    """
    return HttpResponse(text)