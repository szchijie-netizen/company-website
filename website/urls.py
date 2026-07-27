from django.urls import path
from . import views

urlpatterns = [
    path('api/info/', views.CompanyInfoView.as_view(), name='company-info'),
    path('api/contact/', views.ContactCreateView.as_view(), name='contact-create'),
]
