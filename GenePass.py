import sys
import random
import getopt
import pyperclip
from timeit import default_timer as timer
global info, silent
# Options
options = "hn:l:o:s"
# Long options
long_options = ["help", "number =", "length =", "output =", "silent"]

# list of the characters available
numbers = "0123456789"
lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symboles = "!#$%&_-.:" #"!\"#$%&'()*+,-./:<=>?@[\]^_`{|}~;"
charlist = numbers + lettres + symboles


def infos():
    global info
    info = True
    print("GenePass.py\n"
          "OPTION\n"
          "-h   --help      <Show this page>\n"
          "-n   --number    <Number of Passwords>   (by default = 1)\n"
          "-l   --length    <Password Length>       (by default = 128)\n"
          "-o   --output    <output-file>\n"
          "-s   --silent    <don't show any passwords>\n"
          "\n"
          "if you generate only one password its while be copied to your clipboard\n"
          "\n"
          "EXAMPLES:\n"
          "PassGene.py -n 10 -l 50 -o password_list.txt\n"
          "PassGene.py -h\n"
          "\n"
          "SEE THE MAN PAGE https://github.com/M0ShYy/Password_Generator FOR MORE OPTIONS AND EXAMPLES\n")


def creapassword(nombre, longueur, output):
    global silent, charlist
    nombre = int(nombre)                                                    # make sure the variables are int
    longueur = int(longueur)
    password = ""

    for i in range(0, nombre):                                              # foreach password(s)
        for j in range(0, longueur):                                        # foreach characters
            charnb = (random.randrange(len(charlist)))                      # take a random character in the list
            password = password + charlist[charnb]                          # append the characters
        if not silent:                                                      # if the silent option as not being used
            print('mot de pass N°' + str(int(i) + 1) + ' :\n' + password)   # print the password(s)
        if output:                                                          # if the output option as being used
            outfile = open(output, "a")                                     # create/open the file in append mode
            outfile.write(password + '\n')                                  # print the password in and do a line break
        if nombre == 1:                                                     # if there is only one password
            pyperclip.copy(password)                                        # copy it to the clipboard
        password = ""                                                       # clear the password variable


def main(argumentlist):
    global info, silent
    info = False
    silent = False
    nombre = int(1)         # default number of password
    longueur = int(128)     # default number of character in the password(s)
    outputfile = ''

    try:
        arguments, values = getopt.getopt(argumentlist, options, long_options)

        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):         # test if there is -h or --help
                infos()                                     # print help
            elif currentArgument in ("-n", "--number "):    # test if there is -n or -_number
                nombre = currentValue                       # take the value of the number of password(s)
            elif currentArgument in ("-l", "--length "):    # test if there is -l or -- length
                longueur = currentValue                     # take the value of the length of the password(s)
            elif currentArgument in ("-o", "--output "):    # test if there is -o --output
                outputfile = currentValue                   # take the value of the output-file
            elif currentArgument in ("-s", "--silent "):    # test if there is -s or --silent
                silent = True
        if not info:                                        # if the help was not printed then
            creapassword(nombre, longueur, outputfile)
    except getopt.error as err:                             # if there is an error
        # output error, and return with an error code
        print(str(err))                                     # print it
        infos()                                             # and print the help
        sys.exit()

"""
argumentList = (sys.argv[1:])                               # make a list of all the option wrote by the user
main(argumentList)

"""
if __name__ == '__main__':
    argument = "-s -l 10 -n 100000 -o pass.txt"
    argumentList = (argument.split())
    print(argumentList)
    start = timer()
    main(argumentList)
    print("Passwords generated in:", timer() - start, "seconds")
