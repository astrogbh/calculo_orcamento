# Apartamento - R$ 700,00 / 1 quarto
# Se o apartamento tiver 2 quartos, é acrescentado R$ 200,00 na mensalidade.
# A inclusão de vaga de garagem adiciona R$ 300,00 ao valor total.
# Famílias sem crianças recebem 5% de desconto.

from valores import TabelaDePrecos

class Apartamento():
    def __init__(self):
        # Define a quantidade inicial de quartos, se há crianças e se possui vaga de garagem.
        self.quartos = 1
        self.tem_crianca = True
        self.vaga_garagem = False

    def definir_quartos(self, quantidade : int):
        # Atualiza a quantidade de quartos do apartamento.
        self.quartos = quantidade
    
    def incluir_vaga_garagem(self):
        # Marca que será usada a vaga de garagem.
        self.vaga_garagem = True

    def marcar_sem_crianca(self):
        # Indica que o apartamento será ocupado por uma família sem crianças.
        self.tem_crianca = False
    
    def calcular_mensalidade(self):
        # Calcula o valor total da mensalidade do apartamento.
        valor_mensalidade = TabelaDePrecos.APARTAMENTO

        if self.quartos == 2:
            # Adiciona o valor referente ao segundo quarto.
            valor_mensalidade += TabelaDePrecos.APT_2_QUARTOS
        
        if self.vaga_garagem:
            # Adiciona o valor da vaga de garagem, se houver.
            valor_mensalidade += TabelaDePrecos.GARAGEM_APT
        
        if not self.tem_crianca:
            # Aplica o desconto de 5% para famílias sem crianças.
            valor_mensalidade -= valor_mensalidade * TabelaDePrecos.DESCONTO_SEM_CRIANCA

        return valor_mensalidade
    