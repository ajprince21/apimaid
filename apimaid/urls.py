
from django.contrib import admin
from django.urls import path
from maidapp.views import maidListView
urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/maid', maidListView),
]
