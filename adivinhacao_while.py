print('***************************************')
print('***Bem vindo ao jogo de Adivinhação!***')
print('***************************************')

secret_number = 42
count_retry = 1
total_retry = 3

while count_retry <= total_retry:
    print(f"Tentativa {count_retry} de {total_retry}")
    chuteStr = input('Digite o seu numero: ')

    chute = int(chuteStr)

    if secret_number == chute:
        print("Parabéns! Vc acertou")
    if chute > secret_number:
        print("Seu chute foi muito alto")
    elif chute < secret_number:
        print("Seu chute foi muito baixo")

    count_retry = count_retry + 1
