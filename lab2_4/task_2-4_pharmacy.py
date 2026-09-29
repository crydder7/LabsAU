number = int(input("Введите количество произведенных капсул: "))
capacity = int(input("Введите вместимость одной упаковки(ШТ): "))
number_of_packs = number // capacity
number_of_left = number % capacity
print(f"---Отчет фасовочного цеха---\nПолных упаковок: {number_of_packs}\nОстаток капсул: {number_of_left}")
