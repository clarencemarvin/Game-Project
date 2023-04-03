s = int(input('Size--> '))
list1 = []

def createboard(s):
    if 2<s<11:  
        for i in range(0, s*(s-1)+1, s):    
            list1.append([str(i).rjust(2) for i in range(i, i+s, 1)])
            
def printboard(s):
    global list1
    for i in list1:
        print (*i)

def check():
    countx = 0
    counto = 0
    for i in list1: # this is for the row
        for ii in range(len(i)):
            if i[ii] == ' X':
                countx += 1
        if countx == s:
            print('Winner: X')
            exit()
        countx = 0

    for i in range(s): # columns
        for ii in range(s):
            if list1[ii][i] == ' X':
                countx += 1
        if countx == s:
            print('Winner: X')
            exit()
        countx = 0

    for i in range(0, s):
        if list1[i][i] == ' X':
            countx += 1
    if countx == s:
        print('Winner: X')
        exit()
    countx = 0

    for i in range(s-1, -1, -1):
        if list1[s-1-i][i] == ' X':
            countx += 1       
    if countx == s:
        print('Winner: X')
        exit()
    countx = 0

    for i in list1: # this is for the row
        for ii in range(len(i)):
            if i[ii] == ' O':
                counto += 1
        if counto == s:
            print('Winner: O')
            exit()
        counto = 0

    for i in range(s): # columns
        for ii in range(s):
            if list1[ii][i] == ' O':
                counto += 1
        if counto == s:
            print('Winner: O')
            exit()
        counto = 0
    
    for i in range(0, s):
        if list1[i][i] == ' O':
            counto += 1
    if counto == s:
        print('Winner: O')
        exit()
    counto = 0

    for i in range(s-1, -1, -1):
        if list1[s-1-i][i] == ' O':
            counto += 1
    if counto == s:
        print('Winner: O')
        exit()
    counto = 0
                                                                                                                
createboard(s); printboard(s)
turn = 0
steps = 0
while True:
    steps += 1
    if turn == 0:
        player = int(input('X--> '))
        turn += 1
        list1[int(player)//s][int(player)%s] = ' X'
        printboard(s); check()
    else:
        player = int(input('O--> '))
        turn -= 1
        list1[int(player)//s][int(player)%s] = ' O'
        printboard(s); check()

    if steps == (s**2):
        print('Winner: None')
        exit()
