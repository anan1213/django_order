from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'url'

urlpatterns = [
    path('', views.IndexViewSubclass.as_view(), name='index'),
    path('detail/<str:get_name>/', views.IndexViewUrl.as_view(), name='index2'),
    path('create/', views.CreateViewUrl.as_view(), name='create_url'),
    path('create/category/', views.CreateViewSubclass.as_view(), name='create_subclass'),
    path('delete_url/', views.deleteUrl, name='delete_url'),
    path('delete_subclass/', views.deleteSubclass, name='delete_subclass'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
