class Produto:
    def_init_(self,tipo,nome,cpf):
        self._tipo = tipo
        self._nome = nome
        self._cpf = cpf

   def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo   

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

        pass