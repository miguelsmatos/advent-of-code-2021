FILENAME = "input.txt"

numbers = []
boards = []
min_numbers = 0

with open(FILENAME, "r") as fo:
    r = fo.readline()
    numbers = [int(d) for d in r.split(",")]
    new_board = []
    for line in fo:
        row = [int(d) for d in line.split()]
        if len(row) == 0:
            if new_board:
                boards.append(new_board)
                assert len(new_board) == 5
                new_board = []
        else:
            assert len(row) == 5
            new_board.append(row)
    if new_board:
        boards.append(new_board)

min_numbers = len(boards[0][0])

print(f"Playing with {len(boards)} boards and {len(numbers)} numbers")

winner_boards = [False for _ in boards]

for i, n in enumerate(numbers):
    print(f"Number {n}")
    if i < 4:
        continue
    selection = numbers[0 : i + 1]
    winner_count = 0
    for _b, board in enumerate(boards):
        counts_per_row = [0, 0, 0, 0, 0]
        counts_per_column = [0, 0, 0, 0, 0]
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                counts_per_row[r] += val in selection
                counts_per_column[c] += val in selection
        win = any(r == 5 for r in counts_per_row) or any (c == 5 for c in counts_per_column)
        if win and not winner_boards[_b]:
            winner_count += 1
            unmarked_sum = sum((s for row in board for s in row if s not in selection))
            score = unmarked_sum * n
            print(f'Winner! Board {_b} with {i+1} numbers and score {score}')
            print(f'--> Sum {unmarked_sum}; number {n}')
            winner_boards[_b] = True
            # break
    if all(winner_boards):
        break
    # if winner_count:
    #     break

print(f"Last to win was board {_b} with score {score}")

