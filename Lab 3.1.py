num = int(input("Enter num ="))

for i in range(0,num+1):
    for j in range(0,i):
        print('*', end ='')
    print () 

print('-------------------------------')

for i in range(num,0,-1):
    for j in range(i):
        print('*', end ='')
    print () 

print('-------------------------------')

for i in range(num):
    for j in range(num - i - 1):
        print(' ', end='')
    for k in range(i + 1):
        if k < i:
            print('* ', end='')
        else:
            print('*', end='')
    print()


print('-------------------------------')

for i in range(num):
    for j in range(i):
        print(' ', end='')
    for k in range(num - i):
        if k < num - i - 1:
            print('* ', end='')
        else:
            print('*', end='')
    print()

print('-------------------------------')

for i in range(1, num + 1):
    for j in range(num - i):
        print(' ', end='') 
    for k in range(i):
        print('*', end='')
    print()

print('-------------------------------')
