from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.consent, name='consent'),

    path('dashboard/' , views.dashboard_view , name = 'dashboard'),
    path('export/', export_to_excel, name='export_to_excel'),


    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
]
