#####################################################################################################################################
#                                                                                                                                   #
#TITLE:  TOWER DEFENSE                                                                                                              #
#                                                                                                                                   #
#PURPOSE:  A TOWER DEFENSE VIDEO GAME THAT SHOWS HOW TO COMBINE GRAPHICS, USER INTERACTIONS, AND SCORE-KEEPING IN A PYTHON PROGRAM  #
#                                                                                                                                   #
#DATE LAST MODIFIED: 01/24/2014                                                                                                     #
#                                                                                                                                   #
#PROGRAMMER: ESSA SAEED                                                                                                             #
#                                                                                                                                   #
#####################################################################################################################################

from Tkinter import *
from math import *
from time import *

#CREATES THE CANVAS
root = Tk()
root.wm_title("Tower Defense")
screen = Canvas( root, width = 800, height = 800, background = "orange" )
screen.pack()

def setInitialValues():
    #SETS "SOME" VARIABLES GLOBAL FOR OTHER FUNCTIONS TO UTILIZE
    global gameRunning
    global wave1, turretImageFile, enemyImageFile, knightImageFile
    global xMouse, yMouse, mouseDown
    global turret, turretPositions, turretRange, turretBeingMoved
    global turretWidth, turretHeight, xTurret, yTurret
    global xTurretShop, yTurretShop, turretShopWidth, turretShopHeight
    global enemyX, enemyY, enemyHealth, enemyTotalHealth, enemyUnitReward
    global money, moneyDisplay, turretPrice, knightPrice
    global pastPointsArray, hearts, heartImageFile
    global xKnightShop, yKnightShop, knightShopWidth, knightShopHeight, knightBeingMoved
    global xKnight, yKnight, knightPositions
    global charizardPositions, xCharizard, yCharizard, xCharizardShop, yCharizardShop
    global charizardShopWidth, charizardShopHeight, charizardPrice, charizard
    global charizardBeingMoved, charizardImageFile
    global tankX, tankY, tankHealth, tankTotalHealth, tankReward, tankImageFile
    
    #AN ARRAY THAT STORES ALL THE COORDINATES OF PLACED TURRETS
    turretPositions = []

    knightPositions = []

    charizardPositions = []

    #AN ARRAY THAT STORES ALL PAST POINTS THAT A UNIT HAS TRAVELLED FOR FUTURE REFERENCE, SO AS TO NOT GO BACK TO A PREVIOUS POINT
    pastPointsArray = []

    #IMPORT IMAGE FILES
    #menuImageFile = PhotoImage(file = "PTD LOGO.gif")
    turretImageFile = PhotoImage(file = "Squirtle.gif")
    knightImageFile = PhotoImage(file = "Bulbasaur.gif")
    charizardImageFile = PhotoImage(file = "Charizard2 copy.gif")
    enemyImageFile = PhotoImage(file = "Gastly.gif")
    tankImageFile = PhotoImage(file = "haunter.gif")
    bossImageFile = PhotoImage(file = "Mewtwo.gif")
    heartImageFile = PhotoImage(file = "Heart.gif")

    enemyHealth = 40
    enemyTotalHealth = 40

    tankHealth = 100
    tankTotalHealth = 100

    tankX = 800
    tankY = 450

    #CURRENT POSITION OF THE MOUSE
    xMouse = 400
    yMouse = 400

    #CURRENT POSITION OF THE FIRST TURRET
    xTurret = 75
    yTurret = 675

    #DIMENSIONS OF THE FIRST TURRET
    turretWidth = 50
    turretHeight = 50

    #POSITION OF THE FIRST TURRET IN THE SHOP
    xTurretShop = 75
    yTurretShop = 675

    #DIMENSIONS OF THE FIRST TURRET IN THE SHOP
    turretShopWidth = 50
    turretShopHeight = 50

    #CURRENT POSITION OF THE SECOND TURRET
    xKnight = 225
    yKnight = 675

    #POSITION OF THE SECOND TURRET IN THE SHOP
    xKnightShop = 225
    yKnightShop = 675

    #DIMENSIONS OF THE SECOND TURRET IN THE SHOP
    knightShopWidth = 50
    knightShopHeight = 50

    knightPrice = 100

    #CURRENT POSITION OF THE SECOND TURRET
    xCharizard = 375
    yCharizard = 675

    #POSITION OF THE SECOND TURRET IN THE SHOP
    xCharizardShop = 375
    yCharizardShop = 675

    #DIMENSIONS OF THE SECOND TURRET IN THE SHOP
    charizardShopWidth = 50
    charizardShopHeight = 50

    charizardPrice = 200

    money = 100
    
    #CREATES IMAGE FOR THE FIRST TURRET
    turretShop = screen.create_image(xTurret, yTurret, image = turretImageFile)

    #CREATES IMAGE FOR THE SECOND TURRET
    knightShop = screen.create_image(xKnight, yKnight, image = knightImageFile)

    #CREATES IMAGE FOR THE THIRD TURRET
    charizardShop = screen.create_image(xCharizard, yCharizard, image = charizardImageFile)


    turretPrice = 50
    
    turretPriceDisplay = screen.create_text(xTurret, yTurret+50, text = "Price: $" + str(turretPrice))

    knightPriceDisplay = screen.create_text(xKnight, yKnight+50, text = "Price: $" + str(knightPrice))

    charizardPriceDisplay = screen.create_text(xCharizard, yCharizard+50, text = "Price: $" + str(charizardPrice))
    
    #GAME DATA
    wave1 = 5
    hearts = 3
    enemyUnitReward = 50
    tankReward = 100

    #SETS MOVEMENT-INDUCING VARIABLES TO FALSE
    mouseDown = False
    turretBeingMoved = False
    knightBeingMoved = False
    charizardBeingMoved = False

    gameRunning = True
    
