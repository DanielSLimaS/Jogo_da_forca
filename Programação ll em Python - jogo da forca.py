#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Exercício 03 - Jogo da Forca
#Nome:Daniel dos Santos Silva Junior RA:0040972213018
#Nome:Júlia Degan Falcão RA:0040972213031

import random

# Esconde as palavras nessas condições
#criptografia inprovisada 

def encriptarPalavra(palavra):
    alfabeto = 'b/R6WVXMlP#Gu={r5VcQf2]kpXI[VbAYaY>fL28(3SW-&q/uPI{kdCC<P/F7O?WS+qL4|(^CjVPuRHQ6~_R0e7AvDT<Pz~MnJq2knZFPa3~|u<[>i<9oC~(d_y^=n?,Viz0{+mSyJ/H.$6C1\p-pcza/V1E%OF+T[S7p{A]%wS<hjenGpVE&xUokD?6WuPfE4F?EB43X,hf:p:F<):kz(f?~}:O-N3PX2{qPvW:pqP\V|4liP~4k_:u,dcsS,FcpodF7<4Ruy^sQgDTI/-dcl6pVfwgITgHz9e>f&d6dR3eUx$06[++f=%kY{-$)+dswRt,-PzE]\B/~JSb)EmpLPJgF_+PnXW(xOK_\C3w~#WU+;VO#1n7S|fx&KE,D<|+jnP^\t2ge;^d]R,A}i|y2/cQS2e4gs,jcObNVy|?l|&0c)9$8$MxDUaT.mTYC#TNV#6B_#9qBY+l)pub;\rJ(C=S]hGo>-g0SN>q#l]s$kRwmd+Qy9aDS<_O%b$bc~}wiykxf7lz^G5F#t1M9?nMjs;V()G14^fh|r(RtvPI2}d(QPdO<Q|]7IdF>{zIcVjU,M8z;|zW{e&0D=bmNs(zLy>(la}~LOHd(Rk\gO\2<&a/ii#kaC%ynx=Di]WWJT.j\M[-5uSh=XPq4hd!;/%r$$W.L!ce\4NV~zX~[Ul!267ikKV.>St.w:X{%p}?du\IJjxPCt8~Ou.)a:c~NYG\[I%JPz.sH;e5.VRyT)ib0!S;Hh/:chc<h\Hj\i2y/9{MG{{i.v{,5fk8t9E+)7g(%AqkuoEJ!\-{RXT2\%v0tcxs5RZr6^NYY_jz+x7:Wh2YH4\X/(L!tj?\D5%_+ehAs.<Y}e&G(JgW_7j60vi[jqjKnVEKjB[8B|<q6~%UkWt[~T%_OQ_|Mqy;q8Hy[aLn)i<is$Wyk>E/8%NbFa:doNqDGY(Oo(Pje^x~eUb[ljb%wt0Jq.aLmK~X6](a;vm$X/3ug>fLIxJDh-u5)P>l[4!_T~)k[Kphy]&D!6{QsHcy8'
    return "".join([chr(ord(index1) ^ ord(index2)) 
        for (index1, index2) in zip(palavra,alfabeto)])



#aqui será adicionara as palavras criptografada no bloco de texto
def adicionarPalavra():
    
    print(2*'\n')
    nova_palavra = input('Digite uma palavra: ')
    nova_palavra = nova_palavra.lower()
    palavra_criptografada = encriptarPalavra(nova_palavra)
    arq = open('BancoDePalavras.txt', 'a')
    arq.write(palavra_criptografada+'\n')
    arq.close()
    print(6*'\n')


#aqui tera uma opção de mostar as palavras que estão criptografada
def exibirPalavras():
    arq = open('BancoDePalavras.txt', 'r')
    
    palavras = arq.readlines()
    if len(palavras) == 0:
        print("Não foi encontrada palavra")
    else:
        print(">> Palavras: <<")
        #print(palavras)
        for palavra in palavras:
            descriptografarPalavra = encriptarPalavra(palavra)
            descriptografarPalavra =  descriptografarPalavra.replace(descriptografarPalavra[len(descriptografarPalavra)-1],"")
            print(descriptografarPalavra)
    arq.close()
    
#mostrando palavra
def bancoDePalavras():

    while(True):
        print('Palavras Introduzidas')
        exibirPalavras()
        print(1*"\n")
        print('1) *SAIR*')
        opcao = input('Digite a opção que deseja escolher: ')
        
        if (opcao == '1'):
            print(6*'\n')
            break
        else:
            print('Opção inválida! Tente novamente...')


