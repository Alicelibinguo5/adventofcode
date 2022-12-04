# --- Day 4: Camp Cleanup ---
# Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.
#
# However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort,
# the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).
#
# For example, consider the following list of section assignment pairs:
#
pairs_str_1="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
# For the first few pairs, this list means:
#
# Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
# The Elves in the second pair were each assigned two sections.
# The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
# This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:
#
# Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6.
# In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

###PART 1###
# In how many assignment pairs does one range fully contain the other?

def generate_pair_list(input_list):
    input_list = input_list.split("\n")
    list_1 = [tuple(pairs.split(",")) for pairs in input_list]
    list_2 = [(list(pair[0].split("-")), list(pair[1].split("-"))) for pair in list_1]
    output_list = [([p1 for p1 in range(int(pair1[0]), int(pair1[1])+1)],
                    [p2 for p2 in range(int(pair2[0]), int(pair2[1])+1) ]) \
                   for (pair1, pair2) in list_2]

    return output_list


def camp_cleanup_part1(pairs_str):
    if not pairs_str:
        return 0

    nums_pairs = 0
    pairs_list = generate_pair_list(pairs_str)
    # print(pairs_list)
    for (p1, p2) in pairs_list:
        if (set(p1).issubset(set(p2))) or set(p2).issubset(set(p1)):
            nums_pairs += 1

    return nums_pairs
##Part 2
def camp_cleanup_part2(pairs_str):
    if not pairs_str:
        return 0

    nums_pairs = 0
    pairs_list = generate_pair_list(pairs_str)
    # print(pairs_list)
    for (p1, p2) in pairs_list:
        if any(i for i in p1 if i in p2):
            nums_pairs += 1

    return nums_pairs

###OUTPUT
nums_pairs_1 = camp_cleanup_part1(pairs_str_1)
print(f"part 1 example result: {nums_pairs_1}")
nums_pairs_1 = camp_cleanup_part2(pairs_str_1)
print(f"part 2 example result: {nums_pairs_1}")

with open("day4.txt", 'r') as file:
    pairs_str_2 = file.read().rstrip()
nums_pairs_2 = camp_cleanup_part1(pairs_str_2)
print(f"part 1 actual result: {nums_pairs_2}")
nums_pairs_2 = camp_cleanup_part2(pairs_str_2)
print(f"part 2 actual result: {nums_pairs_2}")


