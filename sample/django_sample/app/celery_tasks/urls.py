from django.urls import path

from .views import CeleryTestView

urlpatterns = [
    path('', CeleryTestView.as_view(), name='Test')
]
