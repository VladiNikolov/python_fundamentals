employees_happyness = [int(el) for el in input().split()]
happyness_factor = int(input())

happynes = [el* happyness_factor for el in employees_happyness]
threshold = sum(happynes) / len(happynes)

happy_employees = [el for el in happynes if el >= threshold]
sad_employees = [el for el in happynes if el < threshold]
happy_message = "Employees are happy!"
sad_message = "Employees are not happy!"

if len(sad_employees) > len(happynes) / 2:
    print(f"Score: {len(happy_employees)}/{len(happynes)}. {sad_message}")
else:
    print(f"Score: {len(happy_employees)}/{len(happynes)}. {happy_message}")
