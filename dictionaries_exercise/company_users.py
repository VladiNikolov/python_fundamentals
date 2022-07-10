company_dict = {}

command = input()
while command != "End":
    current_command = command.split(" -> ")
    company_name = current_command[0]
    company_id = current_command[1]
    if company_name in company_dict.keys():
        if company_id not in company_dict[company_name]:
            company_dict[company_name].append(company_id)
    else:
        company_dict[company_name] = []
        company_dict[company_name].append(company_id)
    command = input()
for company_name in company_dict.keys():
    print(f"{company_name}")
    for employee in company_dict[company_name]:
        print(f"-- {employee}")