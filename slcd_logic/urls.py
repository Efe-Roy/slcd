from django.urls import path, include
from .views import licenses_list, licenses_detail

urlpatterns = [
    path('licenses/', licenses_list),
    path('licenses/<int:pk>', licenses_detail),
]

