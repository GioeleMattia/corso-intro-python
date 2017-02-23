# qui sto salutando mamma e nonna
print "Ciao mamma", "Ciao nonna"
print 3, 12
print 3.12 # questo e' un numero in virgola mobile
print True

print 3 + 10
print 3 - 4
print 3 * 2
print 3 / 2
print 3 % 2

print 3 > 4

print 3 < 10

name = "Gioele"
age = 18
delta = 5
template = "Ciao, mi chiamo %s e %s anni fa avevo %s anni"

sentence1 = "Ciao mamma guarda"
sentence2 = "come mi diverto"


print "Ciao, mi chiamo %s e ho %s anni" % (name, age)
print "Ciao, sono %s" % name

print "Ciao, mi chiamo %s e 10 anni fa avevo %s anni" % (name, age -10)

print "Ciao, mi chiamo %s e %s anni fa avevo %s anni" % (name, delta, age - delta)

print template % (name, delta, age - delta)

print sentence1 + " " + sentence2

print """
Lorem ipsum
dolor sit amet
"""

print "Ciao, \n Mi chiamo Gioele \n \n e ho 18 anni."


