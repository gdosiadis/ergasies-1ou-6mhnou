from random import seed
from random import randint
p = int(input("oros fibonacci:"))  #εισαγωγη ορου απο τον χρηστη
a = randint(0, 1000)
for i in range(20):  #20 τυχαιες επιλογες του α
    print((a**p) % p)
    if ((a**p) % p) % 2 != 0:
        print("Odd")
    else:
        print("Even")
    a = randint(0, 1000)

