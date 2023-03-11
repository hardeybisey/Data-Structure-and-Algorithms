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

countConstruct('enterapotentpot', ['a','p', 'ent', 'enter', 'ot','o','t'])