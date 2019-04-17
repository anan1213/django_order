from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'book'


urlpatterns = [
    path('', views.ListImageView.as_view(), name='index'),
    path('create/', views.CreateImageView.as_view(), name='create_book'),
    path('delete_url/', views.delete_book, name='delete_book'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
