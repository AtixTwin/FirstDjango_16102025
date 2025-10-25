from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name="home"),
    path('about/', views.about, name="about"),
    path("item/<int:id>/", views.item_page, name="item_page"),
    path("items/", views.items_def, name="items_list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
