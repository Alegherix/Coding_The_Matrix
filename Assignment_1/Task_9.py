S = {1, 2, 3, 4}
T = {3, 4, 5, 6}

#Intersektion set utan att få använda &
intersektion_set = {x*y for x in S for y in T if x in T and y in S}
print(intersektion_set)