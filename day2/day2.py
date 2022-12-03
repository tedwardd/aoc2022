#!/usr/bin/env python3

# input_file = "sample.txt"
input_file = "input.txt"

win = 6
tie = 3
lose = 0

move_values = {"X": 1, "Y": 2, "Z": 3}

move_decoder = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}


def get_result(player1, player2):
    return move_decoder.get(str(player1 + player2))


with open(input_file, "r") as f:
    file_data = f.readlines()

result_scores = []

for round in file_data:
    moves = round.split(" ")
    # print(moves[0])
    # print(moves[1].strip())
    result = get_result(moves[0].strip(), moves[1].strip())
    value = move_values.get(moves[1].strip())
    result_scores.append(result + value)

print(sum(result_scores))
