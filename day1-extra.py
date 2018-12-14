file = open("day1-input.txt", "r") 
content = file.readlines()

ints = [int(i) for i in content]

# ints = [1,2,-2,5]     # 0,1,3,1,.. : 1 in first loop
# ints = [1,2,3,-7]     # 0,1,3,6,-1,0,.. : 0 in second loop
# ints = [1,2,3,-8]       # 0,1,3,6,-2,-1,1,..  : 1 in second loop

current = 0
index = 0

seen = [0]

while True:

    change = ints[index]

    current += change

    if current in seen:
        print(current)
        break

    # print(current)

    seen.append(current)

    index += 1
    index = index % len(ints)