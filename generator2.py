#Create a generator that yields "n" random numbers between a low and high number (that are inputs).

import random


def rand_num(low,high,n):
    for i in range(n):
        print("yield se pehle wala code")
        yield random.randint(low, high)
        print("violla")


for num in rand_num(1,10,12):
    print(num)

s = 'hello'
s_iter = iter(s)

print(next(s_iter))
print(s_iter.__next__())
print(s_iter.__next__())
print(s_iter.__next__())
print(s_iter.__next__())