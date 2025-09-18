# tests/test_validador.py
import unittest
# A linha abaixo é a correção crucial
from validador import validar_cpf 

class TestValidadorCPF(unittest.TestCase):

    def test_deve_retornar_true_para_cpf_valido(self):
        cpf_com_mascara = "529.982.247-25"
        cpf_sem_mascara = "52998224725"

        self.assertTrue(validar_cpf(cpf_com_mascara), "Deveria ser válido com máscara")
        self.assertTrue(validar_cpf(cpf_sem_mascara), "Deveria ser válido sem máscara")