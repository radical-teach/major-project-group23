import numpy as np
import datetime
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import re

netid_passwords = [("jlb661", "Joe"), ("bn198", "Beaman"), ('at891', 'Avery'), ('ccd83', 'Christopher'), ('fak38','Faraz')]
RUIDs = ['194007666', '194295928', '194295834','183747269', '117302075']
RUID_pattern = re.compile("[0-9]{9}")
while True:
    signin_Option = input("Would you like to sign in via netid/password or RUID? Enter 1 for netid/Password OR 2 for RUID: ")
    if int(signin_Option) == 1:
        netid = input("Enter netid: ")
        password = input("Enter password: ")
        if (netid,password) in netid_passwords:
            break
        else:
            print("Invalid credentials")
    elif int(signin_Option) == 2:
        RUID = input("Enter RUID: ")
        if RUID_pattern.match(RUID) and RUID in RUIDs:
            break
        else:
            print("Invalid credentials")
    else:
        print("Invalid input, Please enter 1 or 2")




homepage = tk.Tk()
homepage.title("RU Riding Application")

homeText = tk.Label(homepage, text="RU Riding", font=("Times New Roman", 40, 'bold'))
homeText.pack(side=tk.TOP)

homepageWindow = Canvas(homepage, width=600, height=600)
homepageWindow.pack(fill="both", expand=True)



homepageWindow.create_text(300, 50, text="This Program Will Show You the Different Bus Routes", font=("Times New Roman", 20))
homepageWindow.create_text(300, 75, text="Of Rutgers New Brunswick", font=("Arial", 20))
homepageWindow.create_text(300, 100, text="Please Select the Button Below to View Buses", font=("Times New Roman", 20))





def busRoutes():

    homepageWindow.create_text(300, 400, text="Please Select A Bus Route on the Following Prompt.", font=("Arial", 20))
    homepageWindow.create_text(300, 450, text="Enter Pickup and Destination.", font=("Arial", 20))


    routesWindow = tk.Tk()

    routesWindow.title("Bus Routes")
    routePrompt = tk.Label(routesWindow, text="Choose a Route")
    routePrompt.grid(row=0, column=0, padx=10, pady=10)


    global routeEnter
    routeEnter = Button(routesWindow, text="Enter", command=busStopList)
    routeEnter.grid(row=5, column=1, padx=10, pady=10)

    global routesMenu
    routesMenu = ttk.Combobox(routesWindow, value=routesNames, width=20)
    routesMenu.grid(row=0, column=1, padx=8, pady=8)


    routesWindow.mainloop()








studentPortal = tk.Button(homepage, text="Run App", command=busRoutes, font=("Arial", 20, 'bold'))
portal = homepageWindow.create_window(150, 300, anchor="nw", window=studentPortal, height=60, width=280)




def busSwitch(busName):
    busesRU = {
        "REXL": 0,
        "REXB": 1,
        "LX": 2,
        "H": 3,
        "F": 4,
        "EE": 5,
        "A": 6,
        "B": 7,
        "BHE": 8,
        "C": 9
    }


    return busesRU.get(busName, "Invalid Argument")


def busStopList():
    if (routesMenu.get() == ""):
        showinfo("Error", "Please Select a Bus Route")

    else:
        stopsWindow = tk.Tk()

        stopsWindow.title("Bus Stops")
        startLabel = tk.Label(stopsWindow, text="Select First Stop")
        startLabel.grid(row=0, column=0, padx=8, pady=8)

        global opt
        i = busSwitch(routesMenu.get())
        opt = LOR[i]

        global selectedNames
        selectedNames = routesListList[i]

        global routeSelected
        routeSelected = routeList[i]

        global firstselected
        firstselected = StringVar()
        firstselected.set(opt[0])

        global firstStopMenu
        firstStopMenu = ttk.Combobox(stopsWindow, value=opt, width=50)
        firstStopMenu.grid(row=0, column=1, padx=8, pady=8)

        def change_dropdown1(*args):
            print(firstselected.get())

        firstselected.trace('w', change_dropdown1)

        destinationLabel = tk.Label(stopsWindow, text="Choose Second Stop")
        destinationLabel.grid(row=1, column=0, padx=8, pady=8)

        global secondselected
        secondselected = StringVar()
        secondselected.set(opt[0])

        global secStopMenu
        secStopMenu = ttk.Combobox(stopsWindow, value=opt, width=50)
        secStopMenu.grid(row=1, column=1, padx=8, pady=8)

        def change_dropdown(*args):
            print(secondselected.get())

        secondselected.trace('w', change_dropdown)

        global select
        select = Button(stopsWindow, text="Submit", command=enterPrompt)
        select.grid(row=5, column=1, padx=8, pady=8)

        stopsWindow.mainloop()



