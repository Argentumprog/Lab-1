subjects_dict = {}

with open("F4.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    parts = line.strip().split(":")
    subject = parts[0].strip()
    lesson_counts = [int(count) for count in parts[1].split()]

    total_lessons=sum(lesson_counts)

    subjects_dict[subject] = total_lessons

print("Словарь с количеством занятий по предметам:",subjects_dict)