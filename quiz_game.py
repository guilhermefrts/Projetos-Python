print ("Bem-vindo ao meu quiz digital!")

playing = input("Você gostaria de jogar? ") 

if playing.lower() != "sim": 
    quit()
    
print("Okay! Vamos jogar :)")

resultado = 0

answer = input("O que significa CPU em inglês? ")
if answer.lower() == "central processing unit":
    print('Correto!')
    resultado += 1
else:
    print("Incorreto!")
    
answer = input("O que significa GPU em inglês? ")
if answer.lower() == "graphics processing unit":
    print('Correto!')
    resultado += 1
else:
    print("Incorreto!")
    
answer = input("Principal diferença entre um HDD e um SSD? ")
if answer.lower() == "velocidade":
    print('Correto!')
    resultado += 1
else:
    print("Incorreto!")
    
answer = input("O que significa RAM em inglês? ")
if answer.lower() == "random access memory":
    print('Correto!')
    resultado += 1
else:
    print("Incorreto!")
    
print("Você acertou " + str(resultado) + " questões!")
print("Você acertou " + str((resultado / 4) * 100) + "%!")