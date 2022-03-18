class Produto():
    
    def __init__(self,id:int,nome:str, descricao:str, quantidade: int, valor: float):
        self._id = id 
        self._nome = nome
        self._descricao = descricao
        self._quantidade = quantidade
        self._valor = valor

    
    def get_id(self):
        return self._id 

    def set_id(self,id):
        self._id = id
        
    def get_nome(self):
        return self._nome

    def set_nome(self,nome):
        self._nome = nome

    def get_descricao(self):
        return self._descricao
    
    def set_descricao(self,descricao):
        self._descricao = descricao

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self,quantidade):
        self._quantidade = quantidade
    
    def get_valor(self):
        return self._valor
    
    def set_valor(self,valor):
        self._valor = valor
    


