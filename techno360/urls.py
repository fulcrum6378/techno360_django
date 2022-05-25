from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('', include('backbone.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('library/', views.library, name='library'),
    path('lessons/', views.lessons, name='lessons'),
]
