#Recurssion
def countConstruct(target, wordBank, cache= {}):
    if target in cache:
        return cache[target]
    if len(target) == 0:
        return 1
    totalcount = 0
    for word in wordBank:
        if target.find(word) == 0:
            newTarget = target.removeprefix(word)
            counter = countConstruct(newTarget, wordBank)
            cache[newTarget] = counter
            totalcount += counter
        
    return totalcount

#Table

def countConstruct(target, wordBank):
    resArr = [0] * (len(target)+1)
    resArr[0] = 1
    for i in range(len(target)+1):
        for word in wordBank:
            wordlength = len(word)
            if target[i: i + wordlength] == word:
                resArr[i + wordlength] += resArr[i]

    return resArr[len(target)]

countConstruct('enterapotentpot', ['a','p', 'ent', 'enter', 'ot','o','t'])