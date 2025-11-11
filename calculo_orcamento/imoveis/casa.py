# Casa - R$ 900,00 / 1 quarto
# Se a casa tiver 2 quartos, é acrescentado R$ 250,00 na mensalidade.
# A inclusão de garagem adiciona R$ 300,00 ao valor total.

from valores import TabelaDePrecos

class Casa():
    def __init__(self):
        # Define a quantidade inicial de quartos e se há garagem.       
        self.quartos = 1
        self.garagem = False

    def definir_quartos(self, quantidade : int):
        # Atualiza a quantidade de quartos da casa.
        self.quartos = quantidade
    
    def incluir_garagem(self):
        # Marca que a casa possui garagem.
        self.garagem = True

    def calcular_mensalidade(self):
        # Calcula o valor total da mensalidade da casa.
        valor_mensalidade = TabelaDePrecos.CASA
        
        if self.quartos == 2:
            # Adiciona o valor referente ao segundo quarto.
            valor_mensalidade += TabelaDePrecos.CASA_2_QUARTOS
        
        if self.garagem:
            # Adiciona o valor da garagem, se houver.
            valor_mensalidade += TabelaDePrecos.GARAGEM_CASA
        
        return valor_mensalidade
        