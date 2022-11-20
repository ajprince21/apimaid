
from django.contrib import admin
from django.urls import path
from maidapp.views import MaidListView, MaidDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/maid', MaidListView.as_view()),
    path('api/maid/<int:pk>', MaidDetailView.as_view()),
]
