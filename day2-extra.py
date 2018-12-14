file = open("day2-input.txt", "r") 
content = file.readlines()

def locate(content):
    for box1 in content:
        for box2 in content:
        
            same_chars = [i[0] for i in zip(box1, box2) if i[0] == i[1]]

            if len(same_chars) == len(box1)-1:
                print(''.join(same_chars))
                return

locate(content)