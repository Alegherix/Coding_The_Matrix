odd_number_set = {i for i in range(1,100,2)}
odd_number_set_two = { i+1 for i in range(0,100,2)}
odd_number_set_three = { i for i in range(100) if i % 2 == 1}
print(odd_number_set)
print(odd_number_set_two)
print(odd_number_set_three)