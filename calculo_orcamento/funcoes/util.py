import csv
from time import sleep
from valores import TabelaDePrecos
from funcoes.validacoes import input_num, input_sn
from funcoes.formatacao import linha, carregando, formatar_real


def gerar_csv(mensalidade : int | float, contrato : int | float, parcelas : int =5):
    """
    Gera um arquivo CSV contendo as 12 parcelas do orçamento do aluguel.

    O arquivo inclui:
    - Valor mensal do aluguel.
    - Valor das parcelas do contrato imobiliário (caso existam).
    - Total de cada mês, combinando aluguel + parcela do contrato.

    Parâmetros:
        mensalidade: Valor mensal do aluguel.
        contrato: Valor total do contrato imobiliário.
        parcelas: Número de parcelas do contrato (1 a 5). Padrão: 5.

    Gera o arquivo 'orcamento_12_parcelas.csv' no diretório atual.
    """
    with open("orçamento_12_parcelas.csv", "w", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Mês", "Aluguel (R$)", "Contrato (R$)", "Total (R$)"])

        # Percorre os 12 meses do ano.
        for mes in range(1, 13):
            # Define o valor da parcela do contrato até o número escolhido.
            if mes <= parcelas:
                valor_parcela_contrato = round(contrato / parcelas, 2)
            else:
                valor_parcela_contrato = 0
            
            # Calcula o valor total do mês (aluguel + parcela do contrato)
            valor_parcela_total = mensalidade + valor_parcela_contrato

            # Escreve os valores formatados no arquivo CSV
            escritor.writerow([mes, 
                               f"{formatar_real(mensalidade, rs=False)}", 
                               f"{formatar_real(valor_parcela_contrato, rs=False)}", 
                               f"{formatar_real(valor_parcela_total, rs=False)}"
                               ])
            
        print("Arquivo 'orcamento_12_parcelas.csv' gerado com sucesso!")


def calcular_orcamento(imovel : object):
    """
    Calcula e exibe o orçamento total do imóvel selecionado.

    Exibe o valor da mensalidade, o valor do contrato imobiliário
    (parcelável em até 5x), e oferece a opção de gerar um arquivo CSV
    com as 12 parcelas mensais do orçamento.

    Parâmetros:
        imovel (objeto): Instância de uma das classes de imóvel
                         (Casa, Apartamento ou Estúdio).
    """
    carregando("Calculando orçamento")
    sleep(1)
    linha()

    # ---- Cálculo dos valores principais ----
    mensalidade = imovel.calcular_mensalidade()
    contrato = TabelaDePrecos.CONTRATO_IMOBILIARIO

    print(f"Valor da mensalidade: {formatar_real(mensalidade)}")
    print(f"Valor do contrato imobiliário: {formatar_real(contrato)}")

    # ---- Validação do parcelamento ----
    print("O contrato pode ser parcelado em até 5x sem juros.")
    parcelas = input_num("Em quantas vezes deseja parcelar? [1 a 5]: ", [1, 2, 3, 4, 5])

    # ---- Exibição final do orçamento ----
    linha()
    print("Resumo do orçamento:")
    print(f"- Mensalidade (12 meses): {formatar_real(mensalidade)}")
    print(f"- Contrato imobiliário: {parcelas}x de {formatar_real(round(contrato/parcelas, 2))}")
    print(f"- Total da 1ª parcela: {formatar_real(round(mensalidade + contrato/parcelas, 2))}")
    print()
    sleep(2)

    # ---- Geração do CSV ----
    geracao_csv = input_sn("Deseja gerar o arquivo csv contendo as 12 parcelas?"
                           "\n[Sim/Nao]: ")
    if geracao_csv:
        carregando("Gerando arquivo CSV com o valor das 12 parcelas", 5)
        gerar_csv(mensalidade, contrato, parcelas)
