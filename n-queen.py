n = int(input('n: '))
list1 = []
lista = [0] * (2*n)
listb = [0] * (2*n)

def createboard(n):
    if 3<n<11:  
        for i in range(0, n*(n-1)+1, n):    
            list1.append([str(i).rjust(2) for i in range(i, i+n, 1)])
def printboard(n):
    global list1
    for i in list1:
        print (*i)

def queens():
    queen = input('Queens: ').split(' ')
    for i in queen:
        list1[int(i)//n][int(i)%n] = ' Q'
        lista[int(i)//n-int(i)%n+n]+=1
        listb[int(i)//n+int(i)%n]+=1

def check():
    global lista
    global listb
    count = 0
    for i in list1: # this is for the row
        for ii in range(n):
            if i.count(' Q') > 1:
                print ('--> FAIL <--')
                exit()
            count = 0
    for i in range(n): # columns
        for ii in range(n):
            if list1[ii][i] == ' Q':
                count += 1
        if count > 1:
            print('--> FAIL <--')
            exit()
        count = 0
    for i in lista:
        if i>1:
            print('--> FAIL <--')
            exit()
    for i in listb:
        if i>1:
            print('--> FAIL <--')
            exit()   
    print('--> SUCCESS <--')

createboard(n)
printboard(n)
queens()
printboard(n)
check()
