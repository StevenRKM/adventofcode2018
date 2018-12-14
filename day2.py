file = open("day2-input.txt", "r") 
content = file.readlines()

# content = [
#     'abcdef', 
#     'bababc', 
#     'abbcde', 
#     'abcccd', 
#     'aabcdd', 
#     'abcdee', 
#     'ababab', 
# ]

# abcdef contains no letters that appear exactly two or three times.
# bababc contains two a and three b, so it counts for both.
# abbcde contains two b, but no letter appears exactly three times.
# abcccd contains three c, but no letter appears exactly two times.
# aabcdd contains two a and two d, but it only counts once.
# abcdee contains two e.
# ababab contains three a and three b, but it only counts once.

# Of these box IDs, four of them contain a letter which appears exactly twice, 
# and three of them contain a letter which appears exactly three times. 
# Multiplying these together produces a checksum of 4 * 3 = 12.

# [ (c, s.count(c)) for c in set(s)]
# bool([i for i in x if i[1] == 2])

count2 = 0
count3 = 0

for box in content:
    counts = [ box.count(c) for c in set(box)]
    if 2 in counts:
        count2 += 1
    if 3 in counts:
        count3 += 1

print(count2 * count3)