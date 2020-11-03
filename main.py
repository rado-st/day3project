wayQuestion = "\n\nYou\'re at a crossroad, where do you want to go? Type 'left' or 'right'. "
actionQuestion = '\n\nYou\'ve come to a lake. There is an island in the middle of the lake. Type \'wait\' to wait for a boat. Type \'swim\' to swim across. '
colorQuestion = '\n\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? '

asciiArt = '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'''



def startGame():
    print("\n\nWelcome to Treasure Island.\nYour mission is to find the treasure.\n\n")
    way = input(wayQuestion).lower()
    chooseWay(way)

def gameOver():
    restart = input("\n\nWould you like to try again? Type 'y/yes' or 'n/no'. ").lower()

    
    if restart[0] == 'y':
        startGame()
    elif restart[0] == 'n':
        print('\n\nThank you for playing the game.\n\n');
        exit()
    else:
        gameOver()

        

def chooseWay(way):
    if way == 'left':
        action = input(actionQuestion).lower()
        chooseAction(action)
    elif way == 'right':
        print('You fell into a hole. Game Over.\n')
        gameOver()
    else:
        print("\n\nYou fool, I have asked you to choose left or right... \n\n")
        newWay = input(wayQuestion).lower()
        chooseWay(newWay)

def chooseAction(action):
    if action == 'swim':
        print('\n\nYou got attacked by a Murloc, ugly creatures... Game Over. \n\n')
        gameOver()
    elif action == 'wait':
        color = input(colorQuestion).lower()
        chooseColor(color)
    else:
        print("\n\nYou fool, you can only swim or wait... \n\n")
        newAction = input(actionQuestion).lower()
        chooseAction(newAction)

def chooseColor(color):
    if color == 'yellow':
        print('\n\nYou found a treasure! You Win!\n\n')
        gameOver()
    elif color == 'red':
        print('\n\nIt\'s a room full of fire. Game Over.\n\n')
        gameOver()
    elif color == 'blue':
        print('\n\nIt\'s a room full of beasts. Game Over.\n\n')
        gameOver()
    else:
        print("\n\n... How many times do I have to ask you to say a correct answer? \n\n")
        newColor = input(colorQuestion).lower()
        chooseColor(newColor)

print(asciiArt)
input('Click enter to start the game')
startGame()
