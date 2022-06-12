first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))
third_row = list(map(int, input().split()))
player = " "
is_draw = False
# by_rows

if first_row[0] == first_row[1] == first_row[2]:
    if first_row[0] == 1:
        player = "First"
    elif first_row[0] == 2:
        player = "Second"
    else:
        is_draw = True
elif second_row[0] == second_row[1] == second_row[2]:
    if second_row[0] == 1:
        player = "First"
    elif second_row[0] == 2:
        player = "Second"
    else:
        is_draw = True
elif third_row[0] == third_row[1] == third_row[2]:
    if third_row[0] == 1:
        player = "First"
    elif third_row[0] == 2:
        player = "Second"
    else:
        is_draw = True

# by_cols

elif first_row[0] == second_row[0] == third_row[0]:
    if first_row[0] == 1:
        player = "First"
    elif first_row[0] == 2:
        player = "Second"
    else:
        is_draw = True
elif first_row[1] == second_row[1] == third_row[1]:
    if first_row[1] == 1:
        player = "First"
    elif first_row[1] == 2:
        player = "Second"
    else:
        is_draw = True
elif first_row[2] == second_row[2] == third_row[2]:
    if first_row[2] == 1:
        player = "First"
    elif first_row[2] == 2:
        player = "Second"
    else:
        is_draw = True

# by_left_diagonal

elif first_row[0] == second_row[1] == third_row[2]:
    if first_row[0] == 1:
        player = "First"
    elif first_row[0] == 2:
        player = "Second"
    else:
        is_draw = True
# by_right_diagonal
elif first_row[2] == second_row[1] == third_row[0]:
    if first_row[2] == 1:
        player = "First"
    elif first_row[2] == 2:
        player = "Second"
    else:
        is_draw = True
# draw
else:
    is_draw = True
if is_draw:
    print("Draw!")
else:
    print(f"{player} player won")


