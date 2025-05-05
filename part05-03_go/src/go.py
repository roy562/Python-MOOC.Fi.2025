# Write your solution here
def who_won(game_board: list):
    count_1=0
    count_2=0

    for row in game_board:
        count_1+= row.count(1)
        count_2+= row.count(2)

    print( count_1, count_2)
    if count_1 > count_2:
        return 1
    elif count_2 > count_1:
        return 2
    else:
        return 0


if __name__ == "__main__":
    go = [
        [1, 0, 2, 0, 2, 0, 1, 0, 1],
        [0, 2, 0, 2, 1, 1, 2, 0, 1],
        [0, 2, 0, 1, 1, 1, 2, 0, 2],
        [0, 1, 1, 2, 2, 2, 0, 1, 0],
        [0, 0, 1, 1, 2, 0, 2, 1, 0],
        [2, 0, 2, 2, 1, 0, 1, 0, 0],
        [0, 0, 2, 1, 0, 1, 2, 0, 0],
        [1, 0, 1, 2, 0, 1, 1, 0, 1],
        [2, 0, 1, 0, 0, 0, 0, 1, 2]
        ]
    print(who_won(go))