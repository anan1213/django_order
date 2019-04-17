from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pdf'


urlpatterns = [
    path('', views.ListPdfView.as_view(), name='index'),
    path('create/', views.CreatePdfView.as_view(), name='create_pdf'),
    #path('delete/', views.deleteUrl, name='delete_url'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
