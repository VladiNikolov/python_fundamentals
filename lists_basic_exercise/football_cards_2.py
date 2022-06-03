input_players = input().split()

team_a = []
team_b = []
is_game_over = False
for num in range(1, 11 + 1):
    team_a.append(f"A-{num}")
    team_b.append(f"B-{num}")

for player in input_players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        is_game_over = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if is_game_over:
    print("Game was terminated")


