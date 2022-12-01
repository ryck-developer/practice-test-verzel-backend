from django.urls import path, include

urlpatterns = [
    path('velist', include('rest_framework.urls')),
]
