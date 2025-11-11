from time import sleep

def linha(sinal: str ="=", num: int = 50):
    """
    Exibe uma linha horizontal no terminal.

    Parâmetros:
        sinal (str): Caractere usado para formar a linha. Padrão: '='.
        num (int): Quantidade de caracteres repetidos. Padrão: 50.
    """
    print(f"{sinal}" * num)

def carregando(msg : str, num : int =3):
    """
    Simula uma pequena animação de carregamento no terminal.

    Exibe uma mensagem personalizada seguida de pontinhos que aparecem
    em sequência, um por segundo.

    Parâmetros:
        msg (str): Mensagem a ser exibida antes dos pontinhos.
        num (int): Quantidade de pontinhos exibidos. Padrão: 3.
    """
    print(msg, end="", flush=True)
    for _ in range(num): 
        sleep(1)
        print(".", end="", flush=True)
    print() # quebra de linha após o carregamento


def formatar_real(valor : int | float, rs : bool =True) -> str:
    """
    Formata um número como real(R$).

    - Substitui o ponto por vírgula como separador decimal.
    - Adiciona o prefixo 'R$' se o parâmetro 'rs' for True.

    Parâmetros:
        valor (int | float): Número a ser formatado.
        rs (bool): Define se o símbolo 'R$' será incluído. Padrão: True.
    """
    num = float(valor)
    if rs:
        return f"R$ {num:.2f}".replace(",", "x").replace(".", ",").replace("x", ".")
    else:
        return f"{num:.2f}".replace(",", "x").replace(".", ",").replace("x", ".")