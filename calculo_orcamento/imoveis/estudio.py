# Estúdio - R$ 1.200,00
# O estúdio pode incluir estacionamento (R$ 250,00) com 2 vagas.
# É possível adicionar vagas extras, com custo de R$ 60,00 cada.

from valores import TabelaDePrecos

class Estudio():
    def __init__(self):
        # Define se o estúdio possui estacionamento e quantas vagas estão incluídas.
        self.estacionamento = False
        self.vagas = 0

    def adicionar_estacionamento(self):
        # Ativa o estacionamento e define as 2 vagas iniciais.
        self.estacionamento = True
        self.vagas = 2

    def adicionar_vagas(self, quantidade : int):
        # Adiciona vagas extras, apenas se o estacionamento foi adicionado.
        if self.estacionamento:
            self.vagas += quantidade

    def calcular_mensalidade(self):
        # Calcula o valor total da mensalidade do estúdio.
        valor_mensalidade = TabelaDePrecos.ESTUDIO

        if self.estacionamento: 
            # Soma o valor do estacionamento e das vagas adicionais, se houver.
            valor_mensalidade += TabelaDePrecos.ESTACIONAMENTO
            vagas_extras = self.vagas - 2
            if vagas_extras  > 0:
                valor_mensalidade += TabelaDePrecos.VAGA_ADICIONADA * vagas_extras

        return valor_mensalidade

