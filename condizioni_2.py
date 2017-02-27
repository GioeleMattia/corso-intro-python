from funzioni import make_sum, make_division, ask_numbers

a, b = ask_numbers()

operation = raw_input("Che operazioe vuoi fare (+ o /)")

if operation == "+":
    print make_sum(a, b)
elif operation == "/":
    print make_division(a, b)
else:
    print "Non so fare %s" %operation
