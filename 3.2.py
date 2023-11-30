import os
with open("F3.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

names = []
salaries = []

for line in lines:
    name, salary = line.split()
    names.append(name)
    salaries.append(float(salary))

poor=[names[i] for i in range(len(salaries)) if salaries[i]<20000]

print("Зарплата меньше 20000 у:",','.join(poor))

av_salary= sum(salaries)/len(salaries)

print("Средняя зарплата:", av_salary)