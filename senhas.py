from random import randint as rand
import time


DeadCodes = []

#Carregar códigos testados
txt = open("Codes.txt","r")
txtt = txt.read()
DeadCodes = txtt.split()    

def Letra(numero):
    if numero == -26:
        return 'A'
    if numero == -1:
        return 'B'
    if numero == -2:
        return 'C'
    if numero == -3:
        return 'D'
    if numero == -4:
        return 'E'
    if numero == -5:
        return 'F'
    if numero == -6:
        return 'G'
    if numero == -7:
        return 'H'
    if numero == -8:
        return 'I'
    if numero == -9:
        return 'J'
    if numero == -10:
        return 'K'
    if numero == -11:
        return 'L'
    if numero == -12:
        return 'M'
    if numero == -13:
        return 'N'
    if numero == -14:
        return 'O'
    if numero == -15:
        return 'P'
    if numero == -16:
        return 'Q'
    if numero == -17:
        return 'R'
    if numero == -18:
        return 'S'
    if numero == -19:
        return 'T'
    if numero == -20:
        return 'U'
    if numero == -21:
        return 'V'
    if numero == -22:
        return 'W'
    if numero == -23:
        return 'X'
    if numero == -24:
        return 'Y'
    if numero == -25:
        return 'Z'

def GerarCode(): 
    while 1:

        pos1 = rand(-26,9)
        if pos1 < 0:
            pos1 = (Letra(pos1))
        else:
            pos1 = str(pos1)

        pos2 = rand(-26,9)
        if pos2 < 0:
            pos2 = (Letra(pos2))
        else:
            pos2 = str(pos2)

##        pos3 = rand(-26,9)
##        if pos3 < 0:
##            pos3 = (Letra(pos3))
##        else:
##            pos3 = str(pos3)
##
##        pos4 = rand(-26,9)
##        if pos4 < 0:
##            pos4 = (Letra(pos4))
##        else:
##            pos4 = str(pos4)
##
##        pos5 = rand(-26,9)
##        if pos5 < 0:
##            pos5 = (Letra(pos5))
##        else:
##            pos5 = str(pos5)
##
##        pos6 = rand(-26,9)
##        if pos6 < 0:
##            pos6 = (Letra(pos6))
##        else:
##            pos6 = str(pos6)
##
##        pos7 = rand(-26,9)
##        if pos7 < 0:
##            pos7 = (Letra(pos7))
##        else:
##            pos7 = str(pos7)
##
##        pos8 = rand(-26,9)
##        if pos8 < 0:
##            pos8 = (Letra(pos8))
##        else:
##            pos8 = str(pos8)  

   

        code = pos1 + pos2
        #+ pos3 + pos4 + pos5 + pos6 + pos7 + pos8 

        if code not in DeadCodes:
              DeadCodes.append(code)
              print(code)          
            
              txt = open("Codes.txt","w")
              for codec in DeadCodes:
                  txt.write(codec + ' ')
              txt.close()          
              return code

while (True) :
    print("digite uma senha de 8 caracteres e tecle ENTER ...")
    senha = input()
    inicio = time.time()
    code = GerarCode()
    while code != senha:
        code = GerarCode() 
    fim = time.time()
    tempo = str(fim - inicio)
    print( "Sua senha foi descoberta em " + tempo)
    



    
   



      



   
