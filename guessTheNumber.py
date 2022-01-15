import random

n = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input("Chute um número de 1 a 10: "))    
    if chute > n:
        print("Você chutou muito alto!")
    elif chute < n:
            print("Você chutou baixo!")
    elif chute == n:
        acertou = True
        print("Você acertou!")     
