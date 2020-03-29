from django.urls import path

from . import views

urlpatterns = [
    #path('/', views.login, name='login'),

    # Testando passagem por paramêtro.
    path('teste/<str:name>', views.testeParam),

    # Lista de Usuários.
    path('lista/', views.listUsers),

    # Acesso ao usuário.
    path('lista/user/<int:id>', views.userView, name="user-view"),
    
    # Adicionar usuário.
    path('lista/addUser/', views.addUser, name="add-user-view"),

    # Editar um usuário.
    path('lista/editUser/<int:id>', views.editUser, name="edit-a-user-view"),

    # Excluir um usuário.
    path('lista/deleteUser/<int:id>', views.deleteUser, name="delete-a-user-view"),
    
]
