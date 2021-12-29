from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('', include('backbone.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
