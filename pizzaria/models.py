from django.db import models

PEDIDO_CHOICES = (
    ('Pizza calabresa R$ 50,00', 'Pizza calabresa R$ 50,00'),
    ('Pizza Portuguesa R$ 50,00', 'Pizza Portuguesa R$ 50,00'),
    ('Pizza de Muçarela R$ 50,00', 'Pizza de Muçarela R$ 50,00'),
    ('Pizza Marguerita R$ 50,00' , 'Pizza Marguerita R$ 50,00'),
    ('Pizza Quatro queijos R$ 50,00', 'Pizza Quatro queijos R$ 50,00')
)   


class Cliente(models.Model):
    nome = models.CharField(
        verbose_name="Nome completo",
        max_length=100,
    )
    telefone = models.CharField(
        verbose_name="Telefone", 
        max_length=20
    )
    bairro = models.CharField(
        verbose_name="Bairro",
        max_length=100
    )
    rua = models.CharField(
        verbose_name="Rua",
        max_length=100
    )
    numero = models.DecimalField(
        verbose_name='Número',
        max_digits=10,
        decimal_places=0
    )
    complemento = models.CharField(
        verbose_name="Complemento",
        max_length=100,
        blank=True
    )
    pizza = models.CharField(
        max_length=100,
        verbose_name='Escolha seu sabor', 
        choices=PEDIDO_CHOICES
    )
    


