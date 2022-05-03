import numpy as np
import datetime
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import requests

homepage = tk.Tk()

homeText = tk.Label(homepage, text="RU Riding", font=("Times New Roman", 40, 'bold'))
homeText.pack(side=tk.TOP)

homepageWindow = Canvas(homepage, width=600, height=600)
homepageWindow.pack(fill="both", expand=True)





homepageWindow.create_text(300, 50, text="This Program Will Show You the Different Bus Routes", font=("Times New Roman", 20))
homepageWindow.create_text(300, 75, text="Of Rutgers New Brunswick", font=("Arial", 20))
homepageWindow.create_text(300, 100, text="Please Select the Button Below to View Buses", font=("Times New Roman", 20))





homepage.title("RU Riding Application")



##############

def busRoutes():
    routesWin = tk.Tk()

    # routesWin.geometry("1920x1080")
    routesWin.title("Routes")
    label = tk.Label(routesWin, text="Choose a Route")
    label.grid(row=0, column=0, padx=8, pady=8)
    global routesMenu
    routesMenu = ttk.Combobox(routesWin, value=routesNames, width=20)
    routesMenu.grid(row=0, column=1, padx=8, pady=8)

    global routesselect
    routesselect = Button(routesWin, text="Submit", command=busStopList)
    routesselect.grid(row=5, column=1, padx=8, pady=8)

    homepageWindow.create_text(300, 400, text="Please Select Bus Route.", font=("Arial", 20))
    homepageWindow.create_text(300, 450, text="Then enter current stop and destination.", font=("Arial", 20))

    routesWin.mainloop()


studentPortal = tk.Button(homepage, text="Student Portal", command=busRoutes, font=("Arial", 20, 'bold'))
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
        stopWindow = tk.Tk()

        stopWindow.title("Bus Stops")
        startLabel = tk.Label(stopWindow, text="Choose First Stop")
        startLabel.grid(row=0, column=0, padx=8, pady=8)

        global options
        index = busSwitch(routesMenu.get())
        options = LOR[index]

        global routeSelectedNames
        routeSelectedNames = routesListList[index]

        global routeSelected
        routeSelected = routeList[index]

        global firstselected
        firstselected = StringVar()
        firstselected.set(options[0])

        global firststopsmenu
        firststopsmenu = ttk.Combobox(stopWindow, value=options, width=50)
        firststopsmenu.grid(row=0, column=1, padx=8, pady=8)

        def change_dropdown1(*args):
            print(firstselected.get())

        firstselected.trace('w', change_dropdown1)

        destinationLabel = tk.Label(stopWindow, text="Choose Second Stop")
        destinationLabel.grid(row=1, column=0, padx=8, pady=8)

        global secondselected
        secondselected = StringVar()
        secondselected.set(options[0])

        global secondstopsmenu
        secondstopsmenu = ttk.Combobox(stopWindow, value=options, width=50)
        secondstopsmenu.grid(row=1, column=1, padx=8, pady=8)

        def change_dropdown(*args):
            print(secondselected.get())

        secondselected.trace('w', change_dropdown)

        global select
        select = Button(stopWindow, text="Submit", command=submit)
        select.grid(row=5, column=1, padx=8, pady=8)

        stopWindow.mainloop()



