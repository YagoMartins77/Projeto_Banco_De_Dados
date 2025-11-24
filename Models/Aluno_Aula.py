from Models.Aluno_Aula import Aluno_Aulaluno


class Aluno_Aula:
    
def __init__(self, id_aula, cpf_aluno):
        super()._init_(self, id_aula, cpf_aluno)
        self._id_aula = id_aula
        self._cpf_aluno = cpf_aluno

    def get_aula(self):
        return self._id_aula

   
    def set_id_aula(self, id_aula):
        self._id_aula = id_aula

   
    def get_cpf_aluno(self):
        return self._cpf_aluno

    def set_cpf_aluno(self, cpf_aluno):
        self._cpf_aluno = cpf_aluno

        pass

