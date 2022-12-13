# advent of code 2022 

calsPerElf = []
with open("../puzzle1.txt", "r") as file:
    lines = file.readlines()
    sum4One = 0
    for line in lines:
        if line == "\n": # next elf
            calsPerElf.append(sum4One) # save prev elfs cals
            sum4One = 0
        else:
            sum4One += int(line)

# (part1) who has the most?
print("Part 1:")
print(f"\tmost cals: {max(calsPerElf)}")

# (part2) sum of the top3 
calsPerElf.sort(reverse=True)
sumTop3 = sum(calsPerElf[0:3])
print("Part 2:")
print(f"\tsum top3: {sumTop3}")
