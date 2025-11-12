class Plano:
    def_init_(self,tipo,ID_Produto_Produto):
        self._ID_Produto = ID_Produto
        self._tipo = tipo

    @dataclass
   def get_id(self):
        return self._ID_Produto

    def set_ID_Produto(self, ID_Produto):
        self._ID_Produto = ID_Produto   

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

        pass