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
<<<<<<< HEAD
=======

>>>>>>> db6a7e8c68c27f30be130f703f606d9c857adfb8
            
            
sliding_sweep("/Users/mederickschool/Desktop/CodingProjects/AOC/day1.txt")
