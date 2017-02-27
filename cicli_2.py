from funzioni_2 import divide_string, upper_word

def test_while():
    i = 0

    while i < 6:
        print "Posizione %s" % i

        i += 1

    print "il risultato finale vale", i

again = True
while again:
    operation = raw_input("Cosa vuoi fare? \n 1: Dividere frase \n 2: Uppercase \n 0: Uscire \n ")
    if operation == "1":
        sentence = raw_input("Dammi la frase: ")
        print divide_string(sentence)
    elif operation == "2":
        sentence = raw_input("Dammi la frase: ")
        print upper_word(sentence)
    elif operation == "0":
        again = False
    else:
        print "Devi scegliere 0, 1 o 2"


