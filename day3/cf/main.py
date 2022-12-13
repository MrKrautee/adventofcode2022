# day 3

def prio(letter):
    prio = ord(letter) - 96
    if prio > 0:
        return prio
    else:
        return ord(letter) - 38

def check_rucksack(rucksack):
    count = len(rucksack.strip())
    half = int(count / 2)
    compartment1 = rucksack[0:half]
    compartment2 = rucksack[half:count]
    for item in compartment1:
        if item in compartment2:
            return prio(item)

with open("../input.txt", "r") as file:
    lines = file.readlines()

prio_sum = sum(list(map(check_rucksack, lines)))
print(f"prio sum: {prio_sum}")
