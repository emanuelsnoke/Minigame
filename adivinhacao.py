import random

def adivinhacao():
    print("Bem-vindo ao jogo de adivinhação de números!")
    print("Estou pensando em um número entre 1 e 100.")
    
    # Gerar um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10  # O jogador tem 10 tentativas

    while tentativas < max_tentativas:
        tentativas += 1
        palpite = int(input(f"Tentativa {tentativas}/{max_tentativas}: Adivinhe o número: "))
        
        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas!")
            break
    else:
        print(f"Você não conseguiu adivinhar o número. Era {numero_secreto}.")

if __name__ == "__main__":
    adivinhacao()
