name = input("Введите имя оператора: ")
pressure = input("Введите текущее значение датчика давления: ")
with open("sensor_log.txt", "w") as file:
    file.write(f"Name\t{name}")
    file.write(f"Pressure\t{pressure}")
print("Данные успешно сохранены в sensor_log.txt ")
