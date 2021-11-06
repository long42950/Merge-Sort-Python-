# Merge sort
def sort(theList):
    if len(theList) == 1:
        return theList
    a = theList[0]
    b = theList[1]
    if a > b:
        return [b,a]
    else:
        return [a,b]

# For class/objects
def get_indexlist(userList, *args):
    index = ""
    newList = []
    for arg in args:
        index = arg
    if index == "":
        newList = userList
    else:
        for item in userList:
            if isinstance(item, dict):
                newList.append(item[index])
            else:
                newList.append(getattr(userList,index))
    return newList

# Main code            
def merge_sort(userList, *args):
    list1 = []
    list2 = []
    rtnList = []
    mainList = get_indexlist(userList, *args)
    if len(mainList) == 2:
        return sort(mainList)
    #Divide
    if len(mainList) > 2:
        half = len(mainList)//2
        if half == 1:
            list1 = [mainList[0]]
        else:
            list1 = merge_sort(mainList[:half])
        list2 = merge_sort(mainList[half:])
    #Conqur
    totallen = len(list1) + len(list2)
    while len(rtnList) < totallen:
        found = False
        for x in list2:
            if x < list1[0]:
                rtnList.append(x)
                list2.remove(x)
                found = True
                
                break
        if not found:
            rtnList.append(list1[0])
            list1.pop(0)
        #If either list ran out of element, joint them
        if len(list1) < 1:
            rtnList = [*rtnList, *list2]
        elif len(list2) < 1:
            rtnList = [*rtnList, *list1]
    return rtnList

# For calling
def merge_sort_main(userList, index):
    indexList = merge_sort(userList, index)
    testList = userList
    rtnList = []
    for i in indexList:
        for item in testList:
            if not isinstance(item, dict):
                if i == getattr(item, index):
                    rtnList.append(item)
                    testList.remove(item)
                    break
            elif i == item[index]:
                rtnList.append(item)
                testList.remove(item)
                break
    return rtnList

daList = [18,9,11,4,6]

#print(merge_sort(daList))
        
