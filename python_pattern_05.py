rows=int(input("enter a row number:"))
for i in range(0,rows):
    for _ in range(rows-i):
        print(" ",end='')
    for _ in range(i):
        print('*',end='')
    for _ in range(rows-1):
        print('',end='')
    for _ in range(i+1):
        print('*',end='')
    print()
