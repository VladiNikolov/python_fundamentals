company_dict = {}

while True:
    command = input()
    if command == "End":
        break
    else:
        data_info = command.split(" -> ")
        company_name = data_info[0]
        company_id = data_info[1]

        if company_name not in company_dict:
            company_dict[company_name] = []
            company_dict[company_name].append(company_id)
        else:
            if company_id in company_dict[company_name]:
                continue
            company_dict[company_name].append(company_id)
for key, value in company_dict.items():
    print(f"{key}")
    for id in value:
        print(f"-- {id}")
