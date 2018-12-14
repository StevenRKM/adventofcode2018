import re

file = open("day2-input.txt", "r") 
content = file.readlines()

# content = [
#     '#1 @ 1,3: 4x4',
#     '#2 @ 3,1: 4x4',
#     '#3 @ 5,5: 2x2',
# ]

# #id @ left,top: width x height

# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........

grid = {} # coords (x,y) => count of ids

claim_format = r"#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)"

for claim in content:
    # parse claim
    match = re.search(claim_format, claim)
    [id, x, y, width, height] = [int(i) for i in match.groups()]

    for i in range(x, x+width):
        for j in range(y, y+height):

            grid.setdefault((i,j), 0)
            grid[(i,j)] += 1  

print(len({ c:v for c,v in grid.items() if v > 1}))







