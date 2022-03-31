from ast import Delete
from pickle import GET
from typing import List
from django.shortcuts import render

from crudProduto.entity import Produto

produto1 = Produto(id =1 , nome="Relógio", valor=30.20 , quantidade=2, descricao='Relógio Adidas')
produto2 = Produto(2, "Smart watch", "Rélógio Bolado", 4, 10.70)
produto3 = Produto(3, 'Relógio do Vovô', "Até meu avô tem", 5, 189.90)
produtos = [produto1, produto2, produto3]

def produto(request):
    return render(request,"index.html",{"lista":produtos})


def ver_produto(request, id:int):
    for produto in produtos:
        if produto.get_id() == id:
            return render(request,"produtos.html",{"produto":produto})

def adicionar_produto(request):
    if request.method == "GET":
        return render(request, "adicionar.html")
    elif request.method == "POST":
        produto = Produto(len(produtos)+1,
            request.POST.get('nome', None),
            request.POST.get('descricao', None),
            request.POST.get('valor', None),
            request.POST.get('quantidade', None)
        )
        produtos.append(produto)
        return render(request,"index.html",{"lista":produtos})

def deletar_produto(request, id):
    if request.method == "DELETE":
        for produto in produtos:
            if produto.get_id() == int(id):
                produtos.remove(produto)
                return render(request,"index.html",{"lista":produtos})
        return render(request,"index.html",{"lista":produtos,"erro":"Produto não encontrado." })