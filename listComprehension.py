#list comprehension
fruit = ["apple", "banana", "kiwi", "mango"]
newfruit = [x if x!="banana" else "orange" for x in fruit]
print(newfruit)

'''Output: ['apple', 'orange', 'kiwi', 'mango']'''

fruit = ["apple", "banana", "kiwi", "mango"]
newfruit = [x if x=="banana" else "orange" for x in fruit]
print(newfruit)

'''Output: ['orange', 'banana', 'orange', 'orange']
