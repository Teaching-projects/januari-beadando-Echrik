#Balogh Erik beadandó: Tulajdonképpen ez egy ilyen menüféleség, amiben különféle dolgokat lehet csinálni.

#Kockadobas
def dobas():
    import random
    osszeg = 0
    hatos = 0
    nums = []
    db = int(input("Adja meg, hogy mennyit szeretne dobni: "))
    for i in range(db):
        num = random.randint(1,6)
        nums.append(num)
    print("Ezeket  dobtad: ",nums)
    for i in nums:
        osszeg += i 
        if i == 6 in nums:
            hatos += 1
    print("A dobasaidbol",hatos, "lett hatos.") 
    print("A dobasok osszege: ",osszeg)
    print("A dobasok atlaga: ",osszeg/db)
    kilepes()
#Teglalap terulet, kerulet szamitas
def teglalapkt():
    a = int(input("Add meg a teglalap egyik oldalat(cm-ben add meg): "))
    b = int(input("Add meg a teglalap masik oldalat(cm-ben add meg): "))
    print("A teglalap kerulete: ", 2*(a + b))
    print("A teglalap terulete: ", a * b)
    kilepes()
#Italautomata
def ital():
    print("Milyen italt szeretne vasarolni?")
    print("1. Tea")
    print("2. Fanta")
    print("3. Energiaital")
    print("4. Kóla")
    itoka = int(input("Az ital szama: "))

    if itoka == 1:
        print("1. NesTea-200Ft")
        print("2. Lipton-150Ft")
        print("3. XIXO-250Ft")
        a = int(input("Valasszon egy italt: "))
        if a == 1:
            print("200Ft lesz!")
        elif a == 2:
            print("150Ft lesz!")
        elif a ==3:
            print("250Ft lesz!")
        else:
            print("Nincs ilyen lehetoseg!")
    elif itoka == 2:
        print("1. Narancs-120Ft")
        print("2. Grape Zero-200Ft")
        print("3. Wild Cherry-210Ft")
        print("4. Lemon-150Ft")
        a = int(input("Valasszon egy italt: "))
        if a == 1:
            print("120Ft lesz!")
        elif a == 2:
            print("200Ft lesz!")
        elif a ==3:
            print("210Ft lesz!")
        elif a ==4:
            print("150Ft lesz!")
        else:
            print("Nincs ilyen lehetoseg!")
    elif itoka == 3:
        print("1. Monster-350Ft")
        print("2. Adrenalin-175Ft")
        print("3. Hell-200Ft")
        print("4. Redbull-300Ft")
        a = int(input("Valasszon egy italt: "))
        if a == 1:
            print("350t lesz!")
        elif a == 2:
            print("175Ft lesz!")
        elif a ==3:
            print("200Ft lesz!")
        elif a ==4:
            print("300Ft lesz!")
        else:
            print("Nincs ilyen lehetoseg!")  
    elif itoka == 4:
        print("1. Pepsi Zero-150Ft")
        print("2. Pepsi-120Ft")
        print("3. Coca Cola Zero-150Ft")
        print("4. Coca Cola-120Ft")
        a = int(input("Valasszon egy italt: "))
        if a == 1:
            print("150t lesz!")
        elif a == 2:
            print("120Ft lesz!")
        elif a ==3:
            print("150Ft lesz!")
        elif a ==4:
            print("120Ft lesz!")
        else:
            print("Nincs ilyen lehetoseg!")   
    else:
        print("Nincs ilyen lehetoseg!")    
    kilepes()
#Kilepes a programbol
def kilepes():
    question = input("Ha ki szeretne lepni, akkor irjon egy igen-t, ha nem, akkor egy nem-et:")
    if  question == "igen" or question == "Igen":
        quit()
    elif question == "nem" or question == "Nem":
        return(maincucc())      
#Robot MI
def robotocska():
    import time

    name = str(input("Mi a neved?: "))
    year = int(input("Hány éves vagy?: "))
    loc = str(input("Hol laksz?: "))
    color = str(input("Mi a kedvenc színed?: "))
    act = str(input("Ki a kedvenc filmszínészed?: "))
    print("Örülök, hogy megismerhetlek", name, "!" "Ohhh, szóval", year, "éves vagy? Akkor te", 2021-year,"körül születtél.", loc, "elég szép hely az én véleményem szerint." "A kedvenc színed a",color,"?" "Ne máááár, nekem is!", act, "a legkedveltebb színészed? Nekem is nagyon tetszenek a filmjei.")

    time.sleep(3.0)

    choose = int(input("Amúgy van kedved kicsit számolni? Ha igen, akkor csak írj be egy 1-est, ha nem akkor 2-est: "))


    if choose == 1:
        print("Pötyögj be kettő számot és én pár alap számítást elvégzek rajta!")
        time.sleep(1.0)
        szam1 = int(input("Adj egy számot: "))
        szam2 = int(input("Adj még egy számot: "))

        osszeg = szam1+szam2
        osszeg2 = szam1-szam2
        osszeg3 = szam1*szam2
        osszeg4 = szam1/szam2
        print("A számjegyek összege: ",osszeg)
        print("A számjegyek különbsége: ",osszeg2)
        print("A számjegyek szorzata: ",osszeg3)
        print("A számjegyek hányadosa: ",osszeg4)
        print("Örülök, hogy egy kis időt szakítottál rám", name, "!" "További szép napot/estét kívánok neked!")
    else:
        print("Örülök, hogy egy kis időt szakítottál rám", name, "!" "További szép napot/estét kívánok neked!")
    kilepes()
#Main program
def maincucc():
    print("|Dobokocka|")
    print("|Italautomata|")
    print("|Robot|")
    print("|TeglalapKT|")
    print("|QUIT|")
    choose = input("Valasszon egy menupontot: ")

    if choose == "Dobokocka" or choose == "dobokocka":
        dobas()
    elif choose == "Italautomata" or choose == "italautomata":
        ital()
    elif choose == "Robot" or choose == "robot":
        robotocska()
    elif choose == "TeglalapKT" or choose == "teglalapKT" or choose == "teglalapkT" or choose == "teglalapkt" or choose == "TeglalapkT" or choose == "Teglalapkt":
        teglalapkt()  
    elif choose == "QUIT" or choose == "quit":
        quit()
maincucc()