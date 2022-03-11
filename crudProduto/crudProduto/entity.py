class Produto():
    
    def __init__(self,id:int,nome:str, descricao:str, quantidade: int, valor: float):
        self.id = id 
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor = valor

    
    def get_id(self):
        return self.id 

    def set_id(self,id):
        self.id = id
        
    def get_nome(self):
        return self.nome

    def set_nome(self,nome):
        self.nome = nome

    def get_descricao(self):
        return self.descricao
    
    def set_descricao(self,descricao):
        self.descricao = descricao

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self,quantidade):
        self.quantidade = quantidade
    
    def get_valor(self):
        return self.valor
    
    def set_valor(self,valor):
        self.valor = valor
    


