import random

top_of_range = input("Digite um número: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Por favor digite um número maior que 0 na próxima vez.')
        quit()
else:
    print('Por favor digite um número na próxima vez.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Tente advinhar um número: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Por favor digite um número na próxima vez.')
        continue

    if user_guess == random_number:
        print("Você acertou!")
        break
    elif user_guess > random_number:
        print("Você está acima do número!")
    else:
        print("Você está abaixo do número")

print("You got it in", guesses, "guesses")