def submit():
    if (firststopsmenu.get() == "" or secondstopsmenu.get() == ""):
        showinfo("Error", "Both input values need to be defined")

    elif (firststopsmenu.get() == secondstopsmenu.get()):
        showinfo("Error", "You can't select the same stop as the origin and destination. Please try again with a different input.")

    else:
        stopsOutput = tk.Tk()

        stopsOutput.geometry("675x600")
        stopsOutput.title("Route Summary")

        distanceBetweenStopsStringList = distanceBetweenStops(firststopsmenu.get(), secondstopsmenu.get())

        label1 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[0])
        label1.grid(row=0, column=0, padx=8, pady=8)

        label2 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[1])
        label2.grid(row=1, column=0, padx=8, pady=8)

        label3 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[2])
        label3.grid(row=2, column=0, padx=8, pady=8)

        label4 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[3])
        label4.grid(row=3, column=0, padx=8, pady=8)

        label5 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[4])
        label5.grid(row=4, column=0, padx=8, pady=8)

        label6 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[5])
        label6.grid(row=5, column=0, padx=8, pady=8)

        label7 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[6])
        label7.grid(row=6, column=0, padx=8, pady=8)

        label8 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[7])
        label8.grid(row=7, column=0, padx=8, pady=8)

        label9 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[8])
        label9.grid(row=8, column=0, padx=8, pady=8)

        label10 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[9])
        label10.grid(row=9, column=0, padx=8, pady=8)

        label14 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[10])
        label14.grid(row=10, column=0, padx=8, pady=8)

        label15 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[11])
        label15.grid(row=11, column=0, padx=8, pady=8)

        label16 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[12])
        label16.grid(row=12, column=0, padx=8, pady=8)

        label17 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[13])
        label17.grid(row=13, column=0, padx=8, pady=8)

        label18 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[14])
        label18.grid(row=14, column=0, padx=8, pady=8)

        label19 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[15])
        label19.grid(row=15, column=0, padx=8, pady=8)

        label20 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[16])
        label20.grid(row=16, column=0, padx=8, pady=8)

        label21 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[17])
        label21.grid(row=17, column=0, padx=8, pady=8)

        label22 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[18])
        label22.grid(row=18, column=0, padx=8, pady=8)

        label23 = tk.Label(stopsOutput, text=distanceBetweenStopsStringList[19])
        label23.grid(row=19, column=0, padx=8, pady=8)

        stopsOutput.mainloop()


