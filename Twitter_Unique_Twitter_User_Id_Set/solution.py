def getUniqueUserIDSum(arr:list):
    cache = set()
    for item in arr:
        if item not in cache:
            cache.add(item)
        else:
            while item in cache:
                item+=1
            cache.add(item)
    return sum(cache)


if __name__ == '__main__':
    print(getUniqueUserIDSum([3,2,1,2,7]))