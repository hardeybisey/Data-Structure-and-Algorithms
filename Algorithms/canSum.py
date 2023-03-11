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

print(canSum(7, [3,5,7,4]))