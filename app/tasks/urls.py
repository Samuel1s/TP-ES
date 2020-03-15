from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),

    # Testando passagem por paramêtro.
    path('teste/<str:name>', views.testeParam)
    
]
