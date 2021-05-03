from django.contrib import admin
from django.urls import path
import dmapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dmapp.views.home, name='home'),
    path('list/', dmapp.views.dm_list, name='list'),
    path('create/', dmapp.views.create, name='create'),
    path('detail/<int:id>', dmapp.views.detail, name='detail'),
]
