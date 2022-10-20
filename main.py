#05/10/2022 - Primeira atividade 


x = 1
y = 1

while (x != 0 and y != 0):
    x,y = map(int,input("Informe os 2 Números separados por espaço, por gentileza ").split())
    if(x > 0):
        if(y > 0 ):
            print("Primeiro")
        elif (y < 0):
            print("Quarto")
    elif(x < 0):
        if(y < 0):
            print("Terceiro")
        elif (y > 0):
            print("Segundo")

    else:
        break