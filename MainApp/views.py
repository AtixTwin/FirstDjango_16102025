from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Алексеев А.Ю.</i>
    """
    return HttpResponse(text)