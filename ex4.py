import random
words = []      #λιστα στην οποια μεταφερονται οι λεξεις της συμβολοσειρας
triades = []    #λιστα στην οποια μεταφερονται οι λεξεις τις λιστας words χωρισμενες σε τριαδες
f = open("ex4.txt")
text = f.read()
f.close()
print(text)
s = "" #μεταβλητη οπου ενωνει τα γραμματα για να δημιουργηθουν οι λεξεις
#k = 0  #μετρητης κενων διαστηματων
i = 0
n = len(text)
while i < 3:
    for j in range(int(n)):
        if (len(text) > 0 and text[0] != " ") and (len(text) > 0 and text[0] != ",") and (
                len(text) > 0 and text[0] != "."):
            s += text[0]
            text = text[1:]

        elif (len(text) > 0 and text[0] == " ") or (len(text) > 0 and text[0] == ",") or (
                len(text) > 0 and text[0] == "."):
            words.append(s)
            i += 1
            s = ""
            text = text[1:]
            #k += 1
            #if k == 3:
            #    k = 0
            if len(words) == 3:
                triades.append(words[0:3])
                del words[0:]
print(text)
print(triades)
ran = random.choice(triades)
ran = ran[1:]  #οι 2 τελευταιες λεξεις μιας τυχαιας 3αδας οπου θα αρχιζει το κειμενο
print(ran)
rtext = ""  #string για τη μετατροπη του κειμενου απο λιστες σε string
for i in range(len(triades)):
    ran += random.choice(triades)
for i in range(len(ran)):
    rtext += str(ran[i])
    rtext += " "
print(rtext)


