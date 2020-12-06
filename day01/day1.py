
filename = "input"

try:
    file = open(filename)
    lines = file.readlines()
    res = []
    for line in lines:
        res.append(int(line.replace("\n", "")))

    #  print(res)
    i = 0
    while ( i < (len(res)-1)):
        j = i + 1
        i+=1 
        while (j < len(res)):
            if (res[i] + res[j] == 2020):
                print(res[i] * res[j])
            j+=1
    
    
finally:
    file.close()
