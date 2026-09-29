name = input("Введите название питательной среды: ")
concentrarion = input("Введите концентрацию агара в процентах: ")
temp = input("Введите температуру стерилизации: ")
with open("recipe.txt", "w") as recipe:
    recipe.write(f"{name}\n".upper())
    recipe.write(f"Концентрация агара(%)\t{concentrarion}")
    recipe.write(f"Температура стерилизации\t{temp}")
print("Файл 'recipe.txt' успешно сформирован!")
