mot =  str(input("type a word"))
motp = ""
moti = ""
for i in range (len(mot)) :
    if i % 2 == 0 :
        motp += mot[i]
    else :
        moti += mot[i]

print(motp)
print(moti)