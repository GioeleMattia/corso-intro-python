from funzioni import make_sum

numbers = [1, 5, 7, 1123, 14144, 56, 6]

for n in numbers:
    print n

count = 0 
for n in numbers:
    print "elemento %s : %s" % (count, n)
    count += 1

numbers = []

for n in range(0,10):
    numbers.append(make_sum(n,2))

print numbers
