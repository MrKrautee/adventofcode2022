# How much calories are carried by the elf carrying most cals? (here 24000)
# TASK: Find elf carrying most calories. How many cals is it carrying?
import pdb
def func():
    sum = 0
    i = 0
    elveCalDict = {}
    with open ('puzzle_cw.txt') as f:
        for char in f:
            if char == '\n':
                elveCalDict[i] = sum
                sum = 0
                i += 1

            else:
                sum += int(char)
        key = max(elveCalDict, key=elveCalDict.get)
        max_cal = elveCalDict[key]
        print("Elve carrying most calories:",key,"\nCarrying {} calories.".format(max_cal))

if __name__ == "__main__":

    ### RUN CODE
    func()
