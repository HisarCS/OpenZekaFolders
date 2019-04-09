

list1 = [[1, 2, 3, 3],[2, 3],[3, 4],[4],[5],[6],[7, 5],[8],[9],[0]]





# occuredCounter = list()
# for l1 in list1:
#     for l2 in l1:
#         # print(l1, l2)
#         if l2 in l1:
#             if l2 in occuredCounter:
#                 print("the number exist more than once", l2)
#                 # occuredCounter.pop()
#             else:
#                 occuredCounter.append(l2)
#
# print(occuredCounter)


def sortTheArray(array):
    theNumberList = list()
    for l1 in array:
        theNumberList.append(len(l1))
    print(theNumberList, sorted(theNumberList, reverse=True))


sortTheArray(list1)