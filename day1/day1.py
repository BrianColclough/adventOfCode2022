def main():
    f = open('day1data.txt', 'r')
    lines = f.readlines()
    
    print("most calories single:", getMostCalories(lines))
    
    print("most calories three:", getTopThreeMostCalories(lines))
    
    f.close()

def getMostCalories(lines):
    max = 0
    currentVal = 0
    
    for l in lines:
        if l == '\n':
            if currentVal > max:
                max = currentVal
            currentVal = 0
        else:
            currentVal = currentVal + int(l)

    return max

def getTopThreeMostCalories(lines):
    allVals = [] 
    currentVal = 0
    
    for l in lines:
        if l == '\n':
            allVals.append(currentVal)
            currentVal = 0
        else:
            currentVal = currentVal + int(l)

    allVals = sorted(allVals)

    topThree = allVals[-3::]

    return sum(topThree)

if __name__ == "__main__":
    main()    

