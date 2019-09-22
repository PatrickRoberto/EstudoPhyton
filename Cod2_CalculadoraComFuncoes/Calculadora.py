def ReceberValor(t):
    return int(input(str.format("Digite o valor {}: ", t)))

def ModeloSaida(x,y, operaco, resultado):
    return str.format("{} {} {} = {}", x, "+", y, resultado)

def sair():
    print("Fim da execução")

def soma(x, y):
    return ModeloSaida(x,y,'+',(x+y))

def subtracao(x, y):
    return ModeloSaida(x,y,'-',(x-y))

def multiplicacao(x, y):
    return ModeloSaida(x,y,'*',(x*y))

def divisao(x, y):
    return ModeloSaida(x,y,'/',(x/y))

def Menu(opcoes):
    op = -1
    while(op > len(opcoes) or op < 0):
        print('Selecione uma opção')
        i = 0
        while i < len(opcoes):
            print(opcoes[i])
            i = i + 1
        print('Digite 0 par sair')
        op = int(input("Digite o número da opção: "))
        if op == 0: break

    return op


calculos = [soma, subtracao, multiplicacao, divisao]
opcoes =['Digite 1 para somar!','Digite 2 para subtrair','Digite 3 para multiplica','Digite 4 para dividir']

op = Menu(opcoes)
if op == 0: sair()
else:
    x = ReceberValor(1)
    y = ReceberValor(2)
    print(calculos[op-1](x, y))

