import numpy as np
import math


class MLP:
    def __init__(self, qtd_neuronios_entrada, qtd_neuronios_oculta,
                 qtd_neuronios_saida):
        # Caracteristica da topologia
        self.qtd_neuronios_entrada = qtd_neuronios_entrada
        self.qtd_neuronios_oculta = qtd_neuronios_oculta
        self.qtd_neuronios_saida = qtd_neuronios_saida
        # Pesos randomicos
        self.entrada_oculta_pesos = np.random.rand(self.qtd_neuronios_oculta,
                                                   self.qtd_neuronios_entrada)
        self.oculta_saida_pesos = np.random.rand(self.qtd_neuronios_saida,
                                                 self.qtd_neuronios_oculta)
        # Aplicando viês
        self.entrada_oculta_vies = np.random.rand(self.qtd_neuronios_oculta, 1)
        self.oculta_saida_vies = np.random.rand(self.qtd_neuronios_saida, 1)
        # Função de ativação
        self.funcao_ativacao_ = np.vectorize(self.funcao_ativacao)

    def funcao_ativacao(self, x):
        return (1 / (1 + math.exp(-x)))

    def feed_forward(self, entradas):
        # Entrada
        self.entradas = entradas
        # Operação camada de entrada e camada oculta
        self.camada_oculta = self.entrada_oculta_pesos.dot(
            self.entradas) + self.entrada_oculta_vies
        self.camada_oculta = self.funcao_ativacao_(self.camada_oculta)
        # Operação camada oculta e camada de saida
        self.camada_saida = self.oculta_saida_pesos.dot(
            self.camada_oculta) + self.oculta_saida_vies
        self.camada_saida = self.funcao_ativacao_(self.camada_saida)
        return self.camada_saida
