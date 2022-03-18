def sweep(file):
    with open(file, 'r', encoding = "utf-8-sig") as f:
        prev_line = 0
        count = 0
        for line in f:
            if int((line)) > prev_line:
                count+=1  
            prev_line=int(line)
    return count      
           
def sliding_sweep(file):
     with open(file, 'r', encoding = "utf-8-sig") as f:
         prev_chunk = 0
         count = -1
         list = []
         #l = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
         l = f.readlines()
         for i in range(len(l)):
            list.append(int(l[i]))
            while len(list) == 3:
                value = sum(list)
                print(f"value: {value}")
                if value > prev_chunk:
                    count += 1
                prev_chunk = value
                print(f"count: {count}")
                del(list[0])   
                #return count 
            
            
sliding_sweep("/Users/mederickschool/Desktop/CodingProjects/AOC/day1.txt")