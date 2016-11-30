palabra = input("palabra a buscar ?? ")
archivo = input("Archivo donde Buscar >> ")
def creartxt():
##archivo vacio a quien se va a llenar o escribir write
    repetidas=0
    conP=open('deber2.txt','w')
##archivo lleno con texto se le va a leer read
    archF=open('harry.txt','r')
    lines=archF.readlines()
    for line in lines:
        palabras=line.split(' ')
        for p in palabras:
            if p==palabra:
                repetidas=repetidas+1
    print("la palabra \"{0}\" se repite {1} veces en el Archivo {2}".format(palabra,repetidas,archivo))

creartxt()

