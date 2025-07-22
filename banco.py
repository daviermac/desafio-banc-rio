import datetime

# Variáveis globais
saldo = 0.0
extrato = []
LIMITE_SAQUE = 500.0
LIMITE_SAQUES_DIARIOS = 3
saques_realizados = 0
data_atual = datetime.date.today()

def formatar_valor(valor):
    return f"R${valor:,.2f}".replace('.', ',') 

def depositar():
    global saldo, extrato
    try:
        valor = float(input("Digite o valor do depósito: R$ "))
        if valor <= 0:
            print("Erro: O valor deve ser positivo.")
            return
        
        saldo += valor
        extrato.append({
            'tipo': 'Depósito',
            'valor': valor,
            'data': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })
        print(f"Depósito de {formatar_valor(valor)} realizado com sucesso!")
    
    except ValueError:
        print("Erro: Digite um valor numérico válido.")

def sacar():
    global saldo, extrato, saques_realizados, data_atual
    
    
    hoje = datetime.date.today()
    if hoje != data_atual:
        saques_realizados = 0
        data_atual = hoje
    
    if saques_realizados >= LIMITE_SAQUES_DIARIOS:
        print("Erro: Limite diário de saques atingido.")
        return
    
    try:
        valor = float(input("Digite o valor do saque: R$ "))
        
        if valor <= 0:
            print("Erro: O valor deve ser positivo.")
            return
            
        if valor > LIMITE_SAQUE:
            print(f"Erro: Limite por saque é de {formatar_valor(LIMITE_SAQUE)}")
            return
            
        if valor > saldo:
            print("Erro: Saldo insuficiente. Não será possível sacar o dinheiro.")
            return
            
        saldo -= valor
        saques_realizados += 1
        extrato.append({
            'tipo': 'Saque',
            'valor': valor,
            'data': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })
        print(f"Saque de {formatar_valor(valor)} realizado com sucesso!")
        print(f"Saques realizados hoje: {saques_realizados}/{LIMITE_SAQUES_DIARIOS}")
    
    except ValueError:
        print("Erro: Digite um valor numérico válido.")

def visualizar_extrato():
    global saldo, extrato
    print("\n" + "=" * 50)
    print("EXTRATO BANCÁRIO".center(50))
    print("=" * 50)
    
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(f"{movimento['data']} - {movimento['tipo']}: {formatar_valor(movimento['valor'])}")
    
    print("\n" + "=" * 50)
    print(f"SALDO ATUAL: {formatar_valor(saldo)}".rjust(50))
    print("=" * 50 + "\n")

def menu():
    print("\nSISTEMA BANCÁRIO")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Visualizar Extrato")
    print("4 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            depositar()
        elif opcao == "2":
            sacar()
        elif opcao == "3":
            visualizar_extrato()
        elif opcao == "4":
            print("Obrigado por utilizar nosso sistema bancário!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
