from django.urls import path
from app.views import home, history

urlpatterns = [
    path('', home, name='home'),
    path('history/', history, name='history'),
]
