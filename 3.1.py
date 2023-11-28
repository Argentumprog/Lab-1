import os
with open("venv/F1.txt", "w") as f1:
    print("Введите данные для файла. Для завершения введите пустую строку")

    while True:
        line=input()
        if not line:
            break
        f1.write(line+'\n')

with open("venv/F1.txt", "r") as f1,open("venv/F2.txt", "w") as f2:
    lines=f1.readlines()
    ev_lines=[line for i, line in enumerate(lines, start=1) if i % 2 == 0]
    f2.writelines(ev_lines)

size_f1=os.path.getsize("venv/F1.txt")
size_f2=os.path.getsize("venv/F2.txt")

print("Размер перрого:",size_f1,"\nРазмер второго:",size_f2)