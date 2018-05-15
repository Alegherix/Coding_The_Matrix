nine_element_set = {x*y for x in {1,3,5} for y in {3,7,10}}
print(len(nine_element_set))

{x*y for x in {1, 2, 3} for y in {1, 2, 3} if x != y}