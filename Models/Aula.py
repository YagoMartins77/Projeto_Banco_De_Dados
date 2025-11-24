from Models.Aula import Alula

class Alula:
    def __init__(self, id_aula, tipo_aula, cpf_professor):
        super().__init__(self, id_aula, tipo_aula, cpf_professor)
        self._id_aula = id_aula
        self._tipo_aula = tipo_aula
        self._cpf_professor = cpf_professor

    def get_id_aula(self):
        return self._id_aula

    def set_id_aula(self, id_aula):
        self._id_aula = id_aula

    def get_tipo_aula(self):
        return self._tipo_aula

    def set_tipo_aula(self, tipo_aula):
        self._tipo_aula = tipo_aula

    def get_cpf_professor(self):
        return self._cpf_professor

    def set_cpf_professor(self, cpf_professor):
        self._cpf_professor = cpf_professor

        pass

