from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/<str:name>/', views.welcome, name='welcome'),
]
