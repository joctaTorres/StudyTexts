'''
WIP
'''

import math



def binarySearch(searchedValue, orderedList=[], start=0, end=0):
    
    # end = len(orderedList)
    center = math.floor(size/2)
    if orderedList[center] == searchedValue:
        return center
    
    if start == end:
        return None
    else:
        if orderedList[center] < searchedValue:
            return binarySearch(searchedValue, orderedList, center+1, end)
        else:
            return binarySearch(searchedValue, orderedList, start, center-1)


list = [1, 2, 3, 4, 5]
searchedValue = 2

index = binarySearch(list, searchedValue)

if index == None:
    print('The list does not contains', searchedValue, '.')
else:
    print('The value', searchedValue, 'is at index', index, 'of the array.')

