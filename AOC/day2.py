def position(file):
    with open(file, 'r', encoding="utf-8") as f:
        horizontal = 0
        depth = 0
        for line in f:
            token = [x.strip() for x in line.split()]
            command = token[0]
            value = int(token[1])
            if command == "forward":
                horizontal += value
            elif command == "down":
                depth += value
            elif command == "up":
                depth -= value
        print(horizontal*depth)

def aim_position(file):
    with open(file, 'r', encoding="utf-8") as f:
        horizontal = 0
        depth = 0
        aim = 0
        for line in f:
            token = [x.strip() for x in line.split()]
            command = token[0]
            value = int(token[1])
            if command == "forward":
                horizontal += value
                depth+= (aim*value)
            elif command == "down":
                aim += value
            elif command == "up":
                aim -= value
        print(horizontal*depth)
