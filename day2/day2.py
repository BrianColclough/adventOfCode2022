letterPointsDict = {'X': 1,'Y': 2,'Z': 3,'A': 1, 'B': 2, 'C':3}
winningPlayDict = {'A':'Y', 'B':'Z','C':'X'}
tieingPlayDict = {'A':'X', 'B':'Y','C':'Z'}
losingPlayDict = {'A':'Z', 'B':'X','C':'Y'}

def main():
    f = open('day2data.txt', 'r')
    lines = f.readlines()

    print("Part 1 total Score", getScorePart1(lines))
    
    print("Part 2 total Score", getScorePart2(lines))
    
    f.close()


def getScorePart1(lines):
    totalScore = 0
    
    for line in lines:
        letters = []
        for letter in line:
            if letter == ' ' or letter == '\n': continue
            
            letters.append(letter)
        
        myMovePoints = letterPointsDict[letters[1]]
        
        if letters == ['A','X']:
            totalScore = totalScore + myMovePoints + 3
        elif letters == ['A', 'Y']:
            totalScore += myMovePoints + 6
        elif letters == ['A', 'Z']:
            totalScore += myMovePoints + 0
        elif letters == ['B', 'X']:
            totalScore += myMovePoints + 0
        elif letters == ['B', 'Y']:
            totalScore += myMovePoints + 3
        elif letters == ['B', 'Z']:
            totalScore += myMovePoints + 6
        elif letters == ['C', 'X']:
            totalScore += myMovePoints + 6
        elif letters == ['C', 'Y']:
            totalScore += myMovePoints + 0 
        elif letters == ['C', 'Z']:
            totalScore += myMovePoints + 3
                
    return totalScore

def getScorePart2(lines):
    totalScore = 0
    
    for line in lines:
        letters = []
        for letter in line:
            if letter == ' ' or letter == '\n': continue
            
            letters.append(letter)
            
        if letters[1] == 'X':
            totalScore += letterPointsDict[losingPlayDict[letters[0]]] + 0
        elif letters[1] == 'Y':
            totalScore += letterPointsDict[tieingPlayDict[letters[0]]] + 3
        elif letters[1] == 'Z':
            totalScore += letterPointsDict[winningPlayDict[letters[0]]] + 6

    return totalScore
           
if __name__ == "__main__":
    main()    


