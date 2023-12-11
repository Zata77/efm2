def triee (tab) :
    for b in range (len(tab)) :
        for i in range (b+1, len(tab)) :
            if tab[b] < tab[i] :
                h=tab[b]
                tab[b]=tab[i]
                tab[i]=h
    return tab

def Afficher (tab) :
    print(tab)

tab=[8, 6 , 14, 25, 0, -1, -100, 15]
tab1 = triee(tab)

Afficher(tab1)