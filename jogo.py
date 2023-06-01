import random

def adivinhe_o_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 1

    while True:
        tentativa = int(input("Adivinhe o número secreto (entre 1 e 100):"))
        tentativas += 1
        
        if tentativa == numero_secreto:
            print(f"Parabéns!!, você acertou o número em {tentativas} tentativas!")
            break
          
        elif tentativa < numero_secreto:
            print("O número é maior:( Tente novamente.")
          
        else:
            print("O número é menor:( Tente novamente.")

adivinhe_o_numero()