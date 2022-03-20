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
<<<<<<< HEAD
                del(list[0])
=======
                del(list[0])   

>>>>>>> be473252efaefdb34abb960c61c6d6b5db8fa1b6
