class Solution:
    def isValid(self, s: str) -> bool:
        # iterate through the array
        # if it matches opening parentheses, then append to array 
        # else if closing parentheses 
        # # if last element of holding array matches
        # # # pop from holding array, go next
        # # else 
        # # # return false
        # if holding array is empty return true, else return false

        # '[]'
        holdingArray = []
        parensDictionary = { '(':')', '{':'}' , '[':']' }
        for char in s:
            if parensDictionary.get(char):
                holdingArray.append(char)
            else:
                if len(holdingArray) > 0 and parensDictionary[holdingArray[-1]] == char:
                    holdingArray.pop()
                else:
                    return False
        return len(holdingArray) == 0