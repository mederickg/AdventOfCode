from copy import copy, deepcopy

def gamma_epsilon(file):
    gamma = []
    epsilon = []
    array2d = []
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            temp = list(line.replace("\n", ""))
            array2d.append(temp)
    for i in range(len(array2d[1])):
        column = [row[i] for row in array2d]
        count1 = 0
        count0 = 0
        for k in column:
            if k == '1':
                count1+=1
            elif k == '0':
                count0+=1
        if count0>count1:
            gamma.append("0")
            epsilon.append("1")
        elif count1>count0:
            gamma.append("1")
            epsilon.append("0")
            

    temp_gamma = "".join(gamma)
    gamma_rate = int((temp_gamma), 2)
    
    temp_epsilon = "".join(epsilon)
    epsilon_rate = int((temp_epsilon), 2)
    
    energy_consumption = gamma_rate*epsilon_rate
    print(f"Energy Consumption: {energy_consumption}")


def life_support(file):
    array2d = []
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            temp = list(line.replace("\n", ""))
            array2d.append(temp)
        array2d2 = deepcopy(array2d)
    for i in range(len(array2d[1])):
        temp_array2d=[]
        column = [row[i] for row in array2d]
        count1 = 0
        count0 = 0
        for k in column:
            if k == '1':
                count1+=1
            elif k == '0':
                count0+=1
        if count0>count1:
            max = "0"
        else:
            max = "1"
        
 
        for k in array2d:
            #print(k[i])
            if k[i] == max:
                temp_array2d.append(k)
        array2d = temp_array2d
        
    resultO = "".join(array2d[0])
    
    array2d = array2d2
       
    for i in range(len(array2d[1])):
        temp_array2d=[]
        column = [row[i] for row in array2d]
        count1 = 0
        count0 = 0
        for k in column:
            if k == '1':
                count1+=1
            elif k == '0':
                count0+=1
        if count0>count1:
            max = "0"
        else:
            max = "1"
        
 
        for k in array2d:
            #print(k[i])
            if k[i] != max:
                temp_array2d.append(k)

        array2d = temp_array2d
        if len(array2d)==1:
            break
        
    print(f"Oxygen: {int((resultO), 2)}")
    
    
    resultC = "".join(array2d[0])
    print(f"CO2: {int((resultC), 2)}")
    
    life_support_rate = int(resultO, 2)*int(resultC, 2)
    
    print(f"Life Support Rating: {life_support_rate}")
    
life_support("/Users/mederickschool/Desktop/CodingProjects/AOC/day3.txt")