from typing import List
from django.shortcuts import render

from crudProduto.entity import Produto

produto1 = Produto(id =1 , nome="Relógio", valor=30.20 , quantidade=2, descricao='Relógio Adidas')
produto2 = Produto(2, "Smart watch", "Rélógio Bolado", 4, 10.70)
produto3 = Produto(3, 'Relógio do Vovô', "Até meu avô tem", 5, 189.90)
produtos = [produto1, produto2, produto3]

def listaProduto(request):
    return render(request,"index.html",{"lista":produtos})