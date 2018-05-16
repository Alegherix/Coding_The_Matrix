s = {-4, -2, 1, 2, 5, 0}
#Modifierad för 14 och 15 med sista if
list_answer = [(i,j,k) for i in s for j in s for k in s if sum((i,j,k))==0 if not (i,j,k) == (0,0,0)][0]
print(list_answer)