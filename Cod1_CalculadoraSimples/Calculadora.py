#Calculadora
print("Calculadora")
print("\n")
print("Digite o número a opção que deseja")
print("Somar: 1")
print("Subtrair: 2")
print("Multiplicar: 3")
print("Dividir: 4")
print("\n")

op = int(input("Digite (1/2/3/4)"))

if op  < 1 or op > 4:
    saida = "Valor Invalido"

else:
    val1 = int(input("Digite o valor 1: "))
    val2 = int(input("Digite o valor 2: "))
    ModeloSaida = "{} {} {} = {}"
    if op == 1:
        saida = str.format(ModeloSaida, val1, "+", val2, (val1 + val2))
    elif op == 2:
        saida = str.format(ModeloSaida, val1, "-", val2, (val1 - val2))
    elif op == 3:
        saida = str.format(ModeloSaida, val1, "x", val2, (val1 * val2))
    elif op == 4:
        saida = str.format(ModeloSaida, val1, "-", val2, (val1 - val2))
    else:
        print("Erro na operação")

print(saida)
