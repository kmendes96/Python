import os
import random

num_jog="x"
erros=0
sorteado=random.randrange(0,1000)
nome=input("Digite seu nome: ")
tentativas=[]

while(sorteado!=num_jog and erros<11):
    num_jog=int(input("Digite seu número: "))
    tentativas.append(num_jog)
    os.system('cls')
    print(str(len(tentativas))+" tentativas: ")
    print(tentativas)
    if(sorteado>num_jog):
        print("ERRO, o numero é maior")
    elif(sorteado<num_jog):
        print("ERRO, o numero é menor")
    erros+=1
if erros<12 and num_jog==sorteado:
    print("Parabéns "+nome+", você acertou o número "+str(num_jog)+" em "+str(erros)+" tentativas.")
else:
    print("Você perdeu por errar 11 vezes. Mais sorte na próxima, "+nome+"\nO número aleatório era: "+str(sorteado))