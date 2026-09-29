volume = float(input("Введите объем раствора: "))
mass = volume * 0.009
water_volume = volume
with open("recipe.txt", "w") as recipe:
    recipe.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    recipe.write(f"-"*30)
    recipe.write('\n')
    recipe.write(f"Общий объем: {volume} мл\n")
    recipe.write(f'Масса соли: {mass} г\n')
    recipe.write(f'Объем воды: {water_volume} мл\n')
recipe.close()
