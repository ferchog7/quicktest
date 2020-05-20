from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ClientList.as_view()),
    path('<int:pk>/', views.ClientDetail.as_view()),
    path('report/', views.ClientReportList.as_view()),
]