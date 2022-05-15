input_players = input().split()

list_team_a = []
list_team_b = []
game_was_terminated = False

for i in range(1, 11 + 1):
    list_team_a.append(f"A-{i}")
    list_team_b.append(f"B-{i}")

for player in input_players:
    if player in list_team_a:
        list_team_a.remove(player)
    elif player in list_team_b:
        list_team_b.remove(player)

    if len(list_team_a) < 7 or len(list_team_b) < 7:
        game_was_terminated = True
        break

print(f"Team A - {len(list_team_a)}; Team B - {len(list_team_b)}")
if game_was_terminated:
    print("Game was terminated")