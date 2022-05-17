# input_lines = input().split(" ")
#
# players_in_team_a = 11
# players_in_team_b = 11
# player_losses_list = []
# condition = False
#
# for current_number in input_lines:
#     if current_number not in player_losses_list:
#         player_losses_list.append(current_number)
#         if "A" in current_number:
#             players_in_team_a -= 1
#         elif "B" in current_number:
#             players_in_team_b -= 1
#
#         if players_in_team_a < 7 or players_in_team_b < 7:
#             condition = True
#             break
#
# print(f"Team A - {players_in_team_a}; Team B - {players_in_team_b}")
# if condition:
#     print("Game was terminated")
#
#---------------------------------------------------------------------
#
input_str = input().split()
team_list_a = []
team_list_b = []
game_over = False
for number in range(1, 11 + 1):
    team_list_a.append(f"A-{number}")
    team_list_b.append(f"B-{number}")
for player in input_str:
    if player in team_list_a:
        team_list_a.remove(player)
    elif player in team_list_b:
        team_list_b.remove(player)

    if len(team_list_a) < 7 or len(team_list_b) < 7:
        game_over = True
        break
print(f"Team A - {len(team_list_a)}; Team B - {len(team_list_b)}")
if game_over:
    print("Game was terminated")