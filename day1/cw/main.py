# How much calories are carried by the elf carrying most cals? (here 24000)
# TASK: Find elf carrying most calories. How many cals is it carrying?

def func():
    sum = 0
    i = 0
    elveCalDict = {}
    with open ('../puzzle1.txt') as f:
        for char in f:
            if char == '\n':
                elveCalDict[i] = sum
                sum = 0
                i += 1

            else:
                sum += int(char)

        key = max(elveCalDict, key=elveCalDict.get)
        max_cal = elveCalDict[key]

if __name__ == "__main__":

    ### RUN CODE
    func()
