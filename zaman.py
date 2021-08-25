x = int (input('pleas enter number one :'))
y = int (input('pleas enter number two :'))

x = x.split('')
y = y.split('')

x = {'h' : int(x[0]) , 'm' : int(x[1]) , 's' : int(x[2])}
y = {'h' : int(y[0]) , 'm' : int(y[1]) , 's' : int(y[2])}

def sum_time(x,y):
    result = {}
    result['h'] = x['h'] + y['h']
    result['m'] = x['m'] + y['m']
    result['s'] = x['s'] + y['s']
    return result

def sub_time(x,y):
    result = {}
    result['h'] = x['h'] - y['h']
    result['m'] = x['m'] - y['m']
    result['s'] = x['s'] - y['s']
    return result

def second_to_time():
    second = int(input("Please enter second: "))
    result = {}
    result['h'] = second / 3600
    result['m'] = (second % 3600) / 60
    result['s'] = (second % 3600) % 60
    return result

def time_to_second(t):
    second = t['h'] * 3600 + t['m'] *60 + t['s']
    print('Second: ' , second)

def show_time(x):
    print(x["h"], ":", x["m"], ":", x["s"])

x ={"h":3, "m":30, "s":45}
y ={"h":13, "m":46, "s":30}
j = print(sum_time(x, y))
print(j)

while True:
    print('1- sum of times ')
    print('2- submite of times ')
    print('3- second to time ')
    print('4- time to second ')
    print('5- exit ')
    choice = int(input('Please enter your choose: '))
    if choice == 1:
        res = sum_time(x , y)
        show_time(res)
    elif choice == 2:
        res = sub_time(x , y)
        show_time(res)
    elif choice == 3:
        res = second_to_time()
        show_time(res)
    elif choice == 4:
        time_to_second(x)
        time_to_second(y)
    elif choice == 5:
        exit()
    else:
        print('talash mojadad') 