def distanceFromBusToYou(youIndex, distanceBetweenStopsStringList):
    bus1stopName = routeSelected.bus1.currentStop.name
    bus2stopName = routeSelected.bus2.currentStop.name
    bus3stopName = routeSelected.bus3.currentStop.name
    yourStopName = routeSelected.stopArray[youIndex].name

    bus1Index = routeSelectedNames.index(bus1stopName)
    bus2Index = routeSelectedNames.index(bus2stopName)
    bus3Index = routeSelectedNames.index(bus3stopName)

    print("The first bus is at " + bus1stopName)
    print("The second bus is at " + bus2stopName)
    print("The third bus is at " + bus3stopName)

    global currentDateTime
    global distanceA
    currentDateTime = datetime.datetime.now()
    global totalDist
    global closestStopNameGlobal

    if (bus1Index == youIndex):
        #  print("busAlreadyAtStop")

        distanceA = 0
        distanceBetweenStopsStringList.append("There is a bus at stop " + yourStopName)
        return distanceBetweenStopsStringList
    elif (bus2Index == youIndex):
        distanceBetweenStopsStringList.append("There is a bus at stop " + yourStopName)
        #   print("busAlreadyAtStop")
        distanceA = 0
        return distanceBetweenStopsStringList
    elif (bus3Index == youIndex):
        distanceBetweenStopsStringList.append("There is a bus at stop " + yourStopName)
        #   print("busAlreadyAtStop")
        distanceA = 0
        return distanceBetweenStopsStringList
    elif (bus1Index < youIndex and bus2Index < youIndex and bus3Index < youIndex):
        closerStopName = bus3stopName
        i = bus3Index
    elif (bus1Index > youIndex and bus2Index > youIndex):
        if (bus1Index > bus2Index):
            closerStopName = bus2stopName
            i = bus2Index
        else:
            closerStopName = bus1stopName
            i = bus1Index
    elif (bus1Index > youIndex and bus2Index < youIndex):
        closerStopName = bus2stopName
        i = bus2Index
    elif (bus1Index < youIndex and bus2Index > youIndex):
        closerStopName = bus1stopName
        i = bus1Index
    elif (bus1Index < youIndex and bus2Index < youIndex and bus3Index > youIndex):
        closerStopName = bus2stopName
        i = bus2Index

    #  print("The closest bus is at stop " + closerStopName)
    distanceBetweenStopsStringList.append("The closest bus is at stop " + closerStopName)
    global resultStringA
    resultStringA = "The closest bus is at stop " + closerStopName

    #  print("The bus will depart from " + closerStopName + " at " + str(datetime.datetime.now().time()))
    distanceBetweenStopsStringList.append(
        "The bus will depart from " + closerStopName + " at " + str(datetime.datetime.now().time()))

    distance = 0

    while i != youIndex:
        if i == (len(routeSelected.stopArray) - 1):
            distance += int(
                getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[0].address).split(" ")[0])
            #  print("The bus will go from " + str(routeSelected.stopArray[i].name) + " to " + routeSelected.stopArray[0].name + " in " + getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[0].address).split(" ")[0] + " minutes, arriving at " + str((currentDateTime + datetime.timedelta(minutes = distance)).time()))
            distanceBetweenStopsStringList.append(
                "The bus will go from " + str(routeSelected.stopArray[i].name) + " to " + routeSelected.stopArray[
                    0].name + " in " +
                getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[0].address).split(" ")[
                    0] + " minutes, arriving at " + str(
                    (currentDateTime + datetime.timedelta(minutes=distance)).time()))

            if i != youIndex:
                i = 0
        else:
            distance += int(
                getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[i + 1].address).split(" ")[0])
            #    print("The bus will go from " + str(routeSelected.stopArray[i].name) + " to " + routeSelected.stopArray[i+1].name + " in " + getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[i+1].address).split(" ")[0] + " minutes, arriving at " + str((currentDateTime + datetime.timedelta(minutes = distance)).time()))
            distanceBetweenStopsStringList.append(
                "The bus will go from " + str(routeSelected.stopArray[i].name) + " to " + routeSelected.stopArray[
                    i + 1].name + " in " +
                getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[i + 1].address).split(" ")[
                    0] + " minutes, arriving at " + str(
                    (currentDateTime + datetime.timedelta(minutes=distance)).time()))
            if (i == (len(routeSelected.stopArray) - 2) and i + 1 != youIndex):
                #  print("MY NAME JEFF")
                distance += int(
                    getDistance(routeSelected.stopArray[i + 1].address, routeSelected.stopArray[0].address).split(" ")[
                        0])
                #  print("The bus will go from " + str(routeSelected.stopArray[i+1].name) + " to " + routeSelected.stopArray[0].name + " in " + getDistance(routeSelected.stopArray[i+1].address, routeSelected.stopArray[0].address).split(" ")[0] + " minutes, arriving at " +  str((currentDateTime + datetime.timedelta(minutes = distance)).time()))
                distanceBetweenStopsStringList.append(
                    "The bus will go from " + str(routeSelected.stopArray[i + 1].name) + " to " +
                    routeSelected.stopArray[0].name + " in " +
                    getDistance(routeSelected.stopArray[i + 1].address, routeSelected.stopArray[0].address).split(" ")[
                        0] + " minutes, arriving at " + str(
                        (currentDateTime + datetime.timedelta(minutes=distance)).time()))
                if (youIndex == i + 1):
                    break
                i = 0
            else:
                i = i + 1

    # print("The bus will be at your stop at " + str((currentDateTime + datetime.timedelta(minutes = distance)).time()))
    distanceBetweenStopsStringList.append("The bus is at your stop. You get on at " + str(
        (currentDateTime + datetime.timedelta(minutes=distance)).time()))

    distanceA = distance
    #  print("distance is " + str(distance))
    #   print("distanceA is " + str(distanceA))

    return distanceBetweenStopsStringList


