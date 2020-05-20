from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.BillList.as_view()),
    path('<int:pk>/', views.BillDetail.as_view()),
    path('<int:pk>/products/', views.BillProductList.as_view()),
]