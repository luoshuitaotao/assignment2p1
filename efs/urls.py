from django.contrib import admin
from django.conf.urls import  include,url
from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path ('accounts/', include ('django.contrib.auth.urls')),

]

