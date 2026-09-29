height = float(input("Введите ваш рост(М): "))
weight = float(input("Введите ващ вес(КГ): "))
bmi = weight / (height ** 2)
print(f'---Отчет о состоянии здоровья---\nРост: {height}\nВес: {weight}\nИндекс массы тела: {bmi}')
