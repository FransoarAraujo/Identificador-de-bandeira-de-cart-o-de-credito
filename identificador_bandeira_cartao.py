# identificador_bandeira_cartao.py

import re

def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira de um cartão de crédito com base no número.
    """
    numero_cartao = re.sub(r"\D", "", numero_cartao)  # Remove caracteres não numéricos

    padroes = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "MasterCard": r"^(5[1-5][0-9]{14}|2[2-7][0-9]{14})$",
        "American Express": r"^3[47][0-9]{13}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$"
    }

    for bandeira, padrao in padroes.items():
        if re.match(padrao, numero_cartao):
            return bandeira

    return "Bandeira desconhecida"

# Execução interativa
if __name__ == "__main__":
    numero = input("Digite o número do cartão de crédito: ")
    bandeira = identificar_bandeira(numero)
    print(f"Bandeira identificada: {bandeira}")
