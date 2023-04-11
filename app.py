import random

wl = []
wa = ""
password = ""
password_len = 12

while len(wl) < 4:
    w = input("Please enter 4 words, symbols or numbers \n")
    wl.append(w)
    
for i in wl:
    wa = wa + i
    
for x in range(password_len):
    password = password + random.choice(wa)

print(password)
