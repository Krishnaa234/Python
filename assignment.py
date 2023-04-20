list1 = [1,2,3,4,3,6,1,9,1,11,11,11,12]
list2 = list1.copy()
for token in list1:
    app = list2.count(token)
    if app>1:
        for i in range (app):
            list2.remove(token)
print(list2)