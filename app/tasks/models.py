from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class UserGym(models.Model) :
    PLAN = (('mensal', 'Mensal'), ('semestral', 'Semestral'), ('a', 'Anual'))
    FLAGS = (('visa', 'Visa'), ('itau', 'Itaú'), ('caixa', 'Caixa'), ('santander', 'Santander'), ('bbrasil', 'BancoDoBrasil'), ('bradesco', 'bradesco'), ('inter', 'BancoInter'), ('nubank','Nubank'))
    
    fullname = models.CharField(max_length=255, null=True)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    flag = models.CharField(max_length=10, choices=FLAGS) 
    card_number = models.CharField(max_length=16)
    card_name = models.CharField(max_length=255)
    medic_description = models.TextField()
    type_plan = models.CharField(max_length=10, choices=PLAN)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

