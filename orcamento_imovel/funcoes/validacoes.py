from time import sleep

def input_sn(msg : str):
    """
    Exibe uma pergunta ao usuário e valida a resposta como 'Sim' ou 'Não'.

    - Retorna True se o usuário digitar 'Sim' ou 'S'.
    - Retorna False se digitar 'Não', 'Nao' ou 'N'.
    - Repete a pergunta até receber uma resposta válida.
    """
    while True:
        pergunta = input(msg).upper().strip()
        
        if pergunta in ["SIM", "S"]:
            return True
        elif pergunta in ["NÃO","NAO", "N"]:
            return False
        else:
            print("Resposta inválida! Digite 'Sim' ou 'Não'.")
            sleep(2)


def input_num(msg : str, lista_num : list[int] =[]):
    """
    Solicita um número inteiro ao usuário e valida a entrada.

    - Retorna o valor como inteiro.
    - Se uma lista de números for passada (lista_num),
      o número informado deve estar presente nela.
    - Exibe mensagens de erro e repete a pergunta em caso de entrada inválida.
    """
    while True:
        try:
            numero = int(input(msg))
            if lista_num:
                if numero in lista_num:
                    return numero
                else:
                    print(f"Digite um número válido: {lista_num}")
                    sleep(2)
                    continue
            else:
                return numero

        except ValueError:
            print("Informe um número inteiro!")
            sleep(2)
        