def say_hello(name):
    print "Ciao", name

def make_sum(a, b):
    return a + b

def make_division(a, b):
    return a / b

def ask_numbers():
    a = int(raw_input("A: "))
    b = int(raw_input("B: "))
    
    return a, b

n = raw_input("Come ti chiami? ")
say_hello(n)

a, b = ask_numbers()

sum_result = make_sum(a, b)
division_result = make_division(float(a), b)


print "Risultato somma: ", sum_result
print "Risultato divisione: ", division_result