def distanceBetweenStops(stop1Name, stop2Name):
    # distanceA = 0

    index1 = routeSelectedNames.index(stop1Name)
    index2 = routeSelectedNames.index(stop2Name)

    distanceBetweenStopsStringList = []

    distanceBetweenStopsStringList = distanceFromBusToYou(index1, distanceBetweenStopsStringList)

    i = index1
    print("Distance a is " + str(distanceA))

    distance = distanceA

    while i != index2:
        if i == (len(routeSelected.stopArray) - 1):
            distance += int(
                getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[0].address).split(" ")[0])
            # print("The bus will go from " + str(routeSelected.stopArray[i].name) + " to " + routeSelected.stopArray[0].name + " in " + getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[0].address).split(" ")[0] + " minutes, arriving at " + str((currentDateTime + datetime.timedelta(minutes = distance)).time()))
            distanceBetweenStopsStringList.append(
                "The bus will go from " + str(routeSelected.stopArray[i].name) + " to " + routeSelected.stopArray[
                    0].name + " in " +
                getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[0].address).split(" ")[
                    0] + " minutes, arriving at " + str(
                    (currentDateTime + datetime.timedelta(minutes=distance)).time()))
            if i != index2:
                i = 0
        else:
            distance += int(
                getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[i + 1].address).split(" ")[0])
            #   print("The bus will go from " + str(routeSelected.stopArray[i].name) + " to " + routeSelected.stopArray[i+1].name + " in " + getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[i+1].address).split(" ")[0] + " minutes, arriving at " + str((currentDateTime + datetime.timedelta(minutes = distance)).time()))
            distanceBetweenStopsStringList.append(
                "The bus will go from " + str(routeSelected.stopArray[i].name) + " to " + routeSelected.stopArray[
                    i + 1].name + " in " +
                getDistance(routeSelected.stopArray[i].address, routeSelected.stopArray[i + 1].address).split(" ")[
                    0] + " minutes, arriving at " + str(
                    (currentDateTime + datetime.timedelta(minutes=distance)).time()))
            if (i == (len(routeSelected.stopArray) - 2) and i + 1 != index2):
                #   print("MY NAME JEFF")
                distance += int(
                    getDistance(routeSelected.stopArray[i + 1].address, routeSelected.stopArray[0].address).split(" ")[
                        0])
                #    print("The bus will go from " + str(routeSelected.stopArray[i+1].name) + " to " + routeSelected.stopArray[0].name + " in " + getDistance(routeSelected.stopArray[i+1].address, routeSelected.stopArray[0].address).split(" ")[0] + " minutes, arriving at " +  str((currentDateTime + datetime.timedelta(minutes = distance)).time()))
                distanceBetweenStopsStringList.append(
                    "The bus will go from " + str(routeSelected.stopArray[i + 1].name) + " to " +
                    routeSelected.stopArray[0].name + " in " +
                    getDistance(routeSelected.stopArray[i + 1].address, routeSelected.stopArray[0].address).split(" ")[
                        0] + " minutes, arriving at " + str(
                        (currentDateTime + datetime.timedelta(minutes=distance)).time()))
                if (index2 == i + 1):
                    break
                i = 0
            else:
                i = i + 1

    distanceBetweenStopsStringList.append("The trip will take you a total of " + str(
        distance) + " minutes to arrive to " + stop2Name + ", and you will arrive at " + str(
        (currentDateTime + datetime.timedelta(minutes=distance)).time()))

    # print(distanceBetweenStopsStringList)      ##########################################################################################################################################################################################
    # return distance

    for j in range(len(distanceBetweenStopsStringList), 20):
        distanceBetweenStopsStringList.append("")

    totalDist = distance
    return distanceBetweenStopsStringList

















class busStop:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class theBus:
    def __init__(self,
                 currentStop):  ################################################################################################################################################################################################################################################
        self.currentStop = currentStop
        self.now = datetime.datetime.now()
    # print(self.now)


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
            print(i.name + ", " + i.address)

    def getAddr(self, index):
        return self.stopArray[index].address

    def nextStop(self, busStop):
        for i in range(len(self.stopArray) - 1):
            if (i == len(self.stopArray) - 1):
                return self.stopArray[0]
            else:
                return self.stopArray[i + 1]












def getDistance(origin, destination):
    apikey = "AIzaSyA7_ZgzwWNDelS0gUj3Y2mZ23CgIr383mQ"
    url1 = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations="
    url2 = "&origins="
    url3 = "&key="

    url_full = url1 + destination + url2 + origin + url3 + apikey

    output = requests.get(url_full).json()

    for obj in output['rows']:
        for data in obj['elements']:
            duration = data['duration']['text']

    return duration









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




############################

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