#Configurar Jogo
def configurarJogo():
    print("\n" * 4)
    while(True):
        print("*********************************")
        print("***Bem vindo ao jogo da Forca!***")
        print("*********************************")

        print(">>>   CONFIGURAÇÃO DO JOGO <<<:")
        print("escolha uma opção: ")
        print('A)	Adicionar nova palavra ao jogo.')
        print('B)	Exibir base de palavras.')
        print('C)	Concluir configuração.')

        opcao = input("Opção escolhida: ")

        if (opcao == "A" or opcao == "a"):
            adicionarPalavra()
        elif(opcao == "B" or opcao == "b"):
            print(6*'\n')
            bancoDePalavras()
        elif(opcao == "C" or opcao == "c"):
            print(6*'\n')
            break
        else:
            print('Opção inválida! Tente novamente...')

    print("\n" * 4)

# Seleciona uma palavra aleatória do arquivo
def GerarPalavra():

    palavras = []
    arquivo = open("BancoDePalavras.txt", "r")
    
    
    for linha in arquivo:
        #print(linha)
        linha = linha.replace("\n","")
        palavras.append(linha)

    i = random.randrange(0, len(palavras))
    palavra_random = palavras[i]
    arquivo.close()
    return palavra_random

# Inserir traços no lugar das letras
def Tracos(palavra_random):
    #print(palavra_random)
    lista = []
    for letra in palavra_random:
        lista.append('_')
    return lista

# Pede ao usuário digitar uma letra
def PedeLetra():
    
    tentativa = input("Escolha uma letra: ")
    return tentativa.lower()

# Substitui a letra no lugar do traço
def SubstituiTraco(tentativa, letras_corretas, palavra_secreta):
    
    i = 0
    for letra in palavra_secreta:
        if (tentativa == letra):
            letras_corretas[i] = letra
        i += 1
        
# Desenho do enforcado
def desenhoForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |     ('_')   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |     ('_')   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |     ('_')   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |     ('_')   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |     ('_')   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |     ('_')   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |     ('_')   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
def validaPartida():
    arquivo = open("BancoDePalavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha)
    if(len(palavras)>0):
        return True
    else:
        return False
    
    
# Jogar
def jogar():
    print('\n' * 3)
    if(validaPartida()):
        print('*JOGANDO*...\n')
        palavra_encriptada = GerarPalavra()
        palavra_secreta = encriptarPalavra(palavra_encriptada)
        letras_corretas = Tracos(palavra_secreta)
        letras_erradas = []

        vitoria = False
        derrota = False

        erros = 0

        letras_faltando = len(palavra_secreta)

        print(letras_corretas)

        while (vitoria == False and derrota == False):
            tentativa = PedeLetra()

            if (tentativa in palavra_secreta):
                SubstituiTraco(tentativa, letras_corretas, palavra_secreta)
                letras_faltando = str(letras_corretas.count('_'))
                print(letras_corretas)
                print('\n')

                if (letras_faltando == "0"):
                    vitoria = True
                    print(f"Você acertou!! A palavra era >> {palavra_secreta} <<.")
                    print("       ___________      ")
                    print("      '._==_==_=_.'     ")
                    print("      .-\\:      /-.    ")
                    print("     | (|:.     |) |    ")
                    print("      '-|:.     |-'     ")
                    print("        \\::.    /      ")
                    print("         '::. .'        ")
                    print("           ) (          ")
                    print("         _.' '._        ")
                    print("        '-------'       ")
            else:
                letras_erradas.append(tentativa)
                erros += 1
                print('\n')
                print(f'Ainda faltam acertar {letras_faltando} letras')
                print(f'Você ainda tem {7-erros} tentativas')
                print('Letras incorretas já inseridas: ', letras_erradas)
                desenhoForca(erros)
                print(letras_corretas)
                print('\n')

                if erros == 7:
                    derrota = True
                    print(f' >Você Perdeu!<. A palavra correta era >> {palavra_secreta} <<.')

        print('\n' * 3)
    else:
        print(">>> Não foi encontrado palavras! <<<")
        
        print('\n' * 2)

# Menu Principal
def menuPrincipal():
    
    while(True):
        
        
        print("*********************************")
        print("***Bem vindo ao jogo da Forca!***")
        print("*********************************")

        print(">>>   MENU <<<:")
        print('1)	Configuração do Jogo')
        print('2)	Jogar')
        print('3)	Sair')

        opcao = int(input('Digite a opção que deseja escolher: '))

        if (opcao == 1):
            configurarJogo()
        elif (opcao == 2):
            jogar()
        elif (opcao == 3):
            break
        else:
            print('Opção inválida! Tente novamente...')

# Início do Programa
open('BancoDePalavras.txt', 'w').close()
menuPrincipal()


# In[ ]:





# In[ ]:




