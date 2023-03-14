#Recurssion
def canSum(targetSum, numbers, cache={}):
    if targetSum in cache:
        return cache[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers) == True:
            cache[targetSum] = True
            return True
    cache[targetSum] = False
    return  False    


#Table
def canSum(target, nums):
    resArr = [False]* (target+1)
    resArr[0] = True
    for i in range(target+1):
        if resArr[i] == True:
            for num in nums:
                if i+num <= target:
                    resArr[i+num]= True
    return resArr[target]


print(canSum(7, [3,5,7,4]))