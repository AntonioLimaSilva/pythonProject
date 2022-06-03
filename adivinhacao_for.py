import random


def jogar_adivinhacao():
    print('***************************************')
    print('***Bem vindo ao jogo de Adivinhação!***')
    print('***************************************')

    secret_number = random.randrange(1, 101)
    total_retry = 0

    print("Digite (1) nível baixo, (2) nível médio e (3) nível difícil")

    level = int(input("Defina o nível: "))

    if level == 1:
        total_retry = 15
    elif level == 2:
        total_retry = 10
    elif level == 3:
        total_retry = 5
    else:
        print("Opção inválida!")

    for count_retry in range(1, total_retry + 1):
        print(f"Tentativa {count_retry} de {total_retry}")
        chuteStr = input('Digite o seu numero: ')

        chute = int(chuteStr)

        if chute < 1 or chute > 100:
            print("Vc deve digitar um número entre 1 e 100")
            continue

        if secret_number == chute:
            print("Parabéns! Vc acertou")
            break
        elif chute > secret_number:
            print("Seu chute foi muito alto")
        elif chute < secret_number:
            print("Seu chute foi muito baixo")
