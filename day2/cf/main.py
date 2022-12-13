# day 2

oponent = ["A", "B", "C"] # Rock, Paper, Scissors
me = ["X", "Y", "Z"] # Rock, Paper, Scissors
# score 1 Rock, 2 Paper, 3 Scissors
# score is index + 1

defeatMap = {"X": "C",
             "Y": "A",
             "Z": "B"}

def assignInput(letters):
    letters = letters.strip()
    choices = letters.split(" ")
    return (choices[0], choices[1])

def evaluateScore(letters):
    oponentsCh, myChoice = assignInput(letters) 
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

# part 2
# x means lose, y means draw, z means win

def evaluateSecretChoices(letters):
    oponentsCh, myChoice = assignInput(letters)
    winCh = [k for k, v in defeatMap.items() if v == oponentsCh][0]
    drawChIdx = oponent.index(oponentsCh)
    options = {"X" : [k for k in me if k != winCh and me.index(k) != drawChIdx][0],
               "Y" : me[oponent.index(oponentsCh)],
               "Z" : winCh}
    return f"{oponentsCh} {options[myChoice]}"

secretGameLines = map(evaluateSecretChoices, lines)
secretScore = sum(list(map(evaluateScore, secretGameLines)))
print(f"my secret score: {secretScore}")
