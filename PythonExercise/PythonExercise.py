def Task1():
    count_minutes_input = int(input())
    count_hours = count_minutes_input // 60
    count_minutes = count_minutes_input % 60
    print(count_hours)
    print(count_minutes)

def Task2():
    count_minutes_input = int(input())
    count_hours_night_input = int(input())
    count_minutes_night_input = int(input())

    count_hours = count_hours_night_input * 60 + count_minutes_night_input + count_minutes_input
    count_hours_output = count_hours // 60
    count_minutes = count_hours % 60

    print(count_hours_output)
    print(count_minutes)

def Task3():
    max_hour = int(input())
    min_hour = int(input())
    hour = int(input())

    if hour >= max_hour and hour <= min_hour:
        print("Это нормально")
    elif hour >= max_hour:
        print("Пересып")
    else: 
        print("Недосып")

def Task4():
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Високосный")
    else:
        print("Обычный")

def Task5():
    a = int(input())
    b = int(input())
    c = int(input())

    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))
    s = s ** 0.5
    print(s)

def Task6():
    figure = int(input())

    if (figure > -15 and figure <= 12) or (figure > 14 and figure < 17) or (figure >= 19):
        print("True")
    else:
        print("False")

def Task7():
    num1 = float(input())
    num2 = float(input())
    operation = str(input())
    if(num2 == 0 and (operation == "mod" or operation == "/" or operation == "div")):
        print("Деление на 0!")
    elif operation =='+':
        print(num1 + num2)
    elif operation == '-': 
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == 'pow':
        print(num1 ** num2)
    elif operation == '/':
        print(num1 / num2)
    elif operation == 'mod':
        print(num1 % num2)
    elif operation == 'div':
        print(num1 // num2)

def Task8():
    type = input()
    pi = 3.14
    if type == "круг":
        r = float(input())
        s = pi*r**2
    elif type == "треугольник":
        a = float(input())
        b = float(input())
        c = float(input())        
        p = (a+b+c)/2
        s = (p*(p-a)*(p-b)*(p-c))
        s = s ** 0.5
    elif type == "прямоугольник":
        a = float(input())
        b = float(input())
        s = a*b
    print(s)

def Task9():
    a = int(input()) 
    b = int(input()) 
    c = int(input()) 

    if a >=b and a >=c:
        print(a)
        if b >= c or b == a:
            print(c)
            print(b)
        else:
            print(b)
            print(c) 
    elif b>=a and b>=c: 
        print(b) 
        if a>=c or a == b: 
            print(c) 
            print(a) 
        else: 
            print(a) 
            print(c) 
    elif c >= a and c >= b: 
        print(c) 
        if b >=a or b ==c: 
            print(a) 
            print(b)
        else: 
            print(b) 
            print(a)

def Task10():
    count_progrs = int(input())
    if (count_progrs % 100 == 11) or (count_progrs % 100 == 13) or (count_progrs % 100 == 14) or (count_progrs % 100 == 12):
        print(count_progrs, "программистов")
    elif count_progrs % 10 == 1:
        print(count_progrs, "программист")
    elif (count_progrs % 10 == 2) or (count_progrs % 10 == 3) or (count_progrs % 10 == 4):
        print(count_progrs, "программиста")
    else:
        print(count_progrs, "программистов")

def Task11():
    number = str(input())
    all_arr = list(map(int, str(number)))
    first_arr = []
    last_arr = []
    for i in range(0,3,1):
        first_arr.append(all_arr[i])
    for i in range(3,6,1):
        last_arr.append(all_arr[i])
    sum_last = sum(last_arr)
    sum_first = sum(first_arr)
    if sum_first == sum_last:
        print("Счастливый")
    else:
        print("Обычный")  

def Task12():
    i = 0
    sum = 0
    a = 1
    while a != 0:
        a = int(input())
        sum = sum + a
    print(sum) 

def Task13():
    a = int(input())
    b = int(input())
    d = a

    while d % a or d % b:
        d += a
    print(d)

def Task14():
    i = int(input()) 
    while i<=100:
        if i<10:
            i = int(input())
            continue
        print(i)
        i = int(input())

def Task15():
    min_str = int(input())
    max_str = int(input())
    max_str = max_str + 1
    min_column = int(input())
    max_column = int(input())
    max_column = max_column + 1
    j = min_column
    if min_str <= max_str and min_column <= max_column:
        print(end = '\t')
        for j in range(min_column, max_column, 1):
                print(j, '\t', end = '')
        print(end = '\n')
   
        for i in range(min_str, max_str, 1):
            print(i, end = '')
            for j in range(min_column, max_column, 1):
                a = i*j
                print('\t',a, end = '')
            print(end = '\n')

def Task16():
    a, b = int(input()), int(input())
    count = summ = 0
    for i in range(a,b+1):
        if i%3 == 0:
            count = count +1
            summ = summ + i
    print(summ/count)

def Task17():
    string = input()
    string = string.lower()
    all_sum = len(string)
    g_sum = string.count('g')
    c_sum = string.count('c')
    gc_sum = g_sum + c_sum
    percent = gc_sum*100/all_sum
    print(percent)

def Task18():
    string = input()
    count = 1

    for i in range(len(string)):
        letter = string[i]
        if i+1 == len(string):
            break
        elif letter == string[i+1]:
            count = count + 1
        else:
            print(letter, end = '')
            print(count, end ='')
            count = 1
    print(letter, end = '')
    print(count, end ='')

def Task19():
    s = [ int(i) for i in input().split()]
    t = []
    s.sort()
    l = len(s)-1
    k = 100000
    if len(s)!=1:
        for i in range(0,l):
            if s[i]==s[i+1] and s[i]!=k:
                t.append(s[i])
                k=s[i]
        for j in range(l,l+1):
            if s[-1]==s[-2] and s[j]!=k:
                t.append(s[j])
    n = len(t)
    for g in range(0,n):
        print(t[g],end=' ')

def Task20():
    a=int(input())
    m=[]
    for i in range(a):
        j=0
        while j<i+1:
            m.append(i+1)
            j+=1
        if len(m)>a: break
    m=m[0:a]
    for i in m:
        print(i, end=" ")

def Task21():
    n = ''
    m = []
    while True:
        n = str(input()) # ввод строк
        if n == 'end':
            break
        m.append([int(s) for s in n.split()]) 
    li, lj = len(m), len(m[0])
    new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]

    for i in range (li):
        for j in range (lj):
            print(new[i][j], end =' ')
        print()


