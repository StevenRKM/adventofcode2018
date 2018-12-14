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
# claim_sizes = {} # id => size
not_overlapped = set() # set containing each claim that has not been overlapped

claim_format = r"#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)"



for claim in content:
    # parse claim
    match = re.search(claim_format, claim)
    [id, x, y, width, height] = [int(i) for i in match.groups()]

    # claim_sizes[id] = width * height

    not_overlapped.add(id)

    for i in range(x, x+width):
        for j in range(y, y+height):
        
            if grid.get((i,j)) == None:
                # no overlap yet
                grid[(i,j)] = id
            else:
                # overlap
                overlapped_id = grid[(i,j)]
                # remove both ids
                not_overlapped = not_overlapped - {overlapped_id, id}                

print([*not_overlapped][0])

# print({ c:v[0] for c,v in grid.items() if len(v) == 1})
# print({ v[0] for c,v in grid.items() if len(v) == 1})
# vettige en trage oneliner
# print([*{ v[0] for c,v in grid.items() if len({ cc:vv[0] for cc,vv in grid.items() if len(vv) == 1 and vv[0] == v[0]}) == claim_sizes[v[0]]}][0])







