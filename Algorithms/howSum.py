# Recurssion
def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        remainder = targetSum - num
        combination = howSum(remainder, numbers)
        if combination != None:
            return combination + [num]
    return  None    

#Table: Any combination
def howSum(target, nums):
    resArr = [None]* (target+1)
    resArr[0] = []
    for i in range(target+1):
        if resArr[i] != None:
            for num in nums:
                if i+num <= target:
                    resArr[i+num] = resArr[i] + [num]
    return resArr[target]


#Table: all possible combination
def howSum(target, nums):
    resArr = [None]* (target+1)
    resArr[0] = []
    for i in range(target+1):
        if resArr[i] != None:
            for num in nums:
                if i+num <= target and resArr[i+num] != None :
                    resArr[i+num] += [resArr[i] + [num]]
                elif i+num <= target:
                    resArr[i+num] = resArr[i] + [num]
    return resArr[target]



print(howSum(7, [3,7,5,4]))


