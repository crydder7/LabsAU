full_name = input("Введите ФИО: ")
date = input("Введите дату: ")
name_of_experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")
len = len(full_name) * 2
angle = "+"
floor = "-" * len + 1
wall = "|"
with open("journal.txt", "w") as journal:
    journal.write(f'{angle}{floor}{angle}\n')
    journal.write(f'{wall}\tФИО исследователя: {full_name}\t{wall}\n')
    journal.write(f'{wall}\tДата: {date}\t{wall}\n')
    journal.write(f'{wall}\tНазвание эксперимента: {name_of_experiment}\t{wall}\n')
    journal.write(f'{angle}{floor}{angle}\n')
    journal.write(f'{wall}\tВывод: {conclusion}\t{wall}\n')
    journal.write(f'{angle}{floor}{angle}\n')
