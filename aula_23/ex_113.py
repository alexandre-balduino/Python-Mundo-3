
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número inteiro válido.")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário.")
            return 0
        else:
            return num
def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número real válido.")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário.")
            return 0
        else:
            return num

num1 = leiaInt("Digite um valor Inteiro: ")
num2 = leiaFloat("Dogite um valor Real: ")
print(f"O valor inteiro digitado foi {num1} e o real foi {num2}")
