from random import *

game=input("Kas tahad mängida kellegagi-(2) või robotiga-(1) ")
gameElem=["Kivi","Paber","Käärid"]
võidudI=[]
võidudR=[]
IV=IK=II=RV=RK=RI=0
while game not in ["1","2"]:
    game=input("Palun kirjuta 1 või 2 ")
if game=="1":
    mäng=input("Mitu korda sa tahad mängida? Mitte rohkem kui 5 korda ")
    while mäng.isdigit()==False or int(mäng)>5 or int(mäng)==0:
        mäng=input("Kirjuta õige arv! ")
    for i in range(int(mäng)):
        shuffle(gameElem)
        robot=gameElem[randint(0,2)]
        inimene=input(f"Palun vali {gameElem} ").title()
        while inimene not in gameElem:
            inimene=input(f"Palun vali {gameElem} ").title()
        if gameElem.index(inimene)>gameElem.index(robot):
            print("Sina võitsid!")
            võidudI.append(f"{i+1} robotimäng - võit")
            IV+=1
            võidudR.append(f"{i+1} robotimäng - kaotus")
            RK+=1
        elif gameElem.index(inimene)<gameElem.index(robot):
            print("Sina kaotasid!")
            võidudR.append(f"{i+1} robotimäng - võit")
            RV+=1
            võidudI.append(f"{i+1} robotimäng - kaotus")
            IK+=1
        else:
            print("Sul on viik!")
            võidudI.append(f"{i+1} robotimäng - viik")
            II+=1
            võidudR.append(f"{i+1} robotimäng - viik")
            RI+=1
        print()
    print("Inimene:")
    print(võidudI)
    print(f"Mängude arv - {mäng}\nVõidud - {IV}\nKaotused - {IK}\nViik - {II}")
    print()
    print("Robot:")
    print(võidudR)
    print(f"Mängude arv - {mäng}\nVõidud - {RV}\nKaotused - {RK}\nViik - {RI}")
else:
    mäng=input("Mitu korda sa tahad mängida? Mitte rohkem kui 5 korda ")
    while mäng.isdigit()==False or int(mäng)>5 or int(mäng)==0:
        mäng=input("Kirjuta õige arv! ")
    for i in range(int(mäng)):
        shuffle(gameElem)
        EsInimene=input(f"1 inimene. Palun vali {gameElem} ").title()
        while EsInimene not in gameElem:
            EsInimene=input(f"1 inimene. Palun vali {gameElem} ").title()
        TeInimene=input(f"2 inimene. Palun vali {gameElem} ").title()
        while TeInimene not in gameElem:
            EsInimene=input(f"2 inimene. Palun vali {gameElem} ").title()
        if gameElem.index(EsInimene)>gameElem.index(TeInimene):
            print("Sina võitsid!")
            võidudI.append(f"{i+1} TeInimeneimäng - võit")
            IV+=1
            võidudR.append(f"{i+1} TeInimeneimäng - kaotus")
            RK+=1
        elif gameElem.index(EsInimene)<gameElem.index(TeInimene):
            print("Sina kaotasid!")
            võidudR.append(f"{i+1} TeInimeneimäng - võit")
            RV+=1
            võidudI.append(f"{i+1} TeInimeneimäng - kaotus")
            IK+=1
        else:
            print("Sul on viik!")
            võidudI.append(f"{i+1} TeInimeneimäng - viik")
            II+=1
            võidudR.append(f"{i+1} TeInimeneimäng - viik")
            RI+=1
        print()
    print("Esimene Inimene:")
    print(võidudI)
    print(f"Mängude arv - {mäng}\nVõidud - {IV}\nKaotused - {IK}\nViik - {II}")
    print()
    print("Teine Inimene:")
    print(võidudR)
    print(f"Mängude arv - {mäng}\nVõidud - {RV}\nKaotused - {RK}\nViik - {RI}")
    