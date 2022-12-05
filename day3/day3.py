alphabet = {chr(ord('a') + i): i + 1 for i in range(26)}
alphabet.update({chr(ord('A') + i): i + 27 for i in range(26)})
    
def main():
    f = open('day3data.txt', 'r')
    lines = f.readlines()
    
    print("Part 1 Value:", getRuckValue(lines))
    
    print("Part 2 Value:", partTwo(lines))
    
    f.close()
    
def getRuckValue(lines):

    total = 0
    
    for line in lines:
        firstHalf, secondHalf = line[:len(line)//2], line[len(line)//2:]   
        
        firstHalfLetters = count_letters(firstHalf)
        secondHalfLetters = count_letters(secondHalf)

        commonLetter = common_keys(firstHalfLetters, secondHalfLetters)
        
        total += alphabet[commonLetter[0]]
        
            

    return total

def partTwo(lines):
    total = 0
    currLine = 1
    for i, line in enumerate(lines):
        if line == ' ' or line == '\n': continue
        i = i+1
        if currLine == 3:
            lineThree = count_letters(line)
            commonLetter = common_keys_triple(lineOne, lineTwo, lineThree)
            total += alphabet[commonLetter[0]]
            print(commonLetter)
            currLine = 1
        elif currLine == 2:
            lineTwo = count_letters(line)
            currLine += 1
        elif currLine == 1:
            lineOne = count_letters(line)
            currLine += 1

    return total

def count_letters(s):
    # Create a dictionary to hold the count of each letter
    letter_counts = {}
    
    # Iterate over each letter in the string
    for c in s:
        if c == ' ' or c == '\n': continue
        # If the letter is not in the dictionary yet, add it and set its count to 1
        if c not in letter_counts:
            letter_counts[c] = 1
        # If the letter is already in the dictionary, increment its count by 1
        else:
            letter_counts[c] += 1
            
    # Return the dictionary with the counts of each letter
    return letter_counts

def common_keys(dict1, dict2):
  # Create a set of the keys from the first dictionary
  keys1 = set(dict1.keys())
  
  # Create a set of the keys from the second dictionary
  keys2 = set(dict2.keys())
  
  # Use the intersection method to find the common keys
  common_keys = keys1.intersection(keys2)
  
  # Return the common keys as a list
  return list(common_keys)
  
def common_keys_triple(dict1, dict2, dict3):
  # Create a set of the keys from the first dictionary
  keys1 = set(dict1.keys())
  
  # Create a set of the keys from the second dictionary
  keys2 = set(dict2.keys())
  
  keys3 = set(dict3.keys())
  
  # Use the intersection method to find the common keys
  common_keys = keys1.intersection(keys2)
  common_keys = common_keys.intersection(keys3)
  
  # Return the common keys as a list
  return list(common_keys)



if __name__ == "__main__":
    main()