#    userQuit = False    #BECOMES TRUE IF THE USER PRESSES 'Q' OR 'q'
#    gameRunning = True  #BECOMES FALSE (i.e. THE GAME ENDS) IF THE USER QUITS OR GETS STUNG TOO MANY TIMES

def endGame():
    sleep(2)
    root.destroy()

def menu(): #CREATES THE MENU SCREEN FOR THE GAME
    #screen.create_rectangle(0,0,800,800, fill = "white", outline = "black")
    #screen.create_text( 400, 300, text = "Pokemon", font = "Times, 50")
    #screen.create_text(400, 350, text = "Tower Defense", font = "Times, 50")
    return True

def lives():    #KEEPS TRACK OF THE NUMBER OF LIVES AND CHANGES CHANGES LIVES DISPLAY ACCORDINGLY
    livesDisplay = screen.create_text(600, 625, text = "Lives: ")
    screen.create_rectangle(625, 620, 775, 650, fill = "grey", outline = "grey")
    for i in range(0, hearts):
        heart = screen.create_image(875 + i*50, 850, image = heartImageFile)

def loseLife(): #DECREASES A LIFE EVERYTIME AN ENEMY UNIT GETS INTO PLAYER'S TERRITORY
    global hearts
    hearts = hearts - 1
    lives()
    if hearts == 0:
        screen.create_rectangle(0,0,800,800, fill = "grey", outline = "black", width = 10)
        screen.create_text(400, 325, text = "GAME OVER", font = "Helvetica, 75")
        screen.update()
        sleep(1)
        endGame()
        #root.destroy()

def showCoordinatesButton():    #ALLOWS USER TO SPECIFY WHETHER OR NOT THEY WISH TO SEE THE COORDINATES ON THE GRID IN PYTHON TERMS
    return False

def gridButton():   #ALLOWS USER TO SPECIFY WHETHER OR NOT THEY WISH TO DISPLAY GRID LINES OR NOT
    return True

def background():   #CREATES THE BACKGROUND FOR THE GAME, AND CREATES THE SHOP AT THE BOTTOM OF THE SCREEN
    global rectangle, moneyDisplay, heart
    
    #EMPTY ARRAY FOR THE RECTANGLE COORDINATES WHERE BUILDING IS ALLOWED
    rectangle = []
    
    #APPENDS COORDINATES OF BUILDABLE LAND
    rectangle.append([100,0,900,50])
    rectangle.append([0,0,50,600])
    rectangle.append([0,150,700,250])
    rectangle.append([0,250,650,300])
    rectangle.append([750,300,900,350])
    rectangle.append([200,350,900,450])
    rectangle.append([50,300,150,600])
    rectangle.append([100,500,900,600])
    
    #CREATES THE GREEN BUILDABLE AREA OVERTOP THE "BROWN"(ORANGE) BACKKGROUND
    for i in range(0, len(rectangle)):
        screen.create_rectangle(rectangle[i][0],rectangle[i][1],rectangle[i][2],rectangle[i][3], fill = "green", outline = "green")

    #CREATES GREY SHOP
    screen.create_rectangle(4,600,800,800, fill = "grey", outline = "black", width = 2)

    #CREATES MONEY DISPLAY, SHOP "TURRET" IMAGES, AND THEIR CORRESPONDING PRICE DISPLAYS 
    moneyDisplay = screen.create_text(700, 675, text = "Money: $" + str(money))

    turretPriceDisplay = screen.create_text(xTurret, yTurret+50, text = "Price: $" + str(turretPrice))
    turretShop = screen.create_image(xTurret, yTurret, image = turretImageFile)

    knightPriceDisplay = screen.create_text(xKnight, yKnight+50, text = "Price: $" + str(knightPrice))
    knightShop = screen.create_image(xKnight, yKnight, image = knightImageFile)

    charizardPriceDisplay = screen.create_text(xCharizard, yCharizard+50, text = "Price: $" + str(charizardPrice))
    charizardShop = screen.create_image(xCharizard, yCharizard, image = charizardImageFile)
    
