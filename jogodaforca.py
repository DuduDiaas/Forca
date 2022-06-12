import os
import random

desafiante = str(input("Nome do Desafiante: "))
dasafiado = str(input("Nome de quem vai ser Desafiado: "))

os.system("cls")


FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

palavras = 'formiga babuino encefalo elefante girafa hamburger chocolate giroscopio'.split()

def main():
    """
    Funcao Principal do programa
    """
    global FORCAIMG
 
    print('F O R C A')
    letrasErradas = '' 
    letrasAcertadas = '' 
    palavraSecreta = geraPalavraAleatoria().upper()
    jogando = True
 
    while jogando: 
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta) 
 
        palpite = recebePalpite(letrasErradas + letrasAcertadas) 
 
        if palpite in palavraSecreta: 
            letrasAcertadas += palpite 
 
            if VerificaSeGanhou(palavraSecreta, letrasAcertadas): 
                print("Parabéns! A palavra secreta é "+palavraSecreta+'! Você ganhou!!')
                jogando = False
        else:
            letrasErradas += palpite 
 
            if len(letrasErradas) == len(FORCAIMG) - 1: 
                imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta) 
 
                print("Você exagerou o seu limite de palpites!")
                print("Depois de "+str(len(letrasErradas))+' letras erradas e '+str(len(letrasAcertadas)), end = ' ')
                print('palpites corretos, a palavra era '+palavraSecreta+'.')
 
                jogando = False
 
        if not jogando: 
            if JogarNovamente(): 
                letrasErradas = '' 
                letrasAcertadas = '' #
                jogando = True
                palavraSecreta = geraPalavraAleatoria().upper()
                
def geraPalavraAleatoria():
    """
    Funcao que retorna uma string a partir da
    lista de palavras global
    """
    global palavras
    return random.choice(palavras)

def imprimeComEspacos(palavra):
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaco entre suas letras ou strings
    """
    for letra in palavra:
        print(letra, end = ' ')
 
    print()
 

def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    """
    Feito a partir da variavel global que contem as imagens
    do jogo em ASCII art, e tambem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta
    """
    global FORCAIMG  
    print(FORCAIMG[len(letrasErradas)]+'\n')  
 
    print("Letras Erradas:", end = ' ') 
    imprimeComEspacos(letrasErradas) 
 
    vazio = '_'*len(palavraSecreta) 
    for i in range(len(palavraSecreta)): 
        if palavraSecreta[i] in letrasAcertadas: 
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:] 
 
    imprimeComEspacos(vazio)

def recebePalpite(palpiteFeitos):
    ''' Essa funcao garante que o usuario digite so uma letra e que confere se a mesma ja foi chutada '''
    
    while True: 
        palpite = input('Adivinhe alguma letra. \n').upper() 
        
        if len(palpite) != 1: 
            print('Coloque uma unica letra')
        elif palpite in palpiteFeitos: 
            print('Voce ja digitou essa letra, digite de novo!')
        elif not 'A' <= palpite <= 'Z': 
            print('Escolha Somente uma letra!')
        else:
            return palpite 

def JogarNovamente():
    """
    Funcao que pede para o usuario decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta
    """
    return input("Voce quer jogar novamente? (sim ou nao)\n").upper().startswith('S') 
 
def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
    '''
    Funcao que verifica se o usuario acertou todas as
    letras da palavra secreta '''
    
    ganhou = True
    for letra in palavraSecreta: 
        if letra not in letrasAcertadas: 
            ganhou = False 
            break 
 
    return ganhou 
 
main()