def enterPrompt():
    if (firstStopMenu.get() == "" or secStopMenu.get() == ""):
        showinfo("Error", "First Stop and Second Stop Inputs Have To Be Defined")

    elif (firstStopMenu.get() == secStopMenu.get()):
        showinfo("Error", "Please Try Again with Two Different Inputs")


class busStop:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class theBus:
    def __init__(self,currentStop):
        self.currentStop = currentStop
        self.now = datetime.datetime.now()

class busStopRoute:
    def __init__(self, stopArray, bus1, bus2, bus3):
        self.stopArray = stopArray
        self.bus1 = bus1
        self.bus2 = bus2
        self.bus3 = bus3

    def addStop(self, busStop):
        self.stopArray.append(busStop)

    def printList(self):
        for i in self.stopArray:
            print(i.name + ", " + i.location)

    def getAddr(self, index):
        return self.stopArray[index].location

    def nextStop(self, busStop):
        for i in range(len(self.stopArray) - 1):
            if (i == len(self.stopArray) - 1):
                return self.stopArray[0]
            else:
                return self.stopArray[i + 1]



ARC = busStop("Allison Road Classrooms", "607 Allison Rd, Piscataway, NJ 08854")
liviPlaza = busStop("Livingston Plaza", "55 Rockafeller Rd, Piscataway, NJ 08854")
BSC = busStop("Busch Student Center", "604 Bartholomew Rd, Piscataway, NJ 08854")
blHealthCenter = busStop("Busch-Livingston Health Center", "110 Hospital Rd, Piscataway, NJ 08854")
hillCenter = busStop("Hill Center", "Hill Center, Piscataway, NJ 08854")
CASC = busStop("College Avenue Student Center", "126 College Ave, New Brunswick, NJ 08901")
collegeHall = busStop("College Hall", "125 George St, New Brunswick, NJ 08901")
redOakLane = busStop("Red Oak Lane", "64 Nichol Ave, New Brunswick, NJ 08901")
gibbons = busStop("Gibbons", "New Gibbons Residence Campus, New Brunswick, NJ 08901")
lipman = busStop("Lipman Hall", "69 Dudley Rd, New Brunswick, NJ 08901")
bielRoad = busStop("Biel Road", "Parking Lot 76, New Brunswick, NJ 08901")
LSC = busStop("Livingston Student Center", "84 Joyce Kilmer Ave, Piscataway, NJ 08854")
soCamApt = busStop("So Cam Apartments", "290 George St, New Brunswick, NJ 08901")
stadiumWestLot = busStop("Stadium West Lot", "Stadium West Lot, Sutphen Rd Piscataway, NJ 08854")
henderson = busStop("Henderson", "Henderson Apartments New Brunswick, NJ 08901")
SAC = busStop("Student Activities Center", "613 George St, New Brunswick, NJ 08901")
werblinMain = busStop("Werblin Main Entrance", "656 Bartholomew Rd, Piscataway, NJ 08854")
sciencesBuilding = busStop("Sciences Building", "607 Allison Rd, Piscataway, NJ 08854")
werblinRec = busStop("Werblin Recreation Center", "656 Bartholomew Rd, Piscataway, NJ 08854")
Yard = busStop("The Yard", "40 College Ave, New Brunswick, NJ 08901")





routesNames = [
    "REXL",
    "REXB",
    "LX",
    "H",
    "F",
    "EE",
    "A",
    "B",
    "BHE",
    "C"
]