def Task22():
    def spiral(n):
        dx,dy = 1,0           
        x,y = 0,0              
        myarray = [[None]* n for j in range(n)]
        for i in range(1,n**2+1):
            myarray[x][y] = i
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and myarray[nx][ny] == None:
                x,y = nx,ny
            else:
                dx,dy = -dy,dx
                x,y = x+dx, y+dy
        return myarray
 
    def printspiral(myarray):
        n = range(len(myarray))
        for y in n:
            for x in n:
                print (myarray[x][y],end=' ')
            print()

    n = int(input())
    printspiral(spiral(n))

def Task23(x):
    if x<=-2:
        f=1-(x+2)**2
    elif x>-2 and x<=2:
        f=-(x/2)
    elif x>2:
        f=(x-2)**2+1
    return f

def Task24(l):
    le = len(l)-1
    i = le
    while i!=-1:
        if l[i]%2:
            del l[i]
        else:
            l[i]=l[i]//2
        i -=1
    return

def Task25(d, key, value):
    if (key in d):
        d[key] += [value];
    else:
        if(2*key in d):
            d[2*key] += [value];
        else:
            d[2*key] = [value];

def Task26():
    words = input().lower().split(" ");
    count = 1;
    countWords = {}
    for word in words:
        count = words.count(word);
        countWords[word] = count;
    for key, value in countWords.items():
        print(key, value);

def Task27():
    alphavite = input();
    key = input();
    inputString = input();
    inputString2 = input();
    encoder = {};

    def get_key(value):
        for k, v in encoder.items():
            if v == value:
                return k
        
    alph = list(alphavite);
    k = list(key)
    str = list(inputString);

    for i in range(len(alphavite)):
        encoder[alphavite[i]] = key[i]

    result=""
    for item in str:
        result += encoder[item]
    print(result)

    decrypt=""
    for item in inputString2:
        decrypt += get_key(item)
    print(decrypt)

def Task28():
    dictionary = {}

    for i in range(int(input())):
        dictionary[input().lower()] = i;

    error = {}
    for i in range(int(input())):
        item = input().lower().split(" ");
        for word in item:
            if(word not in dictionary):
                error[word] = word;
            
    for item in list(set(error)):
        print(item)

def Task29():
    coordinats = {'север': 0, 'юг': 0, 'запад': 0, 'восток': 0}

    for i in range(int(input().lower())):
        key, value = input().split()
        coordinats[key] += int(value)

    print(coordinats['восток'] - coordinats['запад'], coordinats['север'] - coordinats['юг'])