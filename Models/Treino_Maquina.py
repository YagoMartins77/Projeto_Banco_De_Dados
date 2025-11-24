from Models.Maquina import Maquina

class Treino_Maquina:
    def __init__(self, id_tr, nome_mqn):
        super().__init__(self, id_tr, nome_mqn)
        self._id_tr = id_tr
        self._nome_mqn = nome_mqn
   
    def get_id_tr(self):
        return self._id_tr

   
    def set_id_tr(self, id_tr):
        self._id_tr = id_tr

  
    def get_nome_mqn(self):
        return self._nome_mqn

    def set_nome_mqn(self, nome_mqn):
        self._nome_mqn = nome_mqn

        pass

