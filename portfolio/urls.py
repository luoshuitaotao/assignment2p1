from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'portfolio'
urlpatterns = [
    path ('', views.home, name='home'),
    url (r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path ('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path ('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path ('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path ('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('investment_list', views.investment_list, name='investment_list'),
    path ('investment/create/', views.investment_new, name='investment_new'),
    path ('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path ('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),
    path ('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    #path('pdf_detail', views.pdf_detail.as_view(),),
    #path ('detail/<int:id>', views.investment_list, name='detail'),
    #path ('<int:pk>', views.pdfDetail.as_view(),),
    #path ('pdfDetail', views.pdfDetaill, name='pdfDetail'),
    #path('deatil/<int:id>', views.detail_page,name="detail"),
    path ('investment/download/', views.investments_download,name='investments_download'),
    path ('mutual_list', views.mutual_list, name='mutual_list'),
    path ('mutual/create/', views.mutual_new, name='mutual_new'),
    path ('mutual/<int:pk>/edit/', views.mutual_edit, name='mutual_edit'),
    path ('mutual/<int:pk>/delete/', views.mutual_delete, name='mutual_delete'),
]