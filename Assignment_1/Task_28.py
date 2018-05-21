dct={"a":"A", "b":"B", "c":"C"}
keylist = ["b","c","a"]

def dict2list(dct,keylist):
    return [dct[v] for v in keylist]

output = dict2list(dct,keylist)
print(output)