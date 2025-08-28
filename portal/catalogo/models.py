from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=120, unique=True, db_index=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return f'{self.nome}'
    

class Produto(models.Model):
    nome = models.CharField(max_length=180, db_index=True)
    slug = models.SlugField(max_length=120, db_index=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    estoque = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produto')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['ativo']),
            models.Index(fields=['criado_em']),
        ]

        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.nome}'