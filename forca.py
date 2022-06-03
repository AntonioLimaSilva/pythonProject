import random


def jogar_forca():
    print_message()

    index, words = write_file()

    secret_word = words[index].upper()

    correct_letters = init_words(secret_word)

    hanged = False
    acertou = False
    errors = 0

    while not hanged and not acertou:

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in secret_word:
            index = 0
            for letter in secret_word:
                if chute == letter:
                    correct_letters[index] = letter
                index += 1
        else:
            errors += 1

        hanged = errors == 6
        print(correct_letters)

    print("Fim do jogo")


def write_file():
    file_words = open("palavras.txt", "r")
    words = []
    for line in file_words:
        line = line.strip()
        words.append(line)
    index = random.randrange(0, len(words))
    file_words.close()

    return index, words


def init_words(secret_word):
    return ["_" for _ in secret_word]


def print_message():
    print('***************************************')
    print("******Bem vindo ao jogo da Forca*******")
    print('***************************************')


if __name__ == "__main__":
    jogar_forca()
