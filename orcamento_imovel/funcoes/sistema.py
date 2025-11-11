# Sistema de Orçamentos de Imóveis R.M.
# - Exibe o valor do aluguel mensal orçado.
# - Inclui o valor do contrato (parcelável em até 5x).
# - Permite gerar um arquivo CSV com as 12 parcelas.

from imoveis.apartamento import Apartamento
from imoveis.casa import Casa
from imoveis.estudio import Estudio
from funcoes.validacoes import input_sn, input_num
from funcoes.util import calcular_orcamento
from funcoes.formatacao import linha, formatar_real
from valores import TabelaDePrecos
from time import sleep

def executar_sistema():
    """
    Menu principal da aplicação.
    Permite ao usuário escolher o tipo de imóvel e configura suas opções.
    """
    while True:
        linha()
        print("========== R.M. - Orçamentos de Imóveis ==========")
        linha()

        menu = input("Escolha o seu Imóvel:"
                    f"\n[ 1 ] - Apartamento - {formatar_real(TabelaDePrecos.APARTAMENTO)}"
                    f"\n[ 2 ] - Casa - {formatar_real(TabelaDePrecos.CASA)}"
                    f"\n[ 3 ] - Estúdio - {formatar_real(TabelaDePrecos.ESTUDIO)}"
                    "\nOpção: ")
        linha()

        if menu == "1": 
            # === Apartamento ===
            imovel = Apartamento()
            
            # Define a quantidade de quartos.
            quartos = input_num("Quantidade de quartos: "
                                "\n1 Quarto - Valor incluso"
                                f"\n2 Quartos - {formatar_real(TabelaDePrecos.APT_2_QUARTOS)}"
                                "\nQuantidade: ", [1, 2])
            imovel.definir_quartos(quartos)

            # Define se terá garagem.
            garagem = input_sn(f"Será usada a vaga da garagem({formatar_real(TabelaDePrecos.GARAGEM_APT)})?"
                               f"\n[Sim/Nao]: ")
            if garagem:
                imovel.incluir_vaga_garagem()

             # Define se há crianças na família.
            possui_crianca = input_sn(f"Terá criança na familia? Caso não, será aplicado um desconto de {TabelaDePrecos.DESCONTO_SEM_CRIANCA * 100}%."
                                      f"\n[Sim/Nao]: ")
            if not possui_crianca:
                imovel.marcar_sem_crianca()
            break

        elif menu == "2": 
            # === Casa ===
            imovel = Casa()

            # Define a quantidade de quartos.
            quartos = input_num("Quantidade de quartos: "
                                "\n1 Quarto - Valor incluso"
                                f"\n2 Quartos - {formatar_real(TabelaDePrecos.CASA_2_QUARTOS)}"
                                "\nQuantidade: ", [1, 2])
            imovel.definir_quartos(quartos)

            # Define se terá garagem.
            garagem = input_sn(f"Deseja que tenha garagem({formatar_real(TabelaDePrecos.GARAGEM_CASA)})?"
                               f"\n[Sim/Nao]: ")
            if garagem:
                imovel.incluir_garagem()
            break

        elif menu == "3": 
            # === Estúdio ===
            imovel = Estudio()
            
            # Define se terá estacionamento.
            estacionamento = input_sn(f"Adicionar estacionamento com 2 vagas({formatar_real(TabelaDePrecos.ESTACIONAMENTO)})?"
                                      f"\n[Sim/Nao]: ")
            if estacionamento:
                imovel.adicionar_estacionamento()

                # Define se terá vagas adicionais.
                vagas = input_sn(f"Deseja adicionar mais vagas({formatar_real(TabelaDePrecos.VAGA_ADICIONADA)} por vaga)?"
                                 f"\n[Sim/Nao]: ")
                if vagas:
                    quant = input_num("Quantidade da vagas a ser adicionadas: ")
                    imovel.adicionar_vagas(quant)
            break
        
        else:
            print("Opção inválida!\n")
            sleep(2)

    if menu in ["1", "2", "3"]:
        calcular_orcamento(imovel)
    
    print("================ Fim do programa! ================")
