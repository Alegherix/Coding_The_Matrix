dlist = [ {"Bilbo":"Ian","Frodo":"Elijah"},{"Bilbo":"Martin","Thorin":"Richard" } ]
k = "Frodo"
k = "Bilbo"

#Fungerande utan Comprehension
add_list = []
for i in range(len(dlist)):
    if k in dlist[i]:
        add_list.append(dlist[i][k])
    else:
        add_list.append("NOT PRESENT")

print(add_list)

#Sätt standardvärde om nyckeln inte finns
comp_list = [dlist[i].get(k, "NOT PRESENT") for i in range(len(dlist))]
print(comp_list)