# day 4

def get_range(section):
    s = section.split("-")
    s1 = int(s[0])
    s2 = int(s[1])
    return range(s1, s2+1)

def count_overlapped(sections_str):
    sections = sections_str.strip().split(",")
    s1_str_t = ".".join([str(i) for i in get_range(sections[0])])
    s1_str = f".{s1_str_t}."
    s2_str_t = ".".join([str(i) for i in get_range(sections[1])])
    s2_str = f".{s2_str_t}."
    if s1_str in s2_str or s2_str in s1_str:
        return 1
    else:
        return 0

def count_alloverlapped(sections_str):
    sections = sections_str.strip().split(",")
    range1 = get_range(sections[0])
    range2 = get_range(sections[1])
    for s in range1:
        if s in range2:
            return 1
    return 0

with open("../input.txt", "r") as file:
    lines = file.readlines()

overlap_sum = sum(list(map(count_overlapped, lines)))
print(f"overlapped sections {overlap_sum}")

overlapall_sum = sum(list(map(count_alloverlapped, lines)))
print(f"all overlapped sections {overlapall_sum}")
