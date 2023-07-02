from django.urls import path
from .views import login

app_name = 'seguridad'

urlpatterns = [
    path('', login , name="login")
]
