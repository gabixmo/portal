from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Categoria, Produto
from django.core.paginator import Paginator


def produto(request, categoria_slug=None):
    
    qs = Produto.objects.select_related('categoria').filter(ativo=True)
    categoria_sel = None

    if categoria_slug:
        categoria_sel = get_object_or_404(Categoria, slug = categoria_slug)
        qs = qs.filter(categoria=categoria_sel)

    q = request.GET.get('q', '').strip()
    if q:
        qs = qs.filter(
            Q(nome__icontains=q) | Q(descricao__icontains=q) | Q(categoria__nome__icontains=q)
        )

    sort = request.GET.get('sort', 'recentes')
    if sort == 'preco_asc':
        qs = qs.order_by('preco', '-criado_em')
    elif sort == 'preco_desc':
        qs = qs.order_by('-preco', '-criado_em')
    else:
        qs = qs.order_by('-criado_em')

    paginator = Paginator(qs, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.order_by('nome')

    context = {
        'categoria_sel': categoria_sel,
        'categorias': categorias,
        'page_obj': page_obj,
        'q': q,
        'sort': sort
    }

    return render(request, 'catalogo/produtos.html', context)

def home(request):
    return render(request, 'catalogo/home.html')

def sobre(request):
    return render(request, 'catalogo/sobre.html')

def contato(request):
    return render (request, 'catalogo/contato.html')