def grid():     #CREATES 50X50 GRID
    if gridButton() == True:
        #CREATES THE X-GRID FOR EASY PLACING AND TACTICAL DECISION MAKING
        for x in range (0,16):
            xPos = 50 * x
            screen.create_line(xPos, 0, xPos, 600, fill = "black", width = 1)
        #CREATES THE Y-GRID FOR EASY PLACING AND TACTICAL DECISION MAKING
        for y in range (0,13):
            yPos = 50 * y
            screen.create_line(0, yPos, 800, yPos, fill = "black", width = 1)
        if showCoordinatesButton() == True: #CHECKS TO SEE IF USER WANTS THE COORDINATES OF THE GRID TO BE DISPLAYED
            for i in range (0,16):
                for j in range (0,12):
                    screen.create_text(50*i + 25, 50*j + 25, text = "(" + str(50*i+25) + "," + str(50*j+25) + ")")

def isPointInRectangle(point):  #CHECKS TO SEE IF A COORDINATE IS ON THE GREEN BUILDABLE AREA OR NOT
    #rectangle = [0,0,100,40]

    #FLAG KEEPS TRACK OF THE NUMBER OF MIS-MATCHES OF POINT AND RECTANGLE
    #IF FLAG = THE NUMBER OF RECTANGLES, THEN IT IS NOT INSIDE AN ALLOWED RECTANGLE
    flag = 0
    
    for i in range (0, len(rectangle)):
        #OBTAINS DATA FROM EACH RECTANGLE IN THE FORM: (X1, Y1) AND (X2, Y2)
        xMax = rectangle[i][0]
        yMax = rectangle[i][1]
        xMin = rectangle[i][2]
        yMin = rectangle[i][3]

        #point = [17,31]
        #OBTAINS THE DATA FROM THE POINT THAT WAS PASSED IN IN THE FORM: (X, Y)
        x = point[0]
        y = point[1]

        #CHECKS TO SEE IF THE POINT IS WITHIN THE RECTANGLE
        if x >= xMax and x <= xMin and y >= yMax and y <= yMin:
            return True
        else:
            flag = flag + 1
            
    if flag == len(rectangle):
        return False

#THIS PROGRAM WAS MEANT TO GIVE THE ENEMY UNITS AN ARTIFICIAL INTELLIGENCE WHERE THEY WOULD CHECK THEMSELVES WHERE THEY SHOULD MOVE NEXT 
##def enemyController(previousPoint, currentPoint):   #CHECKS TO SEE WHERE THE ENEMY UNIT WILL GO NEXT, ENSURES THAT THE UNIT DOES NOT TRAVEL BACKWARDS
##    global pastPointsArray
##    check = 50
##    
##    preX = previousPoint[0]
##    preY = previousPoint[1]
##
##    pastPointsArray.append([preX, preY])
##    
##    curX = currentPoint[0]
##    curY = currentPoint[1]
##
##    for i in range (0, len(pastPointsArray)):
##        
##        #CHECK UP
##        if (curY - check != pastPointsArray[i][1] or curX != pastPointsArray[i][0]) and isPointInRectangle([curX, curY - check]) == False:
##            possiblePoint = [curX, curY - check]
##
##        #CHECK LEFT
##        elif (curX - check != pastPointsArray[i][0] or curY != pastPointsArray[i][1]) and isPointInRectangle([curX - check, curY]) == False:
##            possiblePoint = [curX - check, curY]
##        
##        #CHECK RIGHT
##        elif (curX + check != pastPointsArray[i][0] or curY != pastPointsArray[i][1]) and isPointInRectangle([curX + check, curY]) == False:
##            possiblePoint = [curX + check, curY]
##
##        #CHECK DOWN
##        elif (curY + check != pastPointsArray[i][1] or curX != pastPointsArray[i][0]) and isPointInRectangle([curX, curY + check]) == False:
##            possiblePoint = [curX, curY + check]
##
##    nextPoint = possiblePoint
##    return nextPoint
##

