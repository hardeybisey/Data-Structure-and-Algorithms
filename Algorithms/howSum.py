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

print(howSum(7, [3,7,5,4]))