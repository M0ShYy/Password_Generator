import random
import sys
import getopt

# Options
options = "hn:l:o:"
# Long options
long_options = ["help", "number =", "length =", "output ="]
# list of the characters avalable
charlist = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


def infos():
   aide = open("h.elp", "rt")
   print(aide.read())
   aide.close()


def creapassword(nombre,longueur,output):
    #outfile =''
    nombre = int(nombre)
    longueur = int(longueur)
    password = ""
    for i in range(0, nombre):  # pour chaque mot de passe
        for j in range(0, longueur):  # pour chaque caractere du mot de pass
            charnb = (random.randrange(len(charlist)))  # prend la position d'un character dans la liste
            password = password + charlist[charnb]  # metre les characters les uns a la suite des autres
        #print('\033[1;31mmot de pass N°' + str(int(i) + 1) + ' :\033[1;m\n' + password)  # affichage du mot de pass colorer
        print('mot de pass N°' + str(int(i) + 1) + ' :\n' + password)  # affichage du mot de pass non colorer
        if output:
            outfile= open(output, "a")
            outfile.write(password + "\n\n")

        password = ""  # remetre a zero le mots de passe
    #if output:
        #outfile.close()


def main(argumentlist):
    nombre = int(0)
    longueur = int(0)
    outputfile = ''
    if not argumentlist:
        infos()
    try:
        arguments, values = getopt.getopt(argumentlist, options, long_options)

        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):     #help commande
                infos()
            elif currentArgument in ("-n","--number "):
                nombre = currentValue

            elif currentArgument in ("-l", "--length "):
                longueur = currentValue
            elif currentArgument in ("-o", "--output "):
                outputfile = currentValue

        creapassword(nombre,longueur,outputfile)
    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
        infos()
        sys.exit()

if __name__ == '__main__':
    #argumentList = (" --number 4 --length 40 --output test".split())
    #print(argumentList)
    argumentList = (sys.argv[1:])
    main(argumentList)