def enemyTrial():
    global enemyX, enemyY, money, moneyDisplay, unit
    global previousPoint, currentPoint, enemyUnitAlive
    
    #SETS THE PATH FOR THE ENEMY UNIT TO FOLLOW
    enemyX = 775
    enemyY = 475
    speed = 5

    enemyUnitAlive = True

    previousPoint = [825, 475]
    currentPoint = [enemyX, enemyY]

    #previousPoint = currentPoint
    
    if enemyUnitAlive == True:

        if enemyY == 475:
            while enemyX != 175 and enemyUnitAlive == True:
                enemyX = enemyX - speed
                #FOLLOWING RECTANGLES SHOW HEALTH BAR OF ENEMY UNIT
                barBorder = screen.create_rectangle(enemyX - 20, enemyY -50, enemyX + 20, enemyY -40, fill="white", outline="black")
                healthBar = screen.create_rectangle(enemyX - 20, enemyY -50, (enemyX + 20) - (enemyTotalHealth - enemyHealth), enemyY -40, fill="red")

                unit = screen.create_image(enemyX, enemyY, image = enemyImageFile)

                screen.update()
                sleep(0.05)
                screen.delete(unit)
              
                screen.delete(barBorder)
                screen.delete(healthBar)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()
                
            while enemyY != 325 and enemyUnitAlive == True:
                enemyY = enemyY - speed
                barBorder = screen.create_rectangle(enemyX - 20, enemyY -50, enemyX + 20, enemyY -40, fill="white", outline="black")
                healthBar = screen.create_rectangle(enemyX - 20, enemyY -50, (enemyX + 20) - (enemyTotalHealth - enemyHealth), enemyY -40, fill="red")

                unit = screen.create_image(enemyX, enemyY, image = enemyImageFile)
              
                screen.update()
                sleep(0.05)
                screen.delete(unit)
             
                screen.delete(barBorder)
                screen.delete(healthBar)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()
                
            while enemyX != 725 and enemyUnitAlive == True:
                enemyX = enemyX + speed
                barBorder = screen.create_rectangle(enemyX - 20, enemyY -50, enemyX + 20, enemyY -40, fill="white", outline="black")
                healthBar = screen.create_rectangle(enemyX - 20, enemyY -50, (enemyX + 20) - (enemyTotalHealth - enemyHealth), enemyY -40, fill="red")

                unit = screen.create_image(enemyX, enemyY, image = enemyImageFile)
              
                screen.update()
                sleep(0.05)
                screen.delete(unit)

                screen.delete(barBorder)
                screen.delete(healthBar)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()

            while enemyY != 125 and enemyUnitAlive == True:
                enemyY = enemyY - speed
                barBorder = screen.create_rectangle(enemyX - 20, enemyY -50, enemyX + 20, enemyY -40, fill="white", outline="black")
                healthBar = screen.create_rectangle(enemyX - 20, enemyY -50, (enemyX + 20) - (enemyTotalHealth - enemyHealth), enemyY -40, fill="red")

                unit = screen.create_image(enemyX, enemyY, image = enemyImageFile)
               
                screen.update()
                sleep(0.05)
                screen.delete(unit)
                
                screen.delete(barBorder)
                screen.delete(healthBar)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()

            while enemyX != 75 and enemyUnitAlive == True:
                enemyX = enemyX - speed
                barBorder = screen.create_rectangle(enemyX - 20, enemyY -50, enemyX + 20, enemyY -40, fill="white", outline="black")
                healthBar = screen.create_rectangle(enemyX - 20, enemyY -50, (enemyX + 20) - (enemyTotalHealth - enemyHealth), enemyY -40, fill="red")

                unit = screen.create_image(enemyX, enemyY, image = enemyImageFile)
                #unit2 = screen.create_image(enemyX + 50, enemyY, image = enemyImageFile)
                
                screen.update()
                sleep(0.05)
                screen.delete(unit)

                #screen.delete(unit2)
                
                screen.delete(barBorder)
                screen.delete(healthBar)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()

            while enemyY != 0 and enemyUnitAlive == True:
                enemyY = enemyY - speed
                barBorder = screen.create_rectangle(enemyX - 20, enemyY -50, enemyX + 20, enemyY -40, fill="white", outline="black")
                healthBar = screen.create_rectangle(enemyX - 20, enemyY -50, (enemyX + 20) - (enemyTotalHealth - enemyHealth), enemyY -40, fill="red")

                unit = screen.create_image(enemyX, enemyY, image = enemyImageFile)
                
                screen.update()
                sleep(0.05)
                screen.delete(unit)
                
                screen.delete(barBorder)
                screen.delete(healthBar)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()

            if enemyX <= 75 and enemyY == 0:
                loseLife()

            if enemyUnitAlive == False:
                enemyX = 775
                enemyY = 475

