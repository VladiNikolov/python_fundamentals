# input_players = input().split()
#
# list_team_a = []
# list_team_b = []
# game_was_terminated = False
#
# for i in range(1, 11 + 1):
#     list_team_a.append(f"A-{i}")
#     list_team_b.append(f"B-{i}")
#
# for player in input_players:
#     if player in list_team_a:
#         list_team_a.remove(player)
#     elif player in list_team_b:
#         list_team_b.remove(player)
#
#     if len(list_team_a) < 7 or len(list_team_b) < 7:
#         game_was_terminated = True
#         break
#
# print(f"Team A - {len(list_team_a)}; Team B - {len(list_team_b)}")
# if game_was_terminated:
#     print("Game was terminated")
#
#------------------------------------------------------------------------
#
input_players = input().split()
teamA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
teamB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
is_match_is_over = False

for current_number in input_players:
    info_player = current_number.split("-")
    team = info_player[0]
    player_number = int(info_player[1])

    if team == "A" and player_number in teamA:
        teamA.remove(player_number)
    elif team == "B" and player_number in teamB:
        teamB.remove(player_number)

    if len(teamA) < 7 or len(teamB) < 7:
        is_match_is_over = True
        break
print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")
if is_match_is_over:
    print("Game was terminated")
