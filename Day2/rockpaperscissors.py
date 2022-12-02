#!/bin/python

#A = "ROCK"
#B = "PAPER"
#C = "SCISSORS"

#X = "ROCK"
#Y = "PAPER"
#Z = "SCISSORS"

# 1 for Rock, 2 for Paper, 3 for Scissors
# 0 for Loss, 3 for Draw, 6 for Win


scores = {}
scores["A"] = {}
scores["A"]["X"] = 4 # Rock + Draw = 1 + 4
scores["A"]["Y"] = 8 # Paper + Win = 2 + 6
scores["A"]["Z"] = 3 # Scissors + Loss = 3 + 0
scores["B"] = {}
scores["B"]["X"] = 1 # Rock + Loss = 1 + 0
scores["B"]["Y"] = 5 # Paper + Draw = 2 + 3
scores["B"]["Z"] = 9 # Scissors + Win = 3 + 6
scores["C"] = {}
scores["C"]["X"] = 7 # Rock + Win = 1 + 6
scores["C"]["Y"] = 2 # Paper + Loss = 2 + 0
scores["C"]["Z"] = 6 # Scissors + Draw = 3 + 3

scoresroundtwo = {}
scoresroundtwo["A"] = {}
scoresroundtwo["A"]["X"] = 3 # Scissors + Loss = 3 + 0
scoresroundtwo["A"]["Y"] = 4 # Rock + Draw = 1 + 3
scoresroundtwo["A"]["Z"] = 8 # Paper + Win = 2 + 6
scoresroundtwo["B"] = {}
scoresroundtwo["B"]["X"] = 1 # Rock + Loss = 1
scoresroundtwo["B"]["Y"] = 5 # Paper + Draw = 2 + 3
scoresroundtwo["B"]["Z"] = 9 # Scissors + Win = 3 + 6
scoresroundtwo["C"] = {}
scoresroundtwo["C"]["X"] = 2 # Paper + Loss = 2
scoresroundtwo["C"]["Y"] = 6 # Scissors + Draw = 3 + 3
scoresroundtwo["C"]["Z"] = 7 # Rock + Win = 1 + 6

Score = 0
Scoreroundtwo = 0

with open("inputrps.txt", "r") as inFile:
    for inLine in inFile:
        (opp, me) = inLine.strip().split(' ')
        Score += scores[opp][me]
        Scoreroundtwo += scoresroundtwo[opp][me]

print(Score)
print(Scoreroundtwo)