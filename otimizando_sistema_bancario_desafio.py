def menu():
    menu =  """
                Menu                   
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair

    => """
    return input(menu)

def main():
    LIMITE_SAQUES =3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato =""
    numero_saques=0
    usuarios = []
    contas = []
 
    
    while True:
        opcao = menu()
        
        if opcao == 'd':
            valor = float(input("Informe o valor do deposito: "))
        
            saldo, extrato = depositar(saldo,valor,extrato)

        elif opcao == 's':
            valor = float(input("Digite a quantia a ser retirada: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)

            if conta:
               contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break
        else:
            print("Opção inválida, por favor selecione novamente a operação desejada")



# funçoes
def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente número): ")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print(" Já existe usuario cadastrado com esse CPF! ")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe  a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})

    print("  Usuario criado com sucesso !")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia,numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n Conta criada com sucesso!  ")
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    
    print(" Usuário não encontrado")



def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Operação falhou, saldo insuficente")
    elif excedeu_limite:
        print("operação falhou, o valor não pode ser maior que o limite")
    elif excedeu_saques:
        print("Operação falhou! Número maximo de saques excedido")
    elif valor > 0:
        saldo-= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques+=1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou, o valor informado é invalido")
    return saldo, extrato  
    
def depositar(saldo,valor,extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f"Deposito: {valor:.2f}\n"
        print("\n  Deposito realizado com sucesso!")
    else:
        print("\n Operação falhou! o vlaor informado é invalido  ")

    return saldo, extrato

def exibir_extrato(saldo, / , * ,extrato):
    print("\n----------Extrato----------")
    print("Não foram realizado movimentaçoes. " if not extrato else extrato)
    print(f"  Saldo: R${saldo:.2f}")
    print("-----------------------------")

 
def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agencia: {conta['agencia']}
            C/C:  {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print(linha)
        print("="* 85)
        

main()