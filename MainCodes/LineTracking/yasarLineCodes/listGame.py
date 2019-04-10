

list1 = [[1, 2, 3, 3],[2, 3],[3, 4],[4],[5],[6],[7, 5],[8],[9, 2, 2, 2],[0]]




def sortTheArrayLen(array):
    theIndexList = list()
    for (i, l1) in enumerate(array):
        theIndexList.append([len(l1), i])
    theIndexList = sorted(theIndexList, reverse=True)

    theTopThree = list()
    for t in theIndexList[:3]:
        indexNumber = t[1]
        theTopThree.append(array[indexNumber])

    return theTopThree




topThree = sortTheArrayLen(list1)
print(topThree)

# print(list1.index([0]))

# print(min(len(list1)))