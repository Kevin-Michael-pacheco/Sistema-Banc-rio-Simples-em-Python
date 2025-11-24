class conta:
    def __init__(self):
        self.dono =input('digite seu nome: ')
        while True:
            try:
                self.saldo =float(input('digite o seu saldo: '))
                break
            except:
                print('o saldo so poder ser numeros não letras')
                continue


    def depositar(self):
        while True:
            try:
                n=int(input("quanto deseja depositar na conta:"))
                if n >=1:
                    self.saldo += n
                    print('deposito realizado com sucesso')
                    print(f'seu saldo  atual agora e de { self.saldo}')
                    break
                else:
                    print('so e possivel adicionar na conta valores maiores que 0')
                    break
            except:
                print('Erro digite apenas o valor em numero pra fazer o deposito')
                continue

    def sacar(self):
        while True:
            try:
                s=int(input('quanto deseja sacar da sua conta: '))
                if s<= self.saldo:
                    self.saldo -= s
                    print('saque realizado')
                    print(f"saldo restante de {self.saldo} reais")
                    break
                else:
                    print("saldo insuficiente")
                    break
            except:
                print(' Erro digite a penas numeros para fazer o saque')
                continue
            
    def mostrar(self):
        print(f'nome: {self.dono}')
        print(f'saldo atual: {self.saldo}')

c =conta()

while True:
    try:
        print('=========================Menu==============================')
        print('1- conferir sua conta')
        print('2- depositar dinheiro na sua conta')
        print('3- sacar dinheiro da sua conta')
        print("4- sair")
        op=int(input('digite o numero da opção que deseja: '))
        print('============================================================')
    except:
        print('digite apenas os numero das opçoes disponiveis')
        continue
     
    if op == 1:
        c.mostrar()
    elif op == 2:
        c.depositar()
    elif op == 3:
        c.sacar()
    elif op == 4:
        print('programa encerrado')
        break
    else:
        print('opção invalida')


        