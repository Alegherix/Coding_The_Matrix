id2salary = {0:1000.0, 3:990, 1:1200.5}
names = ["Larry","Curly","","Moe"]

salary_dic = {names[k]:v for (k,v) in id2salary.items()}
print(salary_dic)