def tankTrial():
    global tankX, tankY, money, moneyDisplay, tank
    global previousPoint, currentPoint, tankAlive
    
    #SETS THE PATH FOR THE ENEMY UNIT(S) TO FOLLOW
    tankX = 775
    tankY = 475
    speed = 5

    tankAlive = True

    previousPoint = [825, 475]
    currentPoint = [tankX, tankY]

    #previousPoint = currentPoint
    
    if tankAlive == True:

        if tankY == 475:
            while tankX != 175 and tankAlive == True:
                tankX = tankX - speed
                #FOLLOWING RECTANGLES SHOW HEALTH BAR OF ENEMY UNIT
                barBorder2 = screen.create_rectangle(tankX - 20, tankY -50, tankX + 20, tankY -40, fill="white", outline="black")
                healthBar2 = screen.create_rectangle(tankX - 20, tankY -50, (tankX + 20) - (tankTotalHealth - tankHealth), tankY -40, fill="red")

                tank = screen.create_image(tankX, tankY, image = tankImageFile)

                screen.update()
                sleep(0.1)
                screen.delete(tank)
                
                screen.delete(barBorder2)
                screen.delete(healthBar2)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()
                
            while tankY != 325 and tankAlive == True:
                tankY = tankY - speed
                barBorder2 = screen.create_rectangle(tankX - 20, tankY -50, tankX + 20, tankY -40, fill="white", outline="black")
                healthBar2 = screen.create_rectangle(tankX - 20, tankY -50, (tankX + 20) - (tankTotalHealth - tankHealth), tankY -40, fill="red")

                tank = screen.create_image(tankX, tankY, image = tankImageFile)

                screen.update()
                sleep(0.1)
                screen.delete(tank)
                
                screen.delete(barBorder2)
                screen.delete(healthBar2)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()
                
            while tankX != 725 and tankAlive == True:
                tankX = tankX + speed
                barBorder2 = screen.create_rectangle(tankX - 20, tankY -50, tankX + 20, tankY -40, fill="white", outline="black")
                healthBar2 = screen.create_rectangle(tankX - 20, tankY -50, (tankX + 20) - (tankTotalHealth - tankHealth), tankY -40, fill="red")

                tank = screen.create_image(tankX, tankY, image = tankImageFile)
                
                screen.update()
                sleep(0.1)
                screen.delete(tank)
                
                screen.delete(barBorder2)
                screen.delete(healthBar2)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()

            while tankY != 125 and tankAlive == True:
                tankY = tankY - speed
                barBorder2 = screen.create_rectangle(tankX - 20, tankY -50, tankX + 20, tankY -40, fill="white", outline="black")
                healthBar2 = screen.create_rectangle(tankX - 20, tankY -50, (tankX + 20) - (tankTotalHealth - tankHealth), tankY -40, fill="red")

                tank = screen.create_image(tankX, tankY, image = tankImageFile)
                
                screen.update()
                sleep(0.1)
                screen.delete(tank)
                
                screen.delete(barBorder2)
                screen.delete(healthBar2)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()

            while tankX != 75 and tankAlive == True:
                tankX = tankX - speed
                barBorder2 = screen.create_rectangle(tankX - 20, tankY -50, tankX + 20, tankY -40, fill="white", outline="black")
                healthBar2 = screen.create_rectangle(tankX - 20, tankY -50, (tankX + 20) - (tankTotalHealth - tankHealth), tankY -40, fill="red")

                tank = screen.create_image(tankX, tankY, image = tankImageFile)
                
                screen.update()
                sleep(0.1)
                screen.delete(tank)
                
                screen.delete(barBorder2)
                screen.delete(healthBar2)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()

            while tankY != 0 and tankAlive == True:
                tankY = tankY - speed
                barBorder2 = screen.create_rectangle(tankX - 20, tankY -50, tankX + 20, tankY -40, fill="white", outline="black")
                healthBar2 = screen.create_rectangle(tankX - 20, tankY -50, (tankX + 20) - (tankTotalHealth - tankHealth), tankY -40, fill="red")

                tank = screen.create_image(tankX, tankY, image = tankImageFile)
                
                screen.update()
                sleep(0.1)
                screen.delete(tank)
                
                screen.delete(barBorder2)
                screen.delete(healthBar2)
                isEnemyInRange()
                isKnightInRange()
                isCharizardInRange()

            if tankX <= 75 and tankY == 0:
                loseLife()

            if tankAlive == False:
                tankX = 775
                tankY = 475

def rawPointToSnapPoint(x):     #TAKES ANY POINT AND CONVERTS IT TO A CENTRAL COORDINATE
    xDiv = round(x / 50)
    xPos = xDiv * 50 + 25
    return xPos

def pointAlreadyTaken(point):   #FUNCTION CHECKS TO SEE IF THE SPOT HAS ALREADY BEEN BULILT ON
    x = point[0]
    y = point[1]
    for i in range (0, len(turretPositions)):
        xArray = turretPositions[i][0]
        yArray = turretPositions[i][1]

        if x == xArray and y == yArray:
            return True
    return False

