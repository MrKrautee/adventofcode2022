# day 4

def count_overlapped(sections_str):
    sections = sections_str.strip().split(",")

    s1 = sections[0].split("-")
    s11 = int(s1[0])
    s12 = int(s1[1])
    s1_str_t = ".".join([str(i) for i in range(s11, s12+1)])
    s1_str = f".{s1_str_t}."

    s2 = sections[1].split("-")
    s21 = int(s2[0])
    s22 = int(s2[1])
    s2_str_t = ".".join([str(i) for i in range(s21, s22+1)])
    s2_str = f".{s2_str_t}."

    if s1_str in s2_str or s2_str in s1_str:
        return 1
    else:
        return 0

with open("../input.txt", "r") as file:
    lines = file.readlines()

overlap_sum = sum(list(map(count_overlapped, lines)))
print(f"overlapped sections {overlap_sum}")
