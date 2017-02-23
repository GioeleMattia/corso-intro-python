print "Come ti chiami?"
name = raw_input()

print "Ciao %s. Quanti anni hai?" % name
age = int(raw_input())

print "Perfetto %s di %s anni" %(name, age)

print """
Ecco cosa mi hai detto:
nome: %s (tipo %s)
eta': %s (tipo %s)
""" % (name, type(name), age, type(age))

bdate = 2017 - age

print "Quindi sei nato nel", bdate

place = raw_input("Dove sei nato? ")

print "Non e' lontana", place


