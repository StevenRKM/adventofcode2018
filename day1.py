file = open("day1-input.txt", "r") 
content = file.readlines()

x = sum([int(i) for i in content])

print(x)