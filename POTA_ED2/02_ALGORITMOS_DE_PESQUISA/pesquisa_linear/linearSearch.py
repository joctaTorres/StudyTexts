def linearSearch(searchedValue, searchList):
    for index, element in enumerate(searchList):
        if element == searchedValue:
            return index
    
    return None


def recursiveLinearSearch(searchedValue, searchList, start=0):
    if searchList[start] == searchedValue:
        return start

    if start == len(searchList)-1:
        return None

    return recursiveLinearSearch(searchedValue, searchList, start=start+1)


searchList = [8, 84, 6, 42, 3, 65, 121, 8, 6, 12, 14, 87894, 423, 42, 1, 568]
searchValue = 42
position = recursiveLinearSearch(searchValue, searchList)
print('The search value', searchValue, 'is located at:', position)
