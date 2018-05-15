# print({2*x for x in {1,2,3}})

#Set comprehension med union
S = {1, 3}
set_union = {x*x for x in S | {5,7}}
print(set_union)

#Kan lägga till if statement inuti comprehensionen.
set_union = {x * x for x in S | {5, 7} if x > 2 and x<7}
print(set_union)

#Comprehension för den Kartesiska produkten av två set
cartesian_set ={x*y for x in {1, 2, 3} for y in {2, 3, 4}}
print(cartesian_set)