def knightAlreadyTaken(point):   #FUNCTION CHECKS TO SEE IF THE SPOT HAS ALREADY BEEN BULILT ON
    x = point[0]
    y = point[1]
    for i in range (0, len(knightPositions)):
        xArray = knightPositions[i][0]
        yArray = knightPositions[i][1]

        if x == xArray and y == yArray:
            return True
    return False

def charizardAlreadyTaken(point):   #FUNCTION CHECKS TO SEE IF THE SPOT HAS ALREADY BEEN BULILT ON
    x = point[0]
    y = point[1]
    for i in range (0, len(charizardPositions)):
        xArray = charizardPositions[i][0]
        yArray = charizardPositions[i][1]

        if x == xArray and y == yArray:
            return True
    return False

def fire(x1, y1, x2, y2):   #X1, Y1 = TURRET COORDINATES, X2, Y2 = ENEMY COORDINATES
    global enemyHealth, money, moneyDisplay, enemyUnitAlive, tankHealth, tankAlive
    shot = screen.create_line(x1, y1, x2, y2, fill = "light blue", width = 2)
    enemyHealth = enemyHealth - 0.5
    screen.update()
    sleep(0.1)
    screen.delete(shot)
    if enemyHealth <= 0:
        enemyUnitAlive = False
        screen.delete(unit)
        money = money + enemyUnitReward
        screen.delete(moneyDisplay)
        moneyDisplay = screen.create_text(700, 675, text = "Money: $" + str(money))
    if tankHealth <= 0:
        tankAlive = False
        screen.delete(tank)
        money = money + tankReward
        screen.delete(moneyDisplay)
        moneyDisplay = screen.create_text(700, 675, text = "Money: $" + str(money))

def fireKnight(x1, y1, x2, y2):   #X1, Y1 = TURRET COORDINATES, X2, Y2 = ENEMY COORDINATES
    global enemyHealth, money, moneyDisplay, enemyUnitAlive, tankHealth, tankAlive
    shot = screen.create_line(x1, y1, x2, y2, fill = "turquoise", width = 4)
    enemyHealth = enemyHealth - 0.5
    screen.update()
    sleep(0.1)
    screen.delete(shot)
    if enemyHealth <= 0:
        enemyUnitAlive = False
#        enemyHealth = enemyTotalHealth
        screen.delete(unit)
        money = money + enemyUnitReward
        screen.delete(moneyDisplay)
        moneyDisplay = screen.create_text(700, 675, text = "Money: $" + str(money))
    if tankHealth <= 0:
        tankAlive = False
        screen.delete(tank)
        money = money + tankReward
        screen.delete(moneyDisplay)
        moneyDisplay = screen.create_text(700, 675, text = "Money: $" + str(money))

def fireCharizard(x1, y1, x2, y2):   #X1, Y1 = TURRET COORDINATES, X2, Y2 = ENEMY COORDINATES
    global enemyHealth, money, moneyDisplay, enemyUnitAlive, tankHealth, tankAlive
    shot = screen.create_line(x1, y1, x2, y2, fill = "dark orange", width = 7)
    enemyHealth = enemyHealth - 3
    screen.update()
    sleep(0.1)
    screen.delete(shot)
    if enemyHealth <= 0:
        enemyUnitAlive = False
        screen.delete(unit)
        money = money + enemyUnitReward
        screen.delete(moneyDisplay)
        moneyDisplay = screen.create_text(700, 675, text = "Money: $" + str(money))
    if tankHealth <= 0:
        tankAlive = False
        screen.delete(tank)
        money = money + tankReward
        screen.delete(moneyDisplay)
        moneyDisplay = screen.create_text(700, 675, text = "Money: $" + str(money))

def getDist( x1, y1, x2, y2 ):  #CALCULATES THE DISTANCE BETWEEN TWO POINTS
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )

def isEnemyInRange():   #CHECKS TO SEE IF THE ENEMY UNIT IS WITHIN THE RANGE OF THE FIRST TURRET
    for i in range (0, len(turretPositions)):
        xArray = turretPositions[i][0]
        yArray = turretPositions[i][1]
        if getDist(enemyX, enemyY, xArray, yArray) <= 90:
            fire(xArray, yArray, enemyX, enemyY)
        elif getDist(tankX, tankY, xArray, yArray) <= 90:
            fire(xArray, yArray, tankX, tankY)

