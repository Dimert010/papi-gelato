print('welkom bij Papi Gelato, u kunt hier maar 4 smaken kiezen')
sorry = "Sorry dat is geen optie die we aanbieden..."
liter = 0
aantalbollen = 0
aantal = 0
aantalbol = 0
ijssmaak = 0
hoorntje = 0
bakje = 0

def start():
    keuze = int(input('Bent u 1) particulier of 2) zakelijk? '))
    if keuze == 1:
        stap1()
    elif keuze == 2:
        zakelijk1()
    else:
        print('sorry')
        return start()

def zakelijk1():
    global liter 
    print('hoevel liter ijs wilt u?')
    liter = int(input('>'))
    if liter >1:
        zakelijk2()
    else:
        print('sorry')
        zakelijk1()

def zakelijk2():
    for k in range(liter):
        print('welke smaak wilt u voor de liter  nummer', k,'? A) Aarbei, C) Chocolade of V) Vanilla?')
        Smaak = input('>').upper()
    if Smaak  == 'A' or Smaak == 'C' or Smaak == 'V':
        zakelijkbon()
    else:
        print('sorry')
        zakelijk2()

def stap1():
    global aantalbollen 
    aantal = int(input('hoeveel bolletjes wilt u?: '))
    aantalbollen = aantal
    if aantal in range(1, 5):
        smaken(aantal)
        aantalbollen += 1
    elif aantal in range(5, 9):
        smaken(aantal)
        aantalbollen += 1
    elif aantal > 8:
        print('Sorry, zo grote bakken hebben we niet.')
        return stap1()
    else:
        print(sorry)
        return stap1()

def smaken(aantalbol):
    global ijssmaak
    p = 1 
    while p <= aantalbol:
        print('welke smaak wilt u voor uw ijs', p,'? A) Aarbei, C) Chocolade of V) Vanilla')
        ijssmaak = input('> ').upper()
        if ijssmaak == 'A' or ijssmaak == 'C' or ijssmaak == 'V':
            p += 1
        else:
            print('sorry, dat is geen optie die we aanbieden.')
    stap2(aantalbol)

def stap2(aantalbol):
    global houder
    global hoorntje
    global bakje
    print('wilt u deze', aantalbol, 'bolletje(s) in A) een hoorntje of een B) een bakje?' )
    houder = input('>').upper()
    if houder == 'A':
        houder = 'hoorntje'
        hoorntje += 1
        toppings(aantalbol)
    elif houder == 'B':
        houder = 'bakje'
        bakje += 1
        toppings(aantalbol)
    else:
        print(sorry)
        return stap2()

def toppings(aantalbol):
    global topping
    print("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?")
    topping = input('>').upper()
    if topping == 'A':
        topping = 'geen'
        stap3(aantalbol)
    elif topping == 'B':
        topping = 'slagroom'
        stap3(aantalbol)
    elif topping == 'C':
        topping = 'sprinkels'
        stap3(aantalbol)
    elif topping == 'D':
        topping = 'caramels'
        stap3(aantalbol)
    else:
        print('sorry, dat is geen optie die we aanbieden.')


def stap3(aantalbol):
    print('Hier is uw', houder,'met', aantalbol,'bolletje. Wilt u nog meer bestellen? Y/N')
    meer = input('> ')
    if meer == 'y':
        stap1()
    elif meer == 'n':
        bonnetje()
        print('bedankt en tot ziens')
    else:
        print('sorry, dat is geen optie die we aanbieden.')

def bonnetje():
    print('----------papi gellato-------------')
    print(f'bolletjes     {aantalbollen*0.95}')
    print(f'hoorntje      {hoorntje*1.25}')
    print(f'bakje         {bakje*0.75}')
    print("             -------- +")
    print(f'totaal        {aantalbollen + hoorntje + bakje}')


def zakelijkbon():
    prijs = liter * 9.80
    print('--------papi gelato----------')
    print(f'{liter}*9,80 = {prijs}')
    print(f'totaal = {prijs}')
    print(f'btw(6%) = {prijs/106*6}')


    
start() 


