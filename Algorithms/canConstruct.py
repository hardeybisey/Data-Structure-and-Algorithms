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

canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['eee', 'eeeeeeeee', 'ee', 'eeeeee', 'eeeeeeeee'])