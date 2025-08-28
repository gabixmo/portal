from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug',)
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'ativo', 'estoque', 'criado_em')
    list_filter = ('ativo', 'categoria', 'estoque', 'criado_em')
    search_fields = ('nome', 'descricao', 'criado_em')
    date_hierarchy = 'criado_em'
    autocomplete_fields = ('categoria',)
    prepupulated_fields = {'slug': ('nome'),}