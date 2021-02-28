import random
lekseis = []
triades = []
f = open("ask4.txt")
keimeno = f.read()
f.close()
print(keimeno)
s = ""
i = 0
l = len(keimeno)
while i < 3:
    for j in range(int(l)):
        if (len(keimeno) > 0 and keimeno[0] != " ") and (len(keimeno) > 0 and keimeno[0] != ",") and (
                len(keimeno) > 0 and keimeno[0] != "."):
            s += keimeno[0]
            keimeno = keimeno[1:]

        elif (len(keimeno) > 0 and keimeno[0] == " ") or (len(keimeno) > 0 and keimeno[0] == ",") or (
                len(keimeno) > 0 and keimeno[0] == "."):
            lekseis.append(s)
            i += 1
            s = ""
            text = keimeno[1:]
            if len(lekseis) == 3:
                triades.append(keimeno[0:3])
                del keimeno[0:]
print(keimeno)
print(triades)
tux = random.choice(triades)
tux = tux[1:]
print(tux)
rkeimeno = ""
for i in range(len(triades)):
    tux += random.choice(triades)
for i in range(len(tux)):
    rkeimeno += str(tux[i])
    rkeimeno += " "
print(rkeimeno)