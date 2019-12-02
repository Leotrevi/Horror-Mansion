def fim_de_jogo():
    print("-------FIM de jogo-------\n")
    exit()

    

def comando_incorreto():
    print("Comando digitado incorreto\n")


def parte1():
    escolha = input("Você esta diante de um grande castelo o que deseja fazer? (entrar)\n")
    if(escolha == "entrar"):
        print("Você entrou...\n")
    else:
        comando_incorreto()
        parte1()
    
def parte2():
    escolha = input("Dentro da mansão você não enxerga nada, esta tudo escuro(acender luzes, gritar)")
    if(escolha == "gritar"):
        print("Você gritou e um grande lobishomem correu em sua direção cravando seus grandes dentes em sua garganta\n")
        fim_de_jogo()
    elif(escolha == "acender luzes"):
        print("As luzes se acedem iluminando o local\n")
    else:
        comando_incorreto()
        parte2()
        
        
def parte3():
    escolha = input("(ficar na sala, ir para esquerda, ir para direita)")
    if(escolha == "ficar na sala"):
        print("Uma mulher em um vestido branco e rosto coberto por cabelos flutua em sua direção, ela possui tentaculos no lugar dos braços\n")
        print("A mulher correu em sua direção abraçando seu corpo com os tentaculos o esmagando, mais sorte na proxima vez")
        fim_de_jogo()
    elif(escolha == "ir para esquerda"):
        print("No corredor à esquerda ha apenas uma parede branca, voce sente tentaculos envolvendo seu corpo, e antes que perceba ja esta caido no chão sem respirar esmagado pelos tentaculos\n")
        fim_de_jogo()
    elif(escolha == "ir para direita"):
        print("Você ouve um barulho estranho atras, e quando se vira para olhar, há apenas uma parede branca lisa atrás de você")

        
    else:
        comando_incorreto()
        parte3()

def parte4():
        print("Você sente seu celular vibrar, ha uma ligação de",amigo)
        escolha1 = input("Deseja atender a ligação? (sim, não): ")
        if escolha1 == "não":
            print("Seu celular se transforma em uma cobra que te pica, sua vista fica turva e escura...")
            fim_de_jogo()
        elif escolha1 == "sim":
            print("Alô.. ALÔ!!",player,"está me ouvindo???")
            print(player,":Sim estou ouvindo o que foi",amigo,"?")
            print(amigo,":Cara eu falei pra não entrar nessa mansão, agora você só poderá sair dai se resolver todos os enigmas e..")
            print("pshsshhhhhhhhhhhhh, a ligação cai")
            print("Obrigado por jogar a demonstração de Horror Castle")

#-----Main-----#

player = input("Digite seu nome: ")
amigo = input("Digite o nome de um amigo seu: ")
print("Olá ",player,"seja bem vindo a Horror Mansion")
print("Tudo que tiver (entre parenteses) pode ser digitado como um comando valido")

parte1()
parte2()
parte3()
parte4()







        
    


