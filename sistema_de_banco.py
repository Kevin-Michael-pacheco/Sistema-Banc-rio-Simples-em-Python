lista = []
s=0
def cadastro():
    usuario = {}
    no=str(input('digite o nome de usuario pra cadastra: '))
    cpf=int(input('digite seu cpf: '))
    senha=int(input('crie uma senha pra sua conta: '))
    usuario['nome'] = no
    usuario['cpf'] = cpf
    usuario['senha'] = senha
    lista.append(usuario)

def login():
    n= str(input('digite seu nome de usuario: '))
    if n == lista[0]['nome']:
        c_p_f=int(input('digite seu cpf: '))   
        if c_p_f == lista[0]['cpf']:
            s=int(input('digite sua senha: '))
            if s == lista[0]['senha']:
                print('login completo')
         
def interface(saldo):
    print()
    print('nome: ',lista[0]['nome'])
    print()
    print('seu saldo e de : ',saldo)
    print()
    print('deseja depositar algum valor na sua conta se sim digite 1 senão digite qualquer outro numero')
    print()
    opcao=int(input('digite uma opção: '))
    if opcao == 1:
        valor =int(input('digite o valor pra ser depositado: '))
        s=int(input('digite sua senha pra confirmar o deposito: '))
        if s ==lista[0]['senha']:
            saldo+=valor
            print()
            print('saldo adicionado a conta tenha um bom dia')
            print()
        else:
            print('senha incorreta tenete novamente')
    else:
        print()
        print('tenha um bom dia')
        print()
    return saldo



def pagar(saldo):
    nome=str(input('digite o nome de que vc deseja pagar: '))
    conta=int(input('digite o numeros da conta da pessoa para realizar o pagamento: '))
    v=float(input('digite o valor a ser pago pra essa pessoa: '))
    pagar = saldo-v
    if saldo < v:
        print('saldo insuficiente pra realizar o pagamento')
    else:
        print('pagamento conculuido')
        print('saldo restante de',pagar)
        saldo=pagar
    return saldo

def protecao():
    print('não compartilhar sua senha com outras pessoa estranhas')
    print()
    print('não clicar em links suspeitos que podem ter virus')
    print()
    print('caso perca seu celular entre no nosso suporte atraves de outro celular o ou outro dispositivo e prove que e você')
    print()


c = cadastro()
while True:
    print('=============MENU=========')
    print('seja benvindo ao nosso banco')
    print('o que deseja fazer digite um opção das opçoes abaixo')
    print('1- ver sua conta')
    print('2-pagar contas')
    print('3-o que devo saber pra proteger minha conta ??')
    print('4- sair')
    print('=============================')
    op=int(input('digite uma opção: '))
    print()
    if op == 1:
        s=interface(s)
    elif op == 2:
        s=pagar(s)
    elif op == 3:
        prote=protecao()
    elif op == 4:
        print('programa encerrado')
        print()
        break
    else:
        print('opção invalida')



