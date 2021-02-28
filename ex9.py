import math
times = 0  #μετραει ποσες φορες επαναλαμβανεται ενας συγκεγκριμενος χαρακτηρας
monoi = 0  #μετραει το πληθος των μονων χαρακτηρων ωστε να βρω τα ποσοστα στο τελος
counter = []  #βοηθητικη λιστα οπου μπαινουν ολοι οι μονοι χαρακτηρες απο μια φορα
f = open('ex4.txt')
text = f.read()
f.close()
#print(text)
for i in range(len(text)):
    c = text[i]  #επιλεγει ακριβως εναν χαρακτηρα μεσα απο τη λιστα
    #print(ord(c))
    if ord(c) % 2 != 0:
        #print("To", ord(c), "einai monos")
        monoi += 1
        if c not in counter:
            counter.append(c)
    c = ""
#print(counter)
for i in range(len(counter)):
    for j in range(len(text)):
        if counter[i] == text[j]:
            times += 1
    print(counter[i], ":", math.ceil((times/monoi)*100)*"*")
    times = 0
