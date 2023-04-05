def generatorfun():
    i=0
    while 1:
        yield i
        i = i+2
        if i>=10:
            break
for x in generatorfun():
    print(x, end='\t')