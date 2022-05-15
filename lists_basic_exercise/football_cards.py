input_lines = input().split(" ")

players_in_team_a = 11
players_in_team_b = 11
player_losses_list = []
condition = False

for current_number in input_lines:
    if current_number not in player_losses_list:
        player_losses_list.append(current_number)
        if "A" in current_number:
            players_in_team_a -= 1
        elif "B" in current_number:
            players_in_team_b -= 1

        if players_in_team_a < 7 or players_in_team_b < 7:
            condition = True
            break

print(f"Team A - {players_in_team_a}; Team B - {players_in_team_b}")
if condition:
    print("Game was terminated")