def isKnightInRange():  #CHECKS TO SEE IF THE ENEMY UNIT IS WITHIN THE RANGE OF THE SECOND TURRET
    for i in range (0, len(knightPositions)):
        xArray = knightPositions[i][0]
        yArray = knightPositions[i][1]
        if getDist(enemyX, enemyY, xArray, yArray) <= 140:
            fireKnight(xArray, yArray, enemyX, enemyY)
        elif getDist(tankX, tankY, xArray, yArray) <= 140:
            fireKnight(xArray, yArray, tankX, tankY)

def isCharizardInRange():  #CHECKS TO SEE IF THE ENEMY UNIT IS WITHIN THE RANGE OF THE THIRD TURRET
    for i in range (0, len(charizardPositions)):
        xArray = charizardPositions[i][0]
        yArray = charizardPositions[i][1]
        if getDist(enemyX, enemyY, xArray, yArray) <= 90:
            fireCharizard(xArray, yArray, enemyX, enemyY)
        elif getDist(tankX, tankY, xArray, yArray) <= 90:
            fireCharizard(xArray, yArray, tankX, tankY)
        
def mouseInsideTurretImage():   #CHECKS TO SEE IF THE MOUSE IS INSIDE THE TURRET ICON IN THE SHOP
    if xMouse >= xTurretShop - turretShopWidth/2 and xMouse <= xTurretShop + turretShopWidth/2  and yMouse >= yTurretShop - turretShopHeight/2 and  yMouse <= yTurretShop + turretShopHeight/2:
        return True

    else:
        return False                                                                          

def mouseInsideKnightImage():
    if xMouse >= xKnightShop - knightShopWidth/2 and xMouse <= xKnightShop + knightShopWidth/2 and yMouse >= yKnightShop - knightShopHeight/2 and yMouse <= yKnightShop + knightShopHeight/2:
        return True
    
    else:
        return False

def mouseInsideCharizardImage():
    if xMouse >= xCharizardShop - charizardShopWidth/2 and xMouse <= xCharizardShop + charizardShopWidth/2 and yMouse >= yCharizardShop - charizardShopHeight/2 and yMouse <= yCharizardShop + charizardShopHeight/2:
        return True
    
    else:
        return False

def drawTurret():   #DRAWS THE TURRET AND SHOWS IT'S APPROPRIATE RANGE
    global turret, turretRange
    screen.delete(turret)
    try:
        screen.delete(turretRange)
    except:
        a = 0
    x = rawPointToSnapPoint(xTurret)
    y = rawPointToSnapPoint(yTurret)
    
    turretRange = screen.create_rectangle(x - 75, y - 75, x + 75, y + 75, outline="black", fill="blue", width=1, stipple="gray50")

    turret = screen.create_image(x, y, image=turretImageFile)

    screen.update()

def drawKnight():   #DRAWS THE KNIGHT AND SHOWS IT'S APPROPRIATE RANGE
    global knight, knightRange
    screen.delete(knight)
    try:
        screen.delete(knightRange)
    except:
        a = 0
    x = rawPointToSnapPoint(xKnight)
    y = rawPointToSnapPoint(yKnight)
    
    knightRange = screen.create_rectangle(x - 125, y - 125, x + 125, y + 125, outline="black", fill="blue", width=1, stipple="gray50")

    knight = screen.create_image(x, y, image=knightImageFile)

    screen.update()

def drawCharizard():   #DRAWS CHARIZARD AND SHOWS IT'S APPROPRIATE RANGE
    global charizard, charizardRange
    screen.delete(charizard)
    try:
        screen.delete(charizardRange)
    except:
        a = 0
    x = rawPointToSnapPoint(xCharizard)
    y = rawPointToSnapPoint(yCharizard)
    
    charizardRange = screen.create_rectangle(x - 75, y - 75, x + 75, y + 75, outline="black", fill="blue", width=1, stipple="gray50")

    charizard = screen.create_image(x, y, image=charizardImageFile)

    screen.update()

def quitCheck():    #CREATES GAME OVER SCREEN WHEN PLAYER QUITS
    if gameRunning == True:
        screen.create_rectangle(0,0,800,800,fill = "grey")
        screen.create_text(400,300, text = "GAME OVER", font = "Helvetica, 75")
        screen.update()
        sleep(1.5)
        root.destroy()

def congrats(): #CREATES CONGRATULATIONS SCREEN WHEN PLAYER WINS
    screen.create_rectangle(0,0,800,800, fill = "grey")
    screen.create_text(400,300, text = "CONGRATULATIONS", font = "Helvetica, 75")
    screen.create_text(400,350, text = "YOU WIN", font = "Helvetica, 50")

