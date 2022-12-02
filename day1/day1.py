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

    result = []
    val = max(allVals)
    allVals.remove(val)
    result.append(val)
    val = max(allVals)
    allVals.remove(val)
    result.append(val)
    val = max(allVals)
    allVals.remove(val)
    result.append(val)
    return sum(result)
    

if __name__ == "__main__":
    main()    

