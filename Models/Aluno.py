from Models.Aluno import Aluno

class Aluno:
    def __init__(self, cpf, rg_aluno, telefone_aluno, nome_aluno, objetivo_treino, tipo_plano, cpf_pers):
        super().__init__(self, cpf, rg_aluno, telefone_aluno, nome_aluno, objetivo_treino, tipo_plano, cpf_pers)
        self._cpf = cpf
        self._rg_aluno = rg_aluno
        self._telefone_aluno = telefone_aluno
        self._nome_aluno = nome_aluno
        self._objetivo_treino = objetivo_treino
        self._tipo_plano = tipo_plano
        self._cpf_pers = cpf_pers

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_rg_aluno(self):
        return self._rg_aluno

    def set_rg_aluno(self, rg_aluno):
        self._rg_aluno = rg_aluno

    def get_telefone_aluno(self):
        return self._telefone_aluno

    def set_telefone_aluno(self, telefone_aluno):
        self._telefone_aluno = telefone_aluno

    def get_nome_aluno(self):
        return self._nome_aluno

    def set_nome_aluno(self, nome_aluno):
        self._nome_aluno = nome_aluno

    def get_objetivo_treino(self):
        return self._objetivo_treino

    def set_objetivo_treino(self, objetivo_treino):
        self._objetivo_treino = objetivo_treino
    def get_tipo_plano(self):
        return self._tipo_plano

    def set_tipo_plano(self, tipo_plano):
        self._tipo_plano = tipo_plano

    def get_cpf_pers(self):
        return self._cpf_pers

    def set_cpf_pers(self, cpf_pers):
        self._cpf_pers = cpf_pers
        pass

