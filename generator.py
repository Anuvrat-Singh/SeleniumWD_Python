#Create a generator that generates the squares of numbers up to some number N.

def gen_squares(N):
    for i in range(N):
        print("yield se pehle ka code")
        yield i**2
        print("Yielded")
        print("subhanallah")

for x in gen_squares(10):
    print(x)