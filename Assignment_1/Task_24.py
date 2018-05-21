base = 10
digits = {range(10)}

# Base the first value in tuple on the fact that it we throw the remainder, and use //
# % modulo can be thought of as returning the value, when no more division is possible.
# Last value is therefore capped at 9, and always returning the current iteration being capped at 9
# Same goes for the second, we're basicly just capping the values with %. so as not to get 999:(9,99,999)
# but instead 999:(9,9,9)

base_dic = { i:(i // base**2, (i // base) % base, i % base ) for i in range(base**3)}
print(base_dic)


# what = 4 % 5
# print(what)