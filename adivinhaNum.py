from random import randint

jogar = 2

while(jogar-1):
    num_secreto = randint(1,30)
    print("\n--- Bem-vindo ao jogo da adivinhação [valor 1 - 30] ---\n")

    opt=-1
    while not(opt>=1 and opt<=3):
        opt = int(input("Dificuldade: 1-facil(10 tentativas) | 2-medio(8 tentativas) | 3-dificil(5 tentativas)\n"))
        if(opt not in(1,2,3)):
            print("Opção inválida!\n")

    chances=-1
    if opt==1:
        chances = 10 #facil
    elif opt==2:
        chances = 8 #medio
    else:
        chances = 5 #dificil

    num_chutes = venceu = 0
    while(num_chutes <= chances):
        chute = int(input("Seu chute: "))
        num_chutes+=1
        if(chute == num_secreto):
            print("Voce venceu!")
            venceu = 1
            break
        elif(chute<num_secreto):
            print(f"seu chute foi {chute} ({num_chutes}/{chances})\nTente um valor mais alto!")
            continue
        else:
            print(f"seu chute foi {chute} ({num_chutes}/{chances})\nTente um valor mais baixo!")

    if not(venceu):
        print('Voce perdeu :(\nTente na proxima!')

    jogar = int(input("Deseja jogar novamente? [1- Não | 2- Sim] "))