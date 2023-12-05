subjects_dict = {}

with open("F4.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    parts = line.strip().split(":")
    subject = parts[0].strip()
    str_num = parts[1].split()
    str = []
    i = 0
    for par in str_num:
        str_12 = str_num[i].split("(")
        str.append(str_12[0])
        i = i + 1
    lesson_counts = [int(count) for count in str]

    total_lessons=sum(lesson_counts)

    subjects_dict[subject] = total_lessons

print("Словарь с количеством занятий по предметам:",subjects_dict)