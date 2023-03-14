#Recursion
def allConstruct(target, wordBank, cache= {}):
    if target in cache:
        return cache[target]
    if target == '':
        return [[]]
    result = []
    for word in wordBank:
        if target.find(word) == 0:
            newTarget = target.removeprefix(word)
            newTargetcomponent = allConstruct(newTarget, wordBank)
            targetWays = [[word] + component for component in newTargetcomponent]
            result+= targetWays
    
    cache[target] = targetWays

    return result


#Table
def allConstruct(target, wordBank):
    resArr = [[] for i in range(len(target)+1)]
    resArr[0] = [[]]
    for i in range(len(target)+1):
        for word in wordBank:
            wordlength = len(word)
            if target[i: i + wordlength] == word:
                currCombination = resArr[i]
                for elem in currCombination:
                    temp = elem + [word]
                    resArr[i + wordlength].append(temp)
    return resArr[len(target)]


# allConstruct('enterapotentpot', ['a','p', 'ent', 'enter', 'ot','o','t'])
# allConstruct('purple', ['purp','p', 'ur', 'le', 'purpl'])
allConstruct('abcdef', ['ab','abc', 'cd', 'def', 'abcd', 'ef', 'c'])