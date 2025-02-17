def singleTonclass(arg):
    L = []
    def Inner():
        if len(L) == 0:
            obj = arg()
            L.append(obj)
        return L[0]
    return Inner

@singleTonclass
class Movie1:
    def __init__(self):
        self.maxtic = 100

    def Booking(self):
        print(f'Available Tickets are {self.maxtic}')
        reqtic = int(input('Enter the number of ticket: '))
        if reqtic <= self.maxtic:
            print('Tickets booked successfully----')
            self.maxtic -= reqtic
        else:
            print('Tickets not available')

@singleTonclass
class Movie2:
    def __init__(self):
        self.maxtic = 200

    def Booking(self):
        print(f'Available Tickets are {self.maxtic}')
        reqtic = int(input('Enter the number of ticket: '))
        if reqtic <= self.maxtic:
            print('Tickets booked successfully----')
            self.maxtic -= reqtic
        else:
            print('Tickets not available')

@singleTonclass
class Movie3:
    def __init__(self):
        self.maxtic = 420

    def Booking(self):
        print(f'Available Tickets are {self.maxtic}')
        reqtic = int(input('Enter the number of ticket: '))
        if reqtic <= self.maxtic:
            print('Tickets booked successfully----')
            self.maxtic -= reqtic
        else:
            print('Tickets not available')

def BMYS():
    print('1. Movie1\n2. Movie2\n3. Movie3')
    option = int(input('Choose the movie option: '))
    if option == 1:
        user = Movie1()
        user.Booking()
    elif option == 2:
        user = Movie2()
        user.Booking()
    elif option == 3:
        user = Movie3()
        user.Booking()
    else:
        print('No Movie Available')

def PayTm():
    print('1. Movie1\n2. Movie2\n3. Movie3')
    option = int(input('Choose the movie option: '))
    if option == 1:
        user = Movie1()
        user.Booking()
    elif option == 2:
        user = Movie2()
        user.Booking()
    elif option == 3:
        user = Movie3()
        user.Booking()
    else:
        print('No Movie Available')

BMYS()
print('-----------')
PayTm()
print('-----------')
PayTm()
print('------------')
BMYS()
print('-------------')
PayTm()