stopLists = [
    "Allison Road Classrooms",
    "Biel Road",
    "Busch Student Center",
    "Busch-Livingston Health Center",
    "College Avenue Student Center",
    "College Hall",
    "Gibbons",
    "Henderson",
    "Hill Center",
    "Lipman Hall",
    "Livingston Plaza",
    "Livingston Student Center",
    "Red Oak Lane",
    "Sciences Building",
    "Staduim West Lot",
    "So Cam Apartments",
    "Student Activities Center",
    "The Yard",
    "Werblin Main Entrance",
    "Werblin Recreation Center"
]


busREXL1 = theBus(redOakLane)
busREXL2 = theBus(collegeHall)
busREXL3 = theBus(liviPlaza)

AllStopsList = []
AllStops = busStopRoute(AllStopsList, busREXL1, busREXL2, busREXL3)
AllStops.addStop(ARC)
AllStops.addStop(bielRoad)
AllStops.addStop(BSC)
AllStops.addStop(blHealthCenter)
AllStops.addStop(CASC)
AllStops.addStop(collegeHall)
AllStops.addStop(gibbons)
AllStops.addStop(henderson)
AllStops.addStop(hillCenter)
AllStops.addStop(lipman)
AllStops.addStop(liviPlaza)
AllStops.addStop(LSC)
AllStops.addStop(redOakLane)
AllStops.addStop(sciencesBuilding)
AllStops.addStop(stadiumWestLot)
AllStops.addStop(soCamApt)
AllStops.addStop(SAC)
AllStops.addStop(Yard)
AllStops.addStop(werblinMain)
AllStops.addStop(werblinRec)

busREXB1 = theBus(redOakLane)
busREXB2 = theBus(collegeHall)
busREXB3 = theBus(hillCenter)

busLX1 = theBus(LSC)
busLX2 = theBus(CASC)
busLX3 = theBus(SAC)

busH1 = theBus(BSC)
busH2 = theBus(CASC)
busH3 = theBus(SAC)

busF1 = theBus(CASC)
busF2 = theBus(redOakLane)
busF3 = theBus(gibbons)

busEE1 = theBus(CASC)
busEE2 = theBus(redOakLane)
busEE3 = theBus(collegeHall)

busA1 = theBus(CASC)
busA2 = theBus(SAC)
busA3 = theBus(BSC)

busB1 = theBus(LSC)
busB2 = theBus(hillCenter)
busB3 = theBus(BSC)

busBHE1 = theBus(LSC)
busBHE2 = theBus(hillCenter)
busBHE3 = theBus(BSC)

busC1 = theBus(stadiumWestLot)
busC2 = theBus(hillCenter)
busC3 = theBus(ARC)

REXLNamesList = [
    "Red Oak Lane",
    "Lipman Hall",
    "College Hall",
    "Livingston Plaza",
    "Livingston Student Center"
]

routeREXLList = []
routeREXL = busStopRoute(routeREXLList, busREXL1, busREXL2, busREXL3)
routeREXL.addStop(redOakLane)
routeREXL.addStop(lipman)
routeREXL.addStop(collegeHall)
routeREXL.addStop(liviPlaza)
routeREXL.addStop(LSC)

REXBList = [
    "Red Oak Lane",
    "Lipman Hall",
    "College Hall",
    "Hill Center",
    "Allison Road Classrooms",
]

routeREXBList = []
routeREXB = busStopRoute(routeREXBList, busREXB1, busREXB2, busREXB3)
routeREXB.addStop(redOakLane)
routeREXB.addStop(lipman)
routeREXB.addStop(collegeHall)
routeREXB.addStop(hillCenter)
routeREXB.addStop(ARC)
routeREXB.addStop(hillCenter)

LXList = [
    "Livingston Student Center",
    "College Avenue Student Center",
    "The Yard",
    "Student Activities Center",
    "Livingston Plaza"
]

routeLXList = []
routeLX = busStopRoute(routeLXList, busLX1, busLX2, busLX3)
routeLX.addStop(LSC)
routeLX.addStop(CASC)
routeLX.addStop(Yard)
routeLX.addStop(SAC)
routeLX.addStop(liviPlaza)



EEList = [
    "College Avenue Student Center",
    "The Yard",
    "So Cam Apartments",
    "Red Oak Lane",
    "Lipman Hall",
    "Biel Road",
    "Henderson",
    "Gibbons",
    "College Hall",
    "Student Activities Center"
]


