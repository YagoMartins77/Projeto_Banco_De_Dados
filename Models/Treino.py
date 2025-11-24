class Treino:
    def __init__(self, id, alongamentos, exercicios_arbcs, exercicios_mqn, carga_mqn, cpf_aluno):
        super().__init__(self, id, alongamentos, exercicios_arbcs, exercicios_mqn, carga_mqn, cpf_aluno) 
        self._id = id 
        self._alongamentos = alongamentos
        self._exercicios_mqn = exercicios_mqn
        self._exercicios_arbcs = exercicios_arbcs
        self._carga_mqn = carga_mqn
        self._cpf_aluno = cpf_aluno

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_alongamentos(self):
        return self._alongamentos

    def set_alongamentos(self, alongamentos):
        self._alongamentos = alongamentos

    def get_exercicios_mqn(self):
        return self._exercicios_mqn

    def set_exercicios_mqn(self, exercicios_mqn):
        self._exercicios_mqn = exercicios_mqn

    def get_exercicios_arbcs(self):
        return self._exercicios_arbcs

    def set_exercicios_arbcs(self, exercicios_arbcs):
        self._exercicios_arbcs = exercicios_arbcs

   
    def get_carga_mqn(self):
        return self._carga_mqn

    def set_carga_mqn(self, carga_mqn):
        self._carga_mqn = carga_mqn

    def get_cpf_aluno(self):
        return self._cpf_aluno

  
    def set_cpf_aluno(self, cpf_aluno):
        self._cpf_aluno = cpf_aluno

        pass

