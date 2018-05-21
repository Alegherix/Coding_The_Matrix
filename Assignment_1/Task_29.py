L = ["A","B","C"]
keylist= ["a","b","c"]


def list2dic(L, keylist):
    return {k:v for k,v in zip(keylist,L)}

print(list2dic(L,keylist))