dlist = [ {"James":"Sean", "director":"Terence"}, {"James":"Roger", "director":"Lewis"}, {"James":"Pierce","director":"Roger"} ]
k = "James"

#Plocka ut dictionariet ur listan, eller nå den i listan,
# Plocka ut varje dictionary ur listan
# Välj nyckel för nuvarande dictionary
# Spara värdet för nyckeln i en ny lista
# dlist[i]{k]

# Med en for loop
for i in range(len(dlist)):
    print(dlist[i][k])

# Med comprehension
flist = [dlist[i][k] for i in range(len(dlist))]
print(flist)