def mouseClickHandler( event ):     #CAPTURES MOUSE CLICKS
    global xMouse, yMouse, turretBeingMoved, mouseDown, turret, knight, knightBeingMoved
    global charizardBeingMoved, charizard
    
    xMouse = event.x
    yMouse = event.y

    mouseDown = True
    
    if mouseInsideTurretImage() == True and money >= turretPrice:
        turretBeingMoved = True
        turret = screen.create_image(xTurret, yTurret, image = turretImageFile)

    elif mouseInsideKnightImage() == True and money >= knightPrice:
        knightBeingMoved = True
        knight = screen.create_image(xKnight, yKnight, image = knightImageFile)

    elif mouseInsideCharizardImage() == True and money >= charizardPrice:
        charizardBeingMoved = True
        charizard = screen.create_image(xCharizard, yCharizard, image = charizardImageFile)

def mouseMotionHandler( event ):    #CAPTURES MOUSE MOVEMENT
    global xMouse, yMouse, xTurret, yTurret, xKnight, yKnight, xCharizard, yCharizard
    
    xMouse = event.x
    yMouse = event.y

    if mouseDown == True:
        if turretBeingMoved == True:
            xTurret = xMouse
            yTurret = yMouse
            drawTurret()

        elif knightBeingMoved == True:
            xKnight = xMouse
            yKnight = yMouse
            drawKnight()

        elif charizardBeingMoved == True:
            xCharizard = xMouse
            yCharizard = yMouse
            drawCharizard()

def mouseReleaseHandler( event ):   #CAPTURES MOUSE RELEASE LOCATION
    global mouseDown, turretBeingMoved, turret, turretPositions
    global money, moneyDisplay, knightBeingMoved, knight, knightPositions
    global charizardBeingMoved, charizardPositions, charizard

    x = rawPointToSnapPoint(event.x)
    y = rawPointToSnapPoint(event.y)

    if turretBeingMoved == True and mouseDown == True and isPointInRectangle([event.x,event.y]) == False or (pointAlreadyTaken([x,y]) == True or knightAlreadyTaken([x,y]) == True or charizardAlreadyTaken([x,y]) == True):
        screen.delete(turret)

    elif knightBeingMoved == True and mouseDown == True and isPointInRectangle([event.x,event.y]) == False or (pointAlreadyTaken([x,y]) == True or knightAlreadyTaken([x,y]) == True or charizardAlreadyTaken([x,y]) == True):
        screen.delete(knight)

    elif charizardBeingMoved == True and mouseDown == True and isPointInRectangle([event.x,event.y]) == False or (pointAlreadyTaken([x,y]) == True or knightAlreadyTaken([x,y]) == True or charizardAlreadyTaken([x,y]) == True):
        screen.delete(charizard)

    else:
        if turretBeingMoved == True:
            turretPositions.append([x,y])
            money = money - turretPrice #CHANGES MONEY DISPLAY WHEN A TURRET IS PURCHASED

        elif knightBeingMoved == True:
            knightPositions.append([x,y])
            money = money - knightPrice

        elif charizardBeingMoved == True:
            charizardPositions.append([x,y])
            money = money - charizardPrice

        screen.delete(moneyDisplay)    
        moneyDisplay = screen.create_text(700, 675, text = "Money: $" + str(money))

    turret = False
    mouseDown = False
    turretBeingMoved = False
    knightBeingMoved = False
    charizardBeingMoved = False
    
    try:
        screen.delete(turretRange)
    except:
        a = 0
    try:
        screen.delete(knightRange)
    except:
        a = 0
    try:
        screen.delete(charizardRange)
    except:
        a = 0

def getKeyStroke( event ):
    global gameRunning

    if event.keysym == "q" or event.keysym == "Q": #TESTS WHETHER THE USER PRESSED Q OR q
        gameRunning = False
        quitCheck()

    else:
        print("You just pushed the " + event.keysym + " key, but that doesn't do anything yet.")


#BINDS THE PROCEDURE mouseClickHandler TO ALL MOUSE-DOWN EVENTS
screen.bind("<Button-1>", mouseClickHandler)

#BINDS THE PROCEDURE mouseMotionHandler TO ALL MOUSE-MOTION EVENTS
screen.bind("<Motion>", mouseMotionHandler)

#BINDS THE PROCEDURE mouseReleaseHandler TO ALL MOUSE-UP EVENTS
screen.bind("<ButtonRelease-1>", mouseReleaseHandler)

#BINDS THE USER'S KEY-STROKES TO THE PROCEDURE getKeyStroke(), DEFINED ABOVE.
screen.bind("<Key>", getKeyStroke)

def rungame():  #MAIN LOOP FOR THE GAME
    global enemyHealth, tankHealth, gameRunning
#    gameRunning = True
    setInitialValues()
    if gameRunning == True:
        background()
        grid()
        lives()
        for num in range (0, wave1):
            enemyTrial()
            enemyHealth = enemyTotalHealth
        tankTrial()
        tankHealth = tankTotalHealth
    congrats()
        
rungame()
