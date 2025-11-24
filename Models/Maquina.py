from Models.Maquina import Maquina

class Maquina:
    def __init__(self, nome, id_mqn, parte_trabalhada):
        super().__init__(self, nome, id_mqn, parte_trabalhada)
        self._nome_mqn = nome_mqn
        self._id_mqn = id_mqn
        self._parte_trabalhada = parte_trabalhada
        
  
    def get_nome(self):
        return self._nome_mqn

    def set_nome(self, nome):
        self._nome_mqn = nome

    def get_id_mqn(self):
        return self._id_mqn

    def set_id_mqn(self, id_mqn):
        self._id_mqn = id_mqn

    def get_parte_trabalhada(self):
        return self._parte_trabalhada

    def set_parte_trabalhada(self, parte_trabalhada):
        self._parte_trabalhada = parte_trabalhada

        pass

    



