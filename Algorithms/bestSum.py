#ecurssion
def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        if (remainderCombination != None):
            combination = remainderCombination + [num]
            if (shortestCombination == None or len(combination) < len(shortestCombination)):
                shortestCombination = combination
    return  shortestCombination    


#Table:
def bestSum(target, nums):
    resArr = [None]* (target+1)
    resArr[0] = []
    for i in range(target+1):
        if resArr[i] != None:
            for num in nums:
                if i+num <= target:
                    newcomb = resArr[i] + [num]
                    if resArr[i+num] == None or len(newcomb) < len(resArr[i+num]):
                        resArr[i+num] = resArr[i] + [num]
    return resArr[target]


print(bestSum(8, [2,3,5]))