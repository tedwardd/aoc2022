#!/usr/bin/env python3

# input_file = "sample.txt"
input_file = "input.txt"

win = 6
tie = 3
lose = 0

rock = 1
paper = 2
scissors = 3

A = rock
B = paper
C = scissors

X = rock
Y = paper
Z = scissors

move_values = {"X": 0, "Y": 3, "Z": 6}

move_decoder = {
    "AX": 3,
    "AY": 1,
    "AZ": 2,
    "BX": 1,
    "BY": 2,
    "BZ": 3,
    "CX": 2,
    "CY": 3,
    "CZ": 1,
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
    score = result + value
    print(score)
    result_scores.append(score)

print(sum(result_scores))
