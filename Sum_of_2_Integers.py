#Dylan Joel Lim Wei Han, 185540R, IT2153-04
#ascending order sorted list
SEQ = [2,3,5,7,8,10,15,16,23,28]
#z parameter is the target value
def challenge(z):
    end = len(SEQ)
    for i in range(len(SEQ)-1,0,-1): #loop through the entire sequence to find a value that is lower than z to start at
        if SEQ[i] < z:
            end = i
            break
    
    for y in range(end,0,-1): #loop through from the end
        tmp = z - SEQ[y] #finding the remainder when z minus the last aquired value
        for x in range(0,y-1,1): #loop from the front to the value before the last aquired value
            if tmp == SEQ[x]: #check if the looped value is equals to the remainder
                print("X = " + str(SEQ[x]) + "\nY = " + str(SEQ[y]) + "\nTRUE") #return x,y,bool
                return
    print("X = not found" + "\nY = not found" + "\nFALSE")#If values not found

challenge(16)