routeEEList = []
routeEE = busStopRoute(routeEEList, busEE1, busEE2, busEE3)
routeEE.addStop(CASC)
routeEE.addStop(Yard)
routeEE.addStop(soCamApt)
routeEE.addStop(redOakLane)
routeEE.addStop(lipman)
routeEE.addStop(bielRoad)
routeEE.addStop(henderson)
routeEE.addStop(gibbons)
routeEE.addStop(collegeHall)
routeEE.addStop(SAC)

HList = [
    "Busch Student Center",
    "Allison Road Classrooms",
    "Hill Center",
    "Stadium West Lot",
    "College Avenue Student Center",
    "The Yard",
    "Student Activities Center",
    "Werblin Recreation Center"
]

routeHList = []
routeH = busStopRoute(routeHList, busH1, busH2, busH3)
routeH.addStop(BSC)
routeH.addStop(ARC)
routeH.addStop(hillCenter)
routeH.addStop(stadiumWestLot)
routeH.addStop(CASC)
routeH.addStop(Yard)
routeH.addStop(SAC)
routeH.addStop(werblinRec)

FList = [
    "College Avenue Student Center",
    "The Yard",
    "Red Oak Lane",
    "Lipman Hall",
    "Biel Road",
    "Henderson",
    "Gibbons",
    "College Hall",
    "Student Activities Center"
]

routeFList = []
routeF = busStopRoute(routeFList, busF1, busF2, busF3)
routeF.addStop(CASC)
routeF.addStop(Yard)
routeF.addStop(redOakLane)
routeF.addStop(lipman)
routeF.addStop(bielRoad)
routeF.addStop(henderson)
routeF.addStop(gibbons)
routeF.addStop(collegeHall)
routeF.addStop(SAC)



CList = [
    "Stadium West Lot",
    "Hill Center",
    "Allison Road Classrooms",
]

routeCList = []
routeC = busStopRoute(routeCList, busC1, busC2, busC3)
routeC.addStop(stadiumWestLot)
routeC.addStop(hillCenter)
routeC.addStop(ARC)

AList = [
    "College Avenue Student Center",
    "The Yard",
    "Student Activities Center",
    "Stadium West Lot",
    "Hill Center",
    "Sciences Building",
    "Busch Student Center",
    "Werblin Main Entrance"
]

routeAList = []
routeA = busStopRoute(routeAList, busA1, busA2, busA3)
routeA.addStop(CASC)
routeA.addStop(Yard)
routeA.addStop(SAC)
routeA.addStop(stadiumWestLot)
routeA.addStop(hillCenter)
routeA.addStop(sciencesBuilding)
routeA.addStop(BSC)
routeA.addStop(werblinMain)

BList = [
    "Livingston Student Center",
    "Hill Center",
    "Sciences Building",
    "Busch Student Center",
    "Livingston Plaza"
]

routeBList = []
routeB = busStopRoute(routeBList, busB1, busB2, busB3)
routeB.addStop(LSC)
routeB.addStop(hillCenter)
routeB.addStop(sciencesBuilding)
routeB.addStop(BSC)
routeB.addStop(liviPlaza)

BHEList = [
    "Livingston Student Center",
    "Busch-Livingston Health Center",
    "Hill Center",
    "Sciences Building",
    "Busch Student Center",
    "Livingston Plaza"
]

routeBHEList = []
routeBHE = busStopRoute(routeBHEList, busBHE1, busBHE2, busBHE3)
routeBHE.addStop(LSC)
routeBHE.addStop(blHealthCenter)
routeBHE.addStop(hillCenter)
routeBHE.addStop(sciencesBuilding)
routeBHE.addStop(BSC)
routeBHE.addStop(liviPlaza)


routesListList = [
    REXLNamesList,
    REXBList,
    LXList,
    HList,
    FList,
    EEList,
    AList,
    BList,
    BHEList,
    CList
]

routeList = [
    routeREXL,
    routeREXB,
    routeLX,
    routeH,
    routeF,
    routeEE,
    routeA,
    routeB,
    routeBHE,
    routeC
]


LOR = np.array(routesListList)


homepage.mainloop()