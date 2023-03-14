#Recurssion
def canConstruct(target, wordBank, cache= {}):
    if target in cache:
        return cache[target]
    if len(target) == 0:
        return True
    for word in wordBank:
        if target.find(word) == 0:
            newTarget = target.removeprefix(word)
            newJob = canConstruct(newTarget, wordBank)
            if newJob:
                cache[target] = newJob
                return True
    cache[target] = False
    return False

#Table
def canConstruct(target, wordBank):
    targetLength = len(target)+1
    resArr = [False]* (targetLength)
    resArr[0] = True
    for i in range(targetLength):
        if resArr[i] == True:
            for word in wordBank:
                wordlength = len(word)
                if target[i: i + wordlength] == word:
                    if i + wordlength <= targetLength:
                        resArr[i + wordlength] = resArr[i]

    return resArr[targetLength-1]
canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['eee', 'eeeeeeeee', 'ee', 'eeeeee', 'eeeeeeeee'])