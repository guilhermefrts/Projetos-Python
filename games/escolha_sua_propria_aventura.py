name = input("Qual seu nome? ")
print("Bem-vindo", name, "a essa aventura!")

answer = input(
    "Você está em uma estrada de terra, chegou a uma encruzilhada e você pode ir para esquerda ou direita, para onde você irá? ").lower()

if answer == "esquerda":
    answer = input(
        "Você chega a um rio, você pode caminhar ao redor dele ou atravessar nadando. Digite caminhada para dar a volta e nadando para nadar: ")

    if answer == "nadando":
        print("Você nadou e foi comido por um jacaré.")
    elif answer == "caminhada":
        print("Você andou por muitos quilômetros, ficou sem água e morreu de sede.")
    else:
        print('Opção inválida. Você perdeu!')

elif answer == "direita":
    answer = input(
        "Você chega a uma ponte, parece instável, você quer atravessá-la ou voltar (cruzar/voltar)? ")

    if answer == "voltar":
        print("Você voltou e se perdeu. Fim de jogo.")
    elif answer == "cruzar":
        answer = input(
            "Você atravessa a ponte e encontra um estranho. Você fala com ele (sim/não)? ")

        if answer == "sim":
            print("Você fala com o estranho e ele te dá uma moeda de ouro. Você ganhou!")
        elif answer == "não":
            print("Você ignora o estranho e ele fica ofendido e lhe mata. Você perdeu!")
        else:
            print('Opção inválida. Você perdeu!')
    else:
        print('Opção inválida. Você perdeu!')

else:
    print('Opção inválida. Você perdeu!')

print(name, "muito obrigado por participar!")