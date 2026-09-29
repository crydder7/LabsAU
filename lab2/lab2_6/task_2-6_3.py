donor_blood_group = input("Введите группу крови донора(0,1,2,3,4): ")
recipient_blood_group = input("Введите группу крови реципиента(0,1,2,3,4): ")
if donor_blood_group == recipient_blood_group or donor_blood_group == "0":
    print("Переливание возможно")
else: 
    print("Переливание невозможно")

