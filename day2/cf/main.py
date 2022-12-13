# day 2

oponent = ["A", "B", "C"] # Rock, Paper, Scissors
me = ["X", "Y", "Z"] # Rock, Paper, Scissors
# score 1 Rock, 2 Paper, 3 Scissors
# score is index + 1

defeatMap = {"X": "C",
             "Y": "A",
             "Z": "B"}

def evaluateScore(letters):
    letters = letters.strip()
    choices = letters.split(" ")
    myChoice = choices[1]
    oponentsCh = choices[0]
    score = me.index(myChoice) + 1
    if defeatMap[myChoice] == oponentsCh:
        # won
        score += 6
    else:
        # X is equal to A (Rock) -> use index
        if me.index(myChoice) == oponent.index(oponentsCh):
            # draw
            score += 3
        else:
            # lost
            score += 0
    return score

with open("../input.txt", "r") as file:
    lines = file.readlines()

score = sum(list(map(evaluateScore, lines)))
print(f"my score: {score}")

