num=int(input('Entre com um número inteiro: '))
for i in range(num):
    for j in range(num-i-1):
        print(" ",end='')
    for j in range(i+1):
        print('* ',end='')
    for j in range(2*(num-i-1)):
        print(" ",end='')
    for j in range(i+1):
        print('* ',end='')
    print()
for i in range(2*num,0,-1):
    for j in range(2*num-i):
        print(" ",end='')
    for j in range(i):
        print('* ',end='')
    print()

input()