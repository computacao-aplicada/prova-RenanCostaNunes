import unittest
from validador import validar_cpf 

class TestValidadorCPF(unittest.TestCase):

    def test_deve_retornar_true_para_cpf_valido(self):
        cpf_com_mascara = "529.982.247-25" 
        cpf_sem_mascara = "52998224725" 
        cpf_com_espacos = " 529.982.247-25 "

        self.assertTrue(validar_cpf(cpf_com_mascara), "Deveria ser válido com máscara.")
        self.assertTrue(validar_cpf(cpf_sem_mascara), "Deveria ser válido sem máscara")
        self.assertTrue(validar_cpf(cpf_com_espacos), "Deveria aceitar espaços externos")

    def test_deve_rejeitar_entradas_invalidas_nulas_ou_vazias(self):
        self.assertFalse(validar_cpf(None), "Deveria rejeitar None (nulo)")
        self.assertFalse(validar_cpf(""), "Deveria rejeitar string vazia") #
        self.assertFalse(validar_cpf("529.982.247-2X"), "Deveria rejeitar caractere inválido 'X'") #

    def test_deve_rejeitar_cpf_com_tamanho_invalido(self):
        self.assertFalse(validar_cpf("1234567890"), "Deveria rejeitar CPF com 10 dígitos") #
        self.assertFalse(validar_cpf("123456789012"), "Deveria rejeitar CPF com 12 dígitos") #

    def test_deve_rejeitar_cpf_com_todos_digitos_iguais(self):
        self.assertFalse(validar_cpf("00000000000"), "Deveria rejeitar sequência de 0s") #
        self.assertFalse(validar_cpf("11111111111"), "Deveria rejeitar sequência de 1s") #

    def test_deve_rejeitar_cpf_com_dv_incorreto(self):
        self.assertFalse(validar_cpf("529.982.247-24"), "DV incorreto para CPF conhecido") #
        self.assertFalse(validar_cpf("123.456.789-00"), "DV incorreto para CPF genérico") #