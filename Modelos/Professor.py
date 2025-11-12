from abc import ABC

class Professor(ABC):
    def __init__(self, cpf_prof, rg_prof, nome_prof, horario_prof, telefone_prof):
        self._cpf_prof = cpf_prof
        self._rg_prof = rg_prof
        self._nome_prof = nome_prof
        self._horario_prof = horario_prof
        self._telefone_prof = telefone_prof

    def get_cpf_prof(self):
        return self._cpf_prof

    def set_cpf(self, cpf_prof):
        self._cpf_prof = cpf_prof
 
    def get_rg(self):
        return self._rg_prof

    def set_rg(self, rg_prof):
        self._rg = rg_prof

    def get_nome(self):
        return self._Nome_Prof

    def set_nome(self, nome):
        self._nome = nome
     
    def get_horario(self):
        return self._horario_prof

    def set_time(self, horario_prof):
        self._horario = horario_prof
     
    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone
        
        pass