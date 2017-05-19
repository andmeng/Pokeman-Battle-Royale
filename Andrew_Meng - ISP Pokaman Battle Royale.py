#-----------------------------------------------------------------------------------#
# Name:        ISP - Pokaman Battle                                                 #
#                                                                                   #
# Purpose:                                                                          #
#   This program in essence is a game and is made to provide enterta-               #
#   inment. This game is called Pokaman Battle Royale or PBR for short. It is a     #
#   game with a Pokemon - style battle system. This means that the battles are      #
#   turn based and you have a select number of moves you can use. You also use      #
#   monsters to battle, not a humanoid character. PBR highly depends on graphical   #
#   user interfaces to receive commands/inputs from the player. The entire visual   #
#   and user-interactable component of PBR includes: A opening screen, a main menu, #
#   a shop screen, and a battle screen. The opening screen is basically a title     #
#   screen and just allows the user to start playing which will bring them to the   #
#   next parts of the opening (choosing your Pokaman). The main menu has several    #
#   sectors where input can be recorded. First there are two main buttons, one      #
#   brings the player to the shop screen, the other back to battle, both I will     #
#   discuss shortly. There are also displays of the player's team of monsters, and  #
#   a GUI that allows the player to switch the monster that will be used, and       #
#   discard any unwanted monsters. This main menu also displays the amount of money #
#   the player has which is obviously related to the shop. On the shop screen there #
#   are a variety of boxes in which a picture of a monster and its corresponding    #
#   price are. If the player has enough money (which is displayed at the bottom of  #
#   the screen), the player will purchase the monster and it will be automatically  #
#   added to their team. This screen also includes an exit button in upon clicking, #
#   will return the player to the main menu. The battle screen is where the main    #
#   gameplay occurs, the player will have a GUI on the bottom of the screen         #
#   displaying a set of moves (up to 4). Upon clicking any of the four, will use    #
#   the corresponding moves. Damage is done if the move lands on the enemy, and     #
#   after the player's turn is complete, the enemy automatically attacks. There are #
#   a variety of factors that are taken into account to calculate damage and exp,   #
#   two key points in a battle system. Damage factors include: Attacker's Attack,   #
#   Move's Accuracy, Move's Attack Power; the damage is then randomized in a range  #
#   based off the value calculated. The exp is done the same as the damage, however #
#   its factors only include the enemy defeated's level. Upon leveling up, the      #
#   corresponding monster of the player's will have an increase in stats and        #
#   potentially learn new moves depending on the level. Much of the game depends on #
#   randomization that factors in several aspects of the game. All of this creates  #
#   this program, Pokaman Battle Royale.                                            #
#                                                                                   #
# Author:      1mengand                                                             #
#                                                                                   #
# Created:     13/05/2015                                                           #
# Copyright:   (c) 1mengand 2015                                                    #
# Licence:     <your licence>                                                       #
#-----------------------------------------------------------------------------------#


from pygame import *    #import pygame library to use their functions
from random import *    #import random library to use functions such as randint

myClock = time.Clock()  #initialize the clock for smooth animations
init()                  #initialize pygame

#Defining colours

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 216, 0)
green = (0, 255, 33)

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   LOADING IMAGES, FONTS, DEFINING RECTANGLES AND SPRITES  #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


"""
This area is used to load all images used in the program as well as create any
necessary rectangles that may be used for buttons or animations (sprites). Related
images and rectangles will be loaded and created in the same areas.
"""

#Loading Fonts

myfont = font.SysFont("monospace", 16)                                                                          #Basic Font for Basic Text and Labels (e.g. HP, Name)
msgfont = font.SysFont("monospace", 28)                                                                         #Font used for screen messages during battle


#Opening Screen Background

main_bg = image.load("Resources/Images/ScreenBackgrounds/MainScreen.png")                                       #This is the opening screen's background
screen_rect = main_bg.get_rect()                                                                                #Get a rectangle the size of this background image. Will be used to change backgrounds in the program


#New Game Choice Screens
#Players have an option of three different Pokamans.
#Each option leads to a different screen

newgame_choicescreen = image.load("Resources/Images/ScreenBackgrounds/NewGameChoiceScreen.png")
gratachu_choice_screen = image.load("Resources/Images/ScreenBackgrounds/NewGameGratachuScreen.png")
watachu_choice_screen = image.load("Resources/Images/ScreenBackgrounds/NewGameWatachuScreen.png")
firachu_choice_screen = image.load("Resources/Images/ScreenBackgrounds/NewGameFirachuScreen.png")


#The following images are used for the ScreenSwapAnimation to create a fade effect

b1 = image.load("Resources/Images/Misc/FullDarkIE1.png")                                                        #different transparencies of black to simulate fade
b2 = image.load("Resources/Images/ScreenAnimation/FullDarkIE2.png")
b3 = image.load("Resources/Images/ScreenAnimation/FullDarkIE3.png")
b4 = image.load("Resources/Images/ScreenAnimation/FullDarkIE4.png")
b5 = image.load("Resources/Images/ScreenAnimation/FullDarkIE5.png")
b6 = image.load("Resources/Images/ScreenAnimation/FullDarkIE6.png")
b7 = image.load("Resources/Images/ScreenAnimation/FullDarkIE7.png")
b8 = image.load("Resources/Images/ScreenAnimation/FullDarkIE8.png")
b9 = image.load("Resources/Images/ScreenAnimation/FullDarkIE9.png")
b10 = image.load("Resources/Images/ScreenAnimation/FullDarkIE10.png")
b11= image.load("Resources/Images/ScreenAnimation/FullDarkIE11.png")

black_shades = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]                                                   #Include all images into a list to cut down code in the Animation function


#The battle screen's background

battle_screen_bg = image.load("Resources/Images/ScreenBackgrounds/BattleScreen.png")
battle_screen_bg_untouched = battle_screen_bg                                                                   #to leave an untouched version for each new battle. Used to clean off any lines drawn ontop of the image.


#Home Screen/Main Menu background

home_screen_bg = image.load("Resources/Images/ScreenBackgrounds/HomeScreen.png")


#Shop Screen background

shop_screen_bg = image.load("Resources/Images/ScreenBackgrounds/ShopBackground.png")


#Message box during battle

screen_msg_box = image.load("Resources/Images/ScreenMsgs/ScreenMsgBox.png")


#Render the following messages with the text loaded earlier (msgfont)

supereffective_msg = msgfont.render("Super effective!", 1, black)                                               #creating images with these texts
noteffective_msg = msgfont.render("Not very effective.", 1, black)
attack_missed_msg = msgfont.render("The attack missed.", 1, black)


#LOADING POKAMAN RELATED IMAGES

#Depending on whether a Pokaman is an ally or enemy, they have different sprite images

    #ally pokaman images
gratachu_ally = image.load("Resources/Images/Pokamans/GratachuAllySprite.png")
watachu_ally = image.load("Resources/Images/Pokamans/WatachuAllySprite.png")
firachu_ally = image.load("Resources/Images/Pokamans/FirachuAllySprite.png")

    #enemy pokaman images
gratachu_enemy = image.load("Resources/Images/Pokamans/GratachuEnemySprite.png")
watachu_enemy = image.load("Resources/Images/Pokamans/WatachuEnemySprite.png")
firachu_enemy = image.load("Resources/Images/Pokamans/FirachuEnemySprite.png")

    #pokaman name labels
gratachu_name = image.load("Resources/Images/Pokamans/GratachuNameLabel.png")
watachu_name = image.load("Resources/Images/Pokamans/WatachuNameLabel.png")
firachu_name = image.load("Resources/Images/Pokamans/FirachuNameLabel.png")


#Creating Rectangles to be used as buttons

#Opening Screen Buttons
buttons = image.load("Resources/Images/Misc/HomeScreenPlayButton.png")                                      #a transparent image with a set size
new_game_button = buttons.get_rect(center = (398, 363))                                                     #define a rectangle that is the size of the 'buttons' image at the specified coordinate


#New Game Choice Screen Buttons
newgamechoicebutton = image.load("Resources/Images/Misc/NewGameChoiceButton.png")
gratachu_button = newgamechoicebutton.get_rect(center = (130, 145))
watachu_button = newgamechoicebutton.get_rect(center = (400, 145))
firachu_button = newgamechoicebutton.get_rect(center = (665, 145))


#Battle Screen Buttons for Moves
movesbutton = image.load("Resources/Images/Misc/MoveButton.png")                                            #on attack screen on your turn during battle
move1 = movesbutton.get_rect(center = (395, 417))
move2 = movesbutton.get_rect(center = (660, 417))
move3 = movesbutton.get_rect(center = (395, 540))
move4 = movesbutton.get_rect(center = (660, 540))

move_rects = [move1, move2, move3, move4]                                                                   #store all the move rectangles to cut down code later (use for loop to reference each)


#Home Screen/Main Menu Buttons
pink_buttons = image.load("Resources/Images/Misc/HomeScreenPinkButton.png")                                 #Load image to get the size of these buttons
swap_current_pokaman_button = image.load("Resources/Images/Misc/SwapPokamanButton.png")
discard_button_off = image.load("Resources/Images/Misc/DiscardButton.png")
discard_button_on = image.load("Resources/Images/Misc/DiscardButtonOn.png")

battleButton = pink_buttons.get_rect(center = (592, 365))
shopButton = pink_buttons.get_rect(center = (592, 283))

swap1 = swap_current_pokaman_button.get_rect(center = (107, 488))
swap2 = swap_current_pokaman_button.get_rect(center = (235, 488))

discardButton = discard_button_off.get_rect(center = (335, 441))


#Shop Buttons
buy_Button = image.load("Resources/Images/Misc/ShopItemTemplate.png")

buyButton1 = buy_Button.get_rect(center = (135, 225))                                                       #8 buttons each at different coordinates
buyButton2 = buy_Button.get_rect(center = (310, 225))
buyButton3 = buy_Button.get_rect(center = (490, 225))
buyButton4 = buy_Button.get_rect(center = (670, 225))
buyButton5 = buy_Button.get_rect(center = (135, 385))
buyButton6 = buy_Button.get_rect(center = (310, 385))
buyButton7 = buy_Button.get_rect(center = (490, 385))
buyButton8 = buy_Button.get_rect(center = (670, 385))

all_buy_buttons = [buyButton1, buyButton2, buyButton3, buyButton4,                                          #to use as reference later to cut down code. (use for loop instead of multiple ifs)
                    buyButton5, buyButton6, buyButton7, buyButton8]

exitButton = pink_buttons.get_rect(center = (598, 542))                                                     #using pink_buttons because same size


#Loading Buttons for Moves
#Each move has its own image that would be displayed on the Pokaman's moves

bite_button = image.load("Resources/Images/Misc/BiteAttackButton.png")
moldycoal_button = image.load("Resources/Images/Misc/MoldyCoalAttackButton.png")
coldcoal_button = image.load("Resources/Images/Misc/ColdCoalAttackButton.png")
hotcoal_button = image.load("Resources/Images/Misc/HotCoalAttackButton.png")
thunderstrike_button = image.load("Resources/Images/Misc/ThunderStrikeAttackButton.png")


#Loading Images for the Attack Animations for Each Move

    #bite attack
bite_top = image.load("Resources/Images/MovesAnimations/UpperBite.png")
bite_bottom = image.load("Resources/Images/MovesAnimations/LowerBite.png")

    #moldycoal attack
moldy_coal_block = image.load("Resources/Images/MovesAnimations/MoldyCoal.png")

    #coldcoal attack
cold_coal_block = image.load("Resources/Images/MovesAnimations/ColdCoal.png")

    #hotcoal attack
hot_coal_block = image.load("Resources/Images/MovesAnimations/HotCoal.png")

    #thunderstrike attack
thunder_strike_image = image.load("Resources/Images/MovesAnimations/ThunderStrike.png")


#Loading Some Basic Sounds
button_sfx = mixer.Sound("Resources/Audio/ButtonSFX.wav")                                                   #just a 'ding' sound effect for when a button is clicked
button_sfx.set_volume(0.5)


#Getting rectangles for Move Animations
#Need the images to move and so a rectangle is created to move accordingly
#and then the image will be blitted onto the adjusted position rectangle

    #bite attack
bite_top_rect = bite_top.get_rect(center = (180, 60))
bite_bottom_rect = bite_bottom.get_rect(center = (180, 190))

e_bite_top_rect = bite_top.get_rect(center = (620, 233))
e_bite_bottom_rect = bite_bottom.get_rect(center = (620, 363))

    #coal attacks
moldy_coal_rect = moldy_coal_block.get_rect(center = (547, 302))
cold_coal_rect = cold_coal_block.get_rect(center = (547, 302))
hot_coal_rect = hot_coal_block.get_rect(center = (547, 302))

e_moldy_coal_rect = moldy_coal_block.get_rect(center = (255, 120))                                          #enemy version of the rect. Individual variable for ease of animation and placing
e_cold_coal_rect = cold_coal_block.get_rect(center = (255, 120))
e_hot_coal_rect = hot_coal_block.get_rect(center = (255, 120))

    #thunder strike attack
thunder_strike_rect = thunder_strike_image.get_rect(center = (189, -91))
e_thunder_strike_rect = thunder_strike_image.get_rect(center = (622, 125))


#GETTING RECTANGLES FOR BATTLE SCREEN
#Sprite Images
sprite_size = image.load("Resources/Images/Misc/SpriteSize.png")

ally_sprite = sprite_size.get_rect(center = (625, 290))
enemy_sprite = sprite_size.get_rect(center = (180, 115))

#SET SCREEN SIZE

size = (width, height) = main_bg.get_size()                                                                 #Set the screen size to the size of the image 'main_bg'
screen = display.set_mode(size)                                                                             #open up the screen

#BUTTON CONDITIONS

openingmenubuttons_enabled = True                                                                           #enabler variable to disable and enable buttons (rectangles) for the main screen (opening)
new_game_choice_made = False                                                                                #like openingmenubuttons_enabled but for newgame screen



 # # # # # # # # # # # # # # # #
#   PRIMARY GAMEPLAY VARIABLES   #
 # # # # # # # # # # # # # # # #

"""
These are basically the main global variables that will be used throughout the game.
Referenced very frequently or just easier to access as a global.
"""

my_pokaman = []                                                                                             #stores all the Pokaman the player has on their team
current_ally = []                                                                                           #during battle sequence this is the current pokaman battling or just the pokaman that will be sent to battle
current_enemy = []                                                                                          #during battle sequence this is the current enemy pokaman
                                                                                                            #current_ally and current_enemy variables used to store temporary Pokaman data (during battle)
turn_complete = False                                                                                       #variable to be used to initiate enemy turn and to disable user buttons temporarily after player turn complete
win_loss_record = [0, 0]                                                                                    #to keep track of the player's win and losses (try to aim for best possible) Format: [wins, losses]
total_money = 60                                                                                            #to keep track of the player's money


 # # # # # # # # # # # # # # # # # # # #
#   POKAMAN AND MOVE/ATTACKS DATABASE   #
 # # # # # # # # # # # # # # # # # # # #

"""
This area will be used to store functions for the animations and damage calculations
of all avaliable attacks/moves in the game. This area will also store the data of
each move aside from animation (e.g. attack power, accuracy) of each move as well
as the basic data (template) of every Pokaman/Monster in the game. They may call
upon other functions later in the code that involve calculations and drawing.
"""


#   ATTACKS/MOVES FUNCTIONS     #

#The following parameter description is a general description for all the attack/
#moves functions

#Parameters: pokaman refers to the pokaman using the attack (ally or enemy);
#            defender is the pokaman being hit by the attack used to calculate damage

def bite(pokaman, defender):
    global myClock                                                                                          #use the global variables of these
    global bite_top_rect
    global bite_bottom_rect
    global e_bite_top_rect
    global e_bite_bottom_rect

    #Parameters: Refer to either the enemy or ally's rectangle (recall the image loading and rectangle for animations of moves
    #            Used because depending on who uses the attack, different positions of animation

    def animation(bite_top_rects, bite_bottom_rects):
        for i in range(10):                                                                                 #Do the following 10 times: Move the rectangles accordingly
            bite_top_rects = bite_top_rects.move(0, 5)
            bite_bottom_rects = bite_bottom_rects.move(0, -5)

            draw_battle()                                                                                   #draw_battle() called to redraw most of the stuff on the battle screen (basically updates/clears the screen)

            screen.blit(bite_top, bite_top_rects)                                                           #blit the bite_top image to its corresponding rectangle
            screen.blit(bite_bottom, bite_bottom_rects)
            display.flip()                                                                                  #update the screen (everything drawn or editted on it)
            myClock.tick(30)                                                                                #set a constant 30 FPS frame rate
        bite_top_rects = bite_top_rects.move(0, -50)                                                        #revert animation rectangles back to original position
        bite_bottom_rects = bite_bottom_rects.move(0, 50)

    #Following if statements are used to test whether the ally or enemy used the attack

    if pokaman == current_ally:
        animation(bite_top_rect, bite_bottom_rect)
        time.wait(100)

    if pokaman == current_enemy:
        animation(e_bite_top_rect, e_bite_bottom_rect)
        time.wait(100)

    draw_battle()                                                                                           #cover the battle_screen without the animation

    final_damage = calculate_damage(bite_attack, pokaman, defender)                                         #calculate the final damage done by the attack (refer to calculate_damage function in code)
    return final_damage                                                                                     #return the final damage done (to be assigned to take HP away in the battle from the defending Pokaman)


#Parameters: Coal refers to which coal image to use (i.e. moldy_coal, cold_coal, hot_coal)
#            coal_rect refers to which rectangle to move
#            ally is just a reference to whether or not the ally is using the move (True or False)
#            to see which direction the coal comes from

def coalAttackAnimation(coal, coal_rect, ally):
    for i in range(39):
        if ally == True:                                                                                    #if it is the ally using the move than move the coal this way
            coal_rect = coal_rect.move(-9, -5)
        elif ally == False:                                                                                 #otherwise this way
            coal_rect = coal_rect.move(9, 5)

        draw_battle()                                                                                       #update battle screen (redraw it)

        screen.blit(coal, coal_rect)
        display.flip()
        myClock.tick(40)

    if ally == True:                                                                                        #revert the coal back to its original position (dependent on whether used by ally or enemy)
        coal_rect = coal_rect.move(351, 195)                                                                #move the rectangle the same distance in reverse
    elif ally == False:
        coal_rect = coal_rect.move(-351, -195)



def moldycoal(pokaman, defender):
    global myClock
    global moldy_coal_rect
    global e_moldy_coal_rect

    if pokaman == current_ally:
        coalAttackAnimation(moldy_coal_block, moldy_coal_rect, True)                                        #call the coal attack animation function with the following parameters
    if pokaman == current_enemy:
        coalAttackAnimation(moldy_coal_block, e_moldy_coal_rect, False)

    draw_battle()

    final_damage = calculate_damage(moldycoal_attack, pokaman, defender)
    return final_damage



def coldcoal(pokaman, defender):
    global myClock
    global cold_coal_rect
    global e_cold_coal_rect

    if pokaman == current_ally:
        coalAttackAnimation(cold_coal_block, cold_coal_rect, True)
    if pokaman == current_enemy:
        coalAttackAnimation(cold_coal_block, e_cold_coal_rect, False)

    draw_battle()

    final_damage = calculate_damage(coldcoal_attack, pokaman, defender)
    return final_damage



def hotcoal(pokaman, defender):
    global myClock
    global hot_coal_rect
    global e_hot_coal_rect

    if pokaman == current_ally:
        coalAttackAnimation(hot_coal_block, hot_coal_rect, True)
    if pokaman == current_enemy:
        coalAttackAnimation(hot_coal_block, e_hot_coal_rect, False)

    draw_battle()

    final_damage = calculate_damage(hotcoal_attack, pokaman, defender)
    return final_damage



def thunderstrike(pokaman, defender):
    global myClock
    global thunder_strike_rect
    global e_thunder_strike_rect

    def animation(rect_to_move):     #refer to enemy or ally thunder strike rect
        for i in range(25):
            rect_to_move = rect_to_move.move(0, 7)

            draw_battle()
            screen.blit(thunder_strike_image, rect_to_move)
            display.flip()
            myClock.tick(20)
        rect_to_move = rect_to_move.move(0, -175)                                                           #revert the animation rectangle back to original position

    if pokaman == current_ally:
        animation(thunder_strike_rect)                                                                      #call this attack's animation function with the ally's thunder_strike_rect
        time.wait(100)                                                                                      #different rectangles for either ally or enemy (different positions)

    if pokaman == current_enemy:
        animation(e_thunder_strike_rect)
        time.wait(100)

    draw_battle()

    final_damage = calculate_damage(thunderstrike_attack, pokaman, defender)
    return final_damage



#       LISTS/ARRAYS USED TO STORE DATA OF EACH ATTACK IN THE GAME      #

#Template: attack_variable_name = [button image, attack type, attack power, animation/damage function, accuracy rate, attack name]
#Note: Attack power is the multiplier for the damage and accuracy rate is a value out of 100 (so a percentage)

bite_attack = [bite_button, 'Normal', 0.60, bite, 85, "Bite"]
moldycoal_attack = [moldycoal_button, 'Grass', 0.50, moldycoal, 75, "Moldy Coal"]
coldcoal_attack = [coldcoal_button, 'Water', 0.50, coldcoal, 75, "Cold Coal"]
hotcoal_attack = [hotcoal_button, 'Fire', 0.50, hotcoal, 75, "Hot Coal"]
thunderstrike_attack = [thunderstrike_button, 'Electric', 0.80, thunderstrike, 60, "Thunder Strike"]


#       LISTS/ARRAYS USED TO STORE DATA OF EACH POKAMAN IN THE GAME     #

#Note: Stores the basic stats and data; the template of the Pokaman
#       Also 'BLANK' in the template below is just a filler spot currently.
#       Something was removed from there so just left it there.

#Template: pokaman_variable_name = [ally sprite's image, level, type, maximum HP,
#                                   current HP, attack power, LIST OF ATTACKS/MOVES,
#                                   image of name, BLANK, pokaman's name,
#                                   EXP needed to level, current EXP, enemy sprite's image,
#                                   rate of growth (leveling), cost (in shop)]
#                                   Note: pokaman's name is just used for messages

gratachu = [gratachu_ally, 3, 'Grass', 12, 12, 50, [bite_attack, moldycoal_attack], gratachu_name, [], "Gratachu", 0, 0, gratachu_enemy, 0.60, 60]
watachu = [watachu_ally, 3, 'Water', 12, 12, 50, [bite_attack, coldcoal_attack], watachu_name, [], "Watachu", 0, 0, watachu_enemy, 0.60, 60]
firachu = [firachu_ally, 3, 'Fire', 12, 12, 50, [bite_attack, hotcoal_attack], firachu_name, [], "Firachu", 0, 0, firachu_enemy, 0.60, 60]

final_list_pokaman = [gratachu, firachu, watachu]                                                           #final list used to randomize enemy pokemon. Also used as reference in shop to cut down code (use for loop instead of ifs)


 # # # # # # # #
#   FUNCTIONS   #
 # # # # # # # #

#   MOUSE INPUT FUNCTIONS   #

"""
These functions are very general and are used throughout the entire program.
They are not very specific to this program but prove an important role in it.
Mainly just detects positions and inputs from the mouse as well as interactions
with any buttons created (rectangles that are used as buttons)
"""

#Function to receive input from mouse (coordinates and button)
def click_mouse():
    (mx, my) = mouse.get_pos()                                                                              #assign the tuple of (mx, my) to the x and y coordinate of the mouse
    mb = mouse.get_pressed()[0]                                                                             #assign the mb (mouse button) to the button that is pressed on the mouse
    return(mx, my, mb)                                                                                      #return all the input recorded of the mouse

#Function to test if the mouse is left clicked at the coordinates of the specified button (rectangle)
#Parameters: button refers to which button (or rectangle used as a button)

def button_pressed(button):
    (mx, my, mb) = click_mouse()
    if button.collidepoint(mx, my) and mb == 1:                                                             #if the mouse coordinates inputted collide with the rectangle and is left-clicked
        button_sfx.play()                                                                                   #play this sound effect
        return True                                                                                         #return True value

#Function to test whether or not the screen is clicked
#generally used to stall on the screen until the user wants to proceed to next screen
def click_screen():
    global running
    for evnt in event.get():                                                                                #for all the events in the event queue
        if evnt.type == QUIT:                                                                               #if the X button is pressed at the top right of the window then set running to False
            running = False                                                                                 #running variable controls the mainloop (the game runs while this variable is True)
        if evnt.type == MOUSEBUTTONDOWN:                                                                    #if the mouse button is clicked then return True
            return True


#   FUNCTIONS FOR BATTLE    #

"""
These functions are used to process the doings of the battle screen. They include drawing functions,
calculations, user interactions, a general loop, and also any set-up for each individual battle
"""

#   FUNCTIONS PRIMARILY TO SET UP BATTLES     #

#FUNCTION TO ASSIGN NEW MOVES (OR TEST FOR)
#Function assigns new moves to Pokaman accordingly, tests for all pokaman in the database
#Parameters: Pokaman refers to which pokaman is being tested to learn new moves
#            #in_battle is just a True of False condition to test whether or not this is being tested in battle or not

def move_assignment(pokaman, in_battle):

    #Function to actually assign moves accordingly based on level to the pokaman
    #Parameters: leveled_pokaman refers to which pokaman is being tested to learn a new move
    #            test_pokaman refers to what template pokaman is being referenced (e.g. if "Gratachu" then only test for Gratachu's moves)
    #            levels refer to what level they learn the corresponding move (correspondence refers to the index of the next parameter (moves)) (LIST)
    #            moves refer to which moves to learn (LIST)

    def move_learning(leveled_pokaman, test_pokaman, levels, moves):
        if in_battle == True:                                                                               #if this is being called in_battle then
            if leveled_pokaman[9] == test_pokaman:                                                          #checking if name of the pokaman being tested to learn new moves is the same as the template pokaman
                for i in range(len(levels)):                                                                #run the loop for as many times as there are new moves to learn (levels and moves list lengths are equal)
                    if len(leveled_pokaman[6]) < 4 and leveled_pokaman[1] == levels[i]:                     #if the Pokaman has less than four moves already (NOTE: There is a four move limit for each Pokaman)
                                                                                                            #and the level of the Pokaman is the same as the first level specified in the levels list
                        learned_move_msg = msgfont.render(str(leveled_pokaman[9]) +                         #render a new message (e.g. "Gratachu learned Thunder Strike!")
                         " learned " + moves[i][5] + "!", 1, black)
                        draw_battle_msg(learned_move_msg)                                                   #call draw_battle_msg with the specified message loaded (function defined later in code)
                        leveled_pokaman[6].append(moves[i])                                                 #after all this, add the corresponding move to the level specified to the pokaman's arsenal

                    elif len(leveled_pokaman[6]) >= 4 and leveled_pokaman[1] == levels[i]:                  #if the pokaman has more than 3 moves already and the pokaman is at the corresponding level for th move then
                        full_moves_msg = msgfont.render(str(leveled_pokaman[9]) +                           #render new message (IDEA: change this area in the future here to add a function to forget and replace moves)
                         " already has 4 moves.", 1, black)
                        draw_battle_msg(full_moves_msg)

        elif in_battle == False:                                                                            #If this is called outside of battle do the following instead
                                                                                                            #Same as when in battle except checks if the pokaman is over or equal to the level required to learn the move instead of
                                                                                                            #being at the level
            if leveled_pokaman[9] == test_pokaman:                                                          #checking if names of the leveled_pokaman and test_pokaman are the same
                for i in range(len(levels)):
                    if len(leveled_pokaman[6]) < 4 and leveled_pokaman[1] >= levels[i]:                     #if the enemy is greater level than the level still append the move
                        leveled_pokaman[6].append(moves[i])


    #Move Learning Database for Each Pokaman in the Game

    move_learning(pokaman, "Gratachu", [4], [thunderstrike_attack])                                         #Call the move_learning function for each pokaman in the game (for the pokaman being tested for new moves)
    move_learning(pokaman, "Watachu", [4], [thunderstrike_attack])
    move_learning(pokaman, "Firachu", [4], [thunderstrike_attack])


#   FUNCTION TO RANDOMIZE THE ENEMY     #

def randomize_enemy():

    team_total_level = 0                                                                                    #variable used to get the player's team total level to use as a factor to randomize the enemy level

    for i in range(len(my_pokaman)):                                                                        #add up all the levels of pokaman in your team
        team_total_level += my_pokaman[i][1]

    team_avg_level = round(team_total_level/len(my_pokaman))                                                #find the average level of all the pokaman in player's team

    if team_avg_level >= 3:                                                                                 #set this condition otherwise enemy level might be negative (if the team_avg_level is greater or equal to 3)
        randomized_enemy_level = randint(team_avg_level - 1, team_avg_level + 1)                            #set randomized enemy level variable to a random integer 1 levels to 1 levels higher than your average level for your team
    else:
        randomized_enemy_level = randint(1, 2)                                                              #otherwise set random_enemy_level to a random number between 1 or 2 (this is generally for the beginning of the game)

    pokaman_value = randint(0, len(final_list_pokaman) - 1)                                                 #generate a random value that will be used as an index from the complete list of pokaman in the database

    enemy = list(final_list_pokaman[pokaman_value])                                                         #randomizes which pokaman to face (use the index previously randomized). Use list command to create a new list, not change the old template of pokaman
    enemy[6] = list(final_list_pokaman[pokaman_value][6])                                                   #copy the list of moves for the enemy so it does not affect the template of pokaman (make this list independent of the template in the database)
    enemy[1] = randomized_enemy_level                                                                       #set the enemy's level to the randomized level earlier


    #Increasing Enemy Stats according to the enemy's level

    for i in range(enemy[1] - 1):                                                                           #Do this for every level above 1
        for i in range(3):                                                                                  #randomize stat_decider to be 1 or 2 (i.e. increase attack power or max HP)
            stat_decider = randint(1, 2)
            if stat_decider == 1:
                enemy[5] += randint(1, 2)                                                                   #increase the stats by either 1 or 2
            elif stat_decider == 2:
                enemy[3] += randint(1, 2)

    enemy[4] = enemy[3]                                                                                     #set current HP to max HP of enemy (i.e. heal the pokaman)


    #Move Learning for each Pokaman is different
    #set any new moves that the enemy pokaman will learn based off their level

    move_assignment(enemy, False)                                                                           #call move_assignment function from earlier (outside of battle)
    return enemy                                                                                            #return the randomized enemy



#   PRIMARY CALCULATION FUNCTIONS   #

"""
These functions are generally functions to calculate things behind the scenes.
This includes damage, EXP, money, hit rates. Mainly number crunching and taking
in several factors to calculate these things.
"""

#   FUNCTION TO CALCULATE DAMAGE BASED ON A VARIETY OF FACTORS  #

#Parameters: move refers to which attack is being used (take the type and power of move)
#            #attacking_pokaman refers to which pokaman is using the move (take attack power of pokaman)
#            #defending pokaman refers to which pokaman is being attacked (take type of pokaman)

def calculate_damage(move, attacking_pokaman, defending_pokaman):
    damage = 0

    #Function to test for move effectiveness
    #Parameters: move_type refers to the type of the move
    #            not_effective refers to which type would the move not be very effective against
    #            same as above but for super effective

    def effective_test(move_type, not_effective, super_effective):
        nonlocal damage                                                                                     #use the damage variable outside this effective_test function scope (outer scope)
        if move[1] == move_type and defending_pokaman[2] == not_effective:                                  #if the move used's type is the specified move type and the defending_pokaman's type is the same as not_effective then
            damage *= 0.5                                                                                   #halve the damage output
            draw_battle_msg(noteffective_msg)                                                               #draw not effective message

        elif move[1] == move_type and defending_pokaman[2] == super_effective:                              #if the move used's type is the specified type and the defending_pokaman's type is the same as super_effective then
            damage *= 2                                                                                     #double damage output
            draw_battle_msg(supereffective_msg)                                                             #draw super effective message
        return damage                                                                                       #return the new damage calculated after considering type effectiveness


    #NOTE: move[2] is atk power of the move, attacking_pokaman[5] is atk power of the pokaman

    damage = uniform(attacking_pokaman[5] * 0.5, attacking_pokaman[5] * 1.5)                                #randomize damage based off the pokaman's attacking power (NOTE: uniform is basically randint but takes float values)
    damage *= move[2]                                                                                       #each move has a different atk power percentage. (i.e. calculates what percentage of your pokaman's raw power it does)

    #Test effectiveness for all the move types

    damage = effective_test('Grass', 'Fire', 'Water')
    damage = effective_test('Water', 'Grass', 'Fire')
    damage = effective_test('Fire', 'Water', 'Grass')
    damage = effective_test('Electric', 'NoneAtMoment', 'Water')

    damage = round(damage)                                                                                  #round damage to a whole number
    return damage                                                                                           #return the final calculated damage after considering all factors



#   FUNCTION TO CALCULATE AND DETERMINE HOW MUCH EXP OBTAINED AFTER BATTLE  #

#NOTE: Based on enemy level

#Parameters: enemy_pokaman refers to who is the enemy pokaman
#            ally_pokaman for who is the ally
#            i.e. current_enemy, current_ally

def calculate_exp(enemy_pokaman, ally_pokaman):
    base_exp = enemy_pokaman[1] * 30                                                                        #base exp is the enemy defeeated level times 30     (30 for the presentation because time is limited (WILL CHANGE))
    final_exp = randint(round(base_exp * 0.8), round(base_exp * 1.5)) * ally_pokaman[13]                    #randomizes the exp. dependent on the base_exp then multiplies it by the pokaman's rate of growth

    return round(final_exp)                                                                                 #return rounded value of the final EXP calculated



#   FUNCTION TO CALCULATE AND DETERMINE HOW MUCH MONEY OBTAINED AFTER BATTLE    #

#Parameters: enemy_pokaman refers to who is the enemy (to get its level)
#            i.e. current_enemy

def calculate_money(enemy_pokaman):
    base_money = enemy_pokaman[1] * 10                                                                      #money is the enemy's level multiplied by 10
    final_money =  randint(round(base_money * 0.5), round(base_money * 1.5))                                #randomize the money based off the base value calculated

    return final_money



#   FUNCTION TO TEST FOR MISSES BASED OFF THE MOVE'S ACCURACY   #

#Parameters: move refers to which move is being used (to take the accuracy value)

def attack_hit(move):
    hit_range = []                                                                                          #will be used to store numbers from 1- 100 depending on the accuracy
    for i in range(1, move[4] + 1):                                                                         #add the values from 1 to 100 until the accuracy value is reached
        hit_range.append(i)

    if randint(1,100) in hit_range:                                                                         #randomize a value from 1 and 100, if its in the hit_range than return True
        return True                                                                                         #i.e. the attack lands)



#   FUNCTIONS FOR DRAWING BATTLE ASPECTS    #

"""
These functions are generally used to draw the aspects of the battle including:
Messages, HP, EXP, updating animation. Some other functions may also be defined
within one of these functions however for convenience.
"""

#FUNCTION TO DRAW THE BATTLE MESSAGES THAT COME UP ON SCREEN

#Parameters: message refers to which message to draw (the text)

def draw_battle_msg(message):
    screen.blit(screen_msg_box, (9, 359))                                                                   #draw the blank message box on the screen
    screen.blit(message, (60, 398))                                                                         #draw the specified message on the message box
    display.flip()

    while True:                                                                                             #run an infinite loop so the program is stalled until the user clicks the screen
        if click_screen() == True:                                                                          #continue the process after clicking the screen (called function)
            draw_battle()                                                                                   #draw battle screen without messages
            break                                                                                           #break out of infinite loop when screen is clicked


#   FUNCTION TO DRAW AND CALCULATE LENGTH OF HP BARS    #

#Parameters: enemy_or_ally just refers to whether it is drawing the HP for the enemy or ally
#            input current_ally or current_enemy for this parameter

def draw_HP(enemy_or_ally):
    global current_ally
    global current_enemy

    if enemy_or_ally == current_ally:                                                                       #to draw HP for ally
        bar_length = (current_ally[4] / current_ally[3]) * 100                                              #the length of the bar representing the percentage of HP to max HP
        if bar_length <= 0:                                                                                 #if the pokaman has less than 0 HP then just draw it so its like 0 HP (prevents an excessively long bar from being drawn)
            draw.line(battle_screen_bg, white, (308, 289), (208, 289), 8)                                   #draw a line from the specified coordinates to the other with a width of 8
        else:
            draw.line(battle_screen_bg, white, (308, 289), (308 - (100 - bar_length), 289), 8)              #draw a white line covering 100 - bar length (the HP lost)

    elif enemy_or_ally == current_enemy:                                                                    #do the same as above but with the enemy's HP bar and their percentage of HP to max
        e_bar_length = (current_enemy[4] / current_enemy[3]) * 100
        if e_bar_length <= 0:
            draw.line(battle_screen_bg, white, (735, 90), (635, 90), 8)
        else:
            draw.line(battle_screen_bg, white, (735, 90), (735 - (100 - e_bar_length), 90), 8)



#   FUNCTION TO DRAW AND CALCULATE LENGTH OF EXP BARS   #

#Parameters: pokaman refers to which pokaman is the EXP being drawn for

def draw_EXP(pokaman):
    global myClock

    #   FUNCTION TO PERFORM ACTIONS FOR LEVEL UP    #

    #Parameter same as the outerscope function

    def level_up(pokaman):                                                                                  #3 is max hp 5 is atk power
        pokaman[11] -= pokaman[10]                                                                          #set the current exp of the pokaman to the remainder after the level up
        pokaman[1] += 1                                                                                     # increase pokaman's level by 1

        #increase stats of the pokaman that leveled up

        for i in range(3):                                                                                  #run this 3 times. Therefore 3 sets of stat point increases
            stat_decider = randint(1, 2)                                                                    #randomize the stat_decider to increase either atk or max hp
            if stat_decider == 1:                                                                           #increase atk power
                pokaman[5] += randint(1, 2)                                                                 #increase current pokaman's attack power by 1 or 2 points, randomized
            elif stat_decider == 2:
                pokaman[3] += randint(1, 2)                                                                 #increase pokaman's max HP by 1 or 2 points

        move_assignment(pokaman, True)                                                                      #test for any new moves that can be learned by the pokaman that leveled up by calling this function


    for i in range(10):                                                                                     #run this 10 times. 10 has no special meaning just an adequate number of times so that the pokaman wont level over in one battle
                                                                                                            #(does not rly slow down program as it will not much if doesnt level up)
        #Calculating the EXP required to level

        pokaman[10] = pokaman[1] * 10                                                                       #reference to pokaman's level. required exp to level is the pokaman's level times 10

        #bar length values change each time loop is run, so it updates the
        #amount of EXP required to level for individual levels

        current_bar_length = (pokaman[11] / pokaman[10]) * 200                                              #length of bar represents percentage of current exp to EXP required to level. *200 because 100% of the bar is 200 pixels wide
        total_current_bar_length = current_bar_length                                                       #for storing current bar length ( length left to draw)

        if (pokaman[11]/pokaman[10]) >= 1:                                                                  #if the percentage of the pokaman's current EXP to required EXP is greater or equal to one then do the following

            level_up_msg = msgfont.render(current_ally[9] + " has leveled up to " +                         #render a level up message
                                          str(current_ally[1] + 1) + "!", 1, black)                                                      #reference to current_ally's level
            current_bar_length = 200                                                                        #set the current_bar_length to 200 (FULL BAR)

            for i in range(50):                                                                             #for loop to animate the EXP bar increase
                draw.line(battle_screen_bg, yellow, (106, 331), ((106 + i * 4), 331), 6)
                draw_battle()
                myClock.tick(30)

            draw_battle_msg(level_up_msg)                                                                   #draw the level up message after the EXP bar animation is done

            level_up(pokaman)                                                                               #apply level_up function to the pokaman

            draw.line(battle_screen_bg, black, (106, 331), (306, 331), 6)

            total_current_bar_length -= 200

    draw.line(battle_screen_bg, black, (106, 331), (306, 331), 6)                                           #clean off the EXP bar area

    #for loop again to animate the EXP bar increase
    #(just draw what is left or any EXP bar that did not go past 100%)

    for i in range(round(total_current_bar_length/4)):
        draw.line(battle_screen_bg, yellow, (106, 331), ((106 + i * 4), 331), 6)
        draw_battle()
        myClock.tick(30)


#   FUNCTION TO SET/DRAW THE BASIC BATTLE SCREEN, I.E IMAGES AND BACKGROUND     #

def draw_battle():
    global current_ally
    HP_text = str(current_ally[4]) + " / " + str(current_ally[3])                                           #converts the HP and Max HP values of current ally to a string in order to combine into one for blitting as text
    HP_label = myfont.render(HP_text, 1, black)                                                             #render text of current_ally's current HP out of max
    lvl_label = myfont.render(str(current_ally[1]), 1, black)                                               #label for the current level of current_ally
    e_lvl_label = myfont.render(str(current_enemy[1]), 1, black)

    screen.blit(battle_screen_bg, screen_rect)
    screen.blit(current_ally[0], ally_sprite)                                                               #blit the image of the first pokaman in your team to the ally_sprite rectangle
    screen.blit(current_ally[7], (75, 250))                                                                 #blit image of the current pokaman's name on screen
    screen.blit(current_enemy[12], enemy_sprite)                                                            #blit the image of the randomized enemy to the enemy_sprite rectangle
    screen.blit(current_enemy[7], (497, 45))
    screen.blit(HP_label, (246, 300))                                                                       #provides a number basis of the player's current pokaman's HP
    screen.blit(lvl_label, (273, 246))                                                                      #blits the level (label) of ally pokaman
    screen.blit(e_lvl_label, (693, 45))

    #This is just to act as a back-up check to prevent crashing in the program
    #If the number of moves for the current_ally is over 4 for some reason than
    #keep deleting the moves until there are only 4

    if len(current_ally[6]) > 4:
        for i in range(len(current_ally[6])):
            if len(current_ally[6]) <= 4:
                break
            else:
                del current_ally[6][len(current_ally[6]) - 1 - i]


    #for setting the attack options buttons

    for i in range(len(current_ally[6])):                                                                   #length of the number of moves the current pokaman has
        screen.blit(current_ally[6][i][0], move_rects[i])                                                   #blit the image of the ith moves of the current_ally to the ith rectangle

    display.flip()



#   FUNCTIONS THAT CONTROL THE FLOW OF BATTLE  #
"""
These functions are basically the main loops (or parts of the main loop) that
control the battle sequence. They control what occurs and the user inputs at
each turn (enemy and ally).
"""

#FUNCTION FOR ENEMY TURNS (Automated)

def enemy_turn():

    draw_battle()

    move_used = randint(0, (len(current_enemy[6]) - 1))                                                     #reference the move pool of the current_enemy theen randomize an index of that move pool to randomize a move to use

    #render screen msg font that require the current_enemy and move used

    enemy_move_msg = msgfont.render("The opposing " + current_enemy[9] + " used " +
                                    current_enemy[6][move_used][5] + ".", 1, black)                         #reference to name of current_enemy and the name of move used (move_used variable) determines which move is used

    draw_battle_msg(enemy_move_msg)                                                                         #display the message for what move the enemy uses and wait for screen click

    if attack_hit(current_enemy[6][move_used]) == True:                                                     #call the attack_hit function and test for the accuracy of the move used by the enemy; if true then do the following
        damage_taken = current_enemy[6][move_used][3](current_enemy, current_ally)                          #damage_taken is the damage YOU will take. move_used references the move pool of the current_enemy then randomize an index
                                                                                                            #of that move pool to randomize a move to use
        current_ally[4] -= damage_taken                                                                     #Subtract HP from the current_ally (subtract the damage taken)
        if current_ally[4] < 0:                                                                             #if current_ally HP goes below 0 then just set to 0
            current_ally[4] = 0                                                                             #to once again prevent excessive HP bar drawing
        draw_HP(current_ally)                                                                               #call draw_HP function for current_ally (draw its HP)

        draw_battle()                                                                                       #update battle screen

    else:
        draw_battle_msg(attack_missed_msg)                                                                  #draw attack missed message
        draw_HP(current_ally)                                                                               #Update Screen HP Bars and such
        draw_HP(current_enemy)
        draw_battle()



#   FUNCTION FOR PLAYER TURN (CHOICE)   #

def ally_turn():
    global running
    global turn_complete
    global enemy_sprite
    global ally_sprite
    global current_enemy
    global current_ally
    global total_money

    damage_dealt = 0                                                                                        #set local variable damage_dealt to 0 (define the variable)

    #LOOP used to receive user input

    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
            if turn_complete == False:                                                                      #if turn_complete is False (it is the player's turn)
                for i in range(len(current_ally[6])):                                                       #for i in range of number of moves the current_ally has    SO only have the move buttons that actually have moves
                    if button_pressed(move_rects[i]) == True:

                        #render screen msg fonts that require the current ally and move used
                        ally_move_msg = msgfont.render(current_ally[9] + " used " +
                                                        current_ally[6][i][5] + ".", 1, black)              #reference to name of the current_ally and the name of the move used (i) determines which move is used

                        draw_battle_msg(ally_move_msg)                                                      #draw and detect clicks for the named move message

                        if attack_hit(current_ally[6][i]) == True:                                          #test the accuracy or if the move selected miss or hits
                            damage_dealt = current_ally[6][i][3](current_ally, current_enemy)               #use the function of the move that is in that box and assign the return value to damage_dealt
                            current_enemy[4] -= damage_dealt                                                #current_enemy's HP data storage index value gets subtracted from the damage_dealt
                        else:
                            draw_battle_msg(attack_missed_msg)                                              #display attack missed message

                        turn_complete = True                                                                #set turn_complete to True (end player's turn)
                        draw_HP(current_enemy)


        #WHEN THE ENEMY LOSES ALL HP

        if current_enemy[4] <= 0:                                                                           #test if enemy HP is less than 0 or equal (i.e. dead)
            win_loss_record[0] += 1                                                                         #add a win
            draw_HP(current_ally)                                                                           #Update Screen HP Bars and such
            draw_HP(current_enemy)
            draw_battle()

            enemy_faint_msg = msgfont.render("The opposing " + current_enemy[9] +
                                            " has fainted.", 1, black)                                      #current_enemy[9] refers to enemy name
            draw_battle_msg(enemy_faint_msg)

            for i in range(30):                                                                             #animate pokaman fainting (flies off screen)
                enemy_sprite = enemy_sprite.move(-10, 0)                                                    #move the sprites
                draw_battle()
                screen.blit(current_enemy[12], enemy_sprite)
                display.flip()
                myClock.tick(20)


            #EXP GAIN CODE

            exp_gain = calculate_exp(current_enemy, current_ally)                                           #call calculate_exp function with the specified parameters

            current_ally[11] += exp_gain                                                                    #adds the calculated exp to the current_ally's exp
                                                                                                            #reference to the current_ally's current exp

            exp_gain_msg = msgfont.render(current_ally[9] + " gained " +
                                          str(exp_gain) + " EXP.", 1, black)
            draw_battle_msg(exp_gain_msg)                                                                   #draws exp gain message on screen and waits for user click input
            draw_EXP(current_ally)                                                                          #call draw_EXP function for current_ally


            money_gain = calculate_money(current_enemy)                                                     #call calculate_money function using the current_enemy as a parameter

            total_money += money_gain                                                                       #add the money gained to the global variable total_money (player's money)

            money_gain_msg = msgfont.render("You gained " + str(money_gain) + " Gratoney", 1, black)
            draw_battle_msg(money_gain_msg)

            break                                                                                           #break out of the battle loop (ally_turn) loop

        #the condition for the enemy's turn to begin

        if turn_complete == True and running == True:                                                       #if the player's turn is complete and the game is running
            enemy_turn()                                                                                    #call enemy_turn function to initiate enemy turn
            if current_ally[4] <= 0:                                                                        #test after enemy turn if your pokaman HP is lower or equal to 0 (i.e. dead)
                ally_faint_msg = msgfont.render(current_ally[9] + " has fainted.", 1, black)
                draw_battle_msg(ally_faint_msg)
                draw_battle()

                for i in range(30):                                                                         #animate pokaman fainting (flies off screen)
                    ally_sprite = ally_sprite.move(10, 0)
                    draw_battle()
                    screen.blit(current_ally[0], ally_sprite)
                    display.flip()
                    myClock.tick(20)

                win_loss_record[1] += 1                                                                     #add a loss
                mixer.music.stop()                                                                          #stop the music running in the background (mixer)
                break                                                                                       #break out of the battle loop
            turn_complete = False


#MAIN BATTLE LOOP (IN THE MAIN LOOP)

def main_battle():
    global running                                                                                          #to allow quitting of program
    global current_ally                                                                                     #declare global to use a common variable in the other functions that are called within
    global current_enemy                                                                                    #same as above
    global turn_complete

    mixer.music.load("Resources/Audio/BattleMusic.wav")                                                     #load this music (audio)
    mixer.music.play(-1)                                                                                    #loop this music infinitely

    turn_complete = False                                                                                   #start with player's turn by setting this to False

    current_ally = my_pokaman[0]                                                                            #current_ally is the first pokaman on the team

    current_enemy = randomize_enemy()                                                                       #set the current_enemy to the enemy returned by the randomize_enemy function

    screenSwapAnimation(battle_screen_bg)                                                                   #call screenSwapAnimation function with the specified background to switch to

    draw_battle()
    draw_EXP(current_ally)

    ally_turn()                                                                                             #initate the battle by calling ally_turn

    #sets the first pokaman of your team to current_ally

    my_pokaman[0] = current_ally                                                                            #used to update the details (just in case of level up)  of current_ally to the pokaman on your team



#       FUNCTIONS FOR MAIN MENU         #

"""
These functions are used to control the flow of the opening screens, and the
main menu. They also consist of any misc functions such as the screenSwapAnimation
function which is occasionally used just as a visual. These functions will control
the flow of the screens that are not directly correlated to the battles, although
may have a link to them.
"""

#       MISC FUNCTION       #

#Parameter: background just refers to which background to switch to after the fading effect

def screenSwapAnimation(background):
    global myClock
    for i in range(len(black_shades)):                                                                      #blit the background of the parameter
        screen.blit(background, screen_rect)                                                                #blit the corresponding image (shade of black (transparency)) corresponding to i
        screen.blit(black_shades[i], screen_rect)
        display.flip()
        myClock.tick(20)
    screen.blit(background, screen_rect)                                                                    #blit the specified background to the screen


#   MAIN MENU FUNCTION FOR AFTER THE FIRST BATTLE   #

def main_menu():
    global running
    global ally_sprite
    global enemy_sprite
    global my_pokaman
    global current_ally

    discard_on = False                                                                                      #variable to enable discarding of Pokamans

    #Parameters: discard_on_off refers to a True or False value to decide
    #            whether or not the discard button was clicked on or not

    def update_screen_details(discard_on_off):
        win_loss_text = msgfont.render("Wins: " + str(win_loss_record[0]) +
                                        " Losses: " + str(win_loss_record[1]), 1, black)
        money_text = msgfont.render(str(total_money), 1, black)
        name_text = myfont.render(my_pokaman[0][9], 1, black)                                               #render the name of the first pokaman on the team
        level_text = myfont.render(str(my_pokaman[0][1]), 1, black)                                         #render the level of the first pokaman on the team
        attack_text = myfont.render(str(my_pokaman[0][5]), 1, black)                                        #render the attack of the first pokaman on the team
        maxHP_text = myfont.render(str(my_pokaman[0][3]), 1, black)                                         #render the max HP of the first pokaman on the team
        type_text = myfont.render(my_pokaman[0][2], 1, black)                                               #render the type of the first pokaman on the team

        current_poka_image = transform.scale(my_pokaman[0][12], (77, 118))                                  #scale image of my first pokaman (enemy image) on team to fit the area I want

        screen.blit(home_screen_bg, screen_rect)
        screen.blit(win_loss_text, (435, 184))
        screen.blit(money_text, (488, 536))
        screen.blit(current_poka_image, (77, 186))
        screen.blit(name_text, (288, 192))
        screen.blit(level_text, (288, 215))
        screen.blit(attack_text, (288, 238))
        screen.blit(maxHP_text, (288, 261))
        screen.blit(type_text, (288, 284))

        if discard_on_off == True:                                                                          #test to see if the discard button should be labelled as on or off
            screen.blit(discard_button_on, (312, 417))                                                      #if on then blit this image (different image for discard button being on)


        #Scale the other pokaman on the team to size and then blit them to the screen as well

        for i in range(1, len(my_pokaman)):                                                                 #do this for each other pokaman (besides first)
            scaled_poka_image = transform.scale(my_pokaman[i][12], (79, 120))
            if i == 1:                                                                                      #if it is the first, run through this loop
                screen.blit(scaled_poka_image, (68, 428))
            elif i == 2:                                                                                    #if it is the second, run through this loop
                screen.blit(scaled_poka_image, (196, 428))                                                  #NOTE: Currently a max of 2 loops anyways as there is a cap of 3 pokaman that you can have at once

        display.flip()


    #   FUNCTION TO OPEN SHOP SCREEN AND ALL ITS FUNCTIONS   #

    def shopScreen():
        global running
        global total_money
        page = 1                                                                                            #page as in the page of the shop screen (currently only one page so unused)
        breaker = False                                                                                     #set a breaker variable to exit the screen later

        while running:
            for evnt in event.get():
                if evnt.type == QUIT:
                    running = False
                if len(my_pokaman) < 3:                                                                     #only allow to buy if the player has less than 3 pokaman (which is the max you can have at once)
                    for i in range(len(final_list_pokaman)):
                        if button_pressed(all_buy_buttons[i]) == True and page == 1:                        #page has no use right now as there is only 1 page
                            if total_money >= final_list_pokaman[i][14]:                                    #referring to whether the player has enough money in comparison to the i'th pokaman's (the one displayed) value
                                total_money -= final_list_pokaman[i][14]                                    #subtract the money from your money

                                #updating the shop screen (the money used)
                                money_text = msgfont.render(str(total_money), 1, black)
                                screen.blit(shop_screen_bg, screen_rect)
                                screen.blit(money_text, (100, 526))
                                display.flip()

                                #calculate team's average level to find a range to randomize the bought pokaman's level
                                team_total_level = 0

                                for k in range(len(my_pokaman)):                                            #add up all the levels of pokaman in your team
                                    team_total_level += my_pokaman[k][1]

                                team_avg_level = round(team_total_level/len(my_pokaman))                    #find the average level of all the pokaman in player's team

                                pokaman_to_add = list(final_list_pokaman[i])                                #create a new list of the bought pokaman
                                pokaman_to_add[6] = list(final_list_pokaman[i][6])                          #copy the list of moves of the pokaman to add so it does not affect the template pokaman

                                if team_avg_level >= 6:                                                     #only if the team's average level is over 6
                                    pokaman_to_add[1] = randint(team_avg_level - 5, team_avg_level + 2)     #randomize the level of the pokaman to add in this range of the team's average level

                                #increase new ally stats based on level

                                for i in range(pokaman_to_add[1] - 1):
                                    for i in range(3):
                                        stat_decider = randint(1, 2)
                                        if stat_decider == 1:
                                            pokaman_to_add[5] += randint(1, 2)
                                        elif stat_decider == 2:
                                            pokaman_to_add[3] += randint(1, 2)

                                pokaman_to_add[4] = pokaman_to_add[3]                                       #set current HP to max HP of pokaman to add

                                move_assignment(pokaman_to_add, False)

                                my_pokaman.append(pokaman_to_add)                                           #add the pokaman to your team

                if button_pressed(exitButton)== True:                                                       #if the exit button is pressed set breaker to true and break out of the closest loop
                    breaker = True
                    break

            if breaker == True:                                                                             #break out of the shopscreen loop when the exitButton pressed
                break


    mixer.music.load("Resources/Audio/MainMenuMusic.wav")                                                   #load the main menu
    mixer.music.play(-1)

    update_screen_details(False)                                                                            #call update_screen_details function with the discard button as false (default screen)


    #resetting the locations of these sprite boxes
    ally_sprite.centerx = 625
    ally_sprite.centery = 290
    enemy_sprite.centerx = 180
    enemy_sprite.centery = 115


    #resetting the HP bars of the pokamans
    draw.line(battle_screen_bg, green, (735, 90), (635, 90), 8)         #redraw HP bars on battle screen background
    draw.line(battle_screen_bg, green, (308, 289), (208, 289), 8)

    #to heal all your pokaman on the team
    for i in range(len(my_pokaman)):
        my_pokaman[i][4] = my_pokaman[i][3]

    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
            if button_pressed(battleButton) == True:                                                        #if battle button is pressed than call main battle function (set up everything for it too)
                current_ally = my_pokaman[0]
                main_battle()
                discard_on = False                                                                          #set discarding to False
                main_menu()                                                                                 #after battle is over recall main_menu function to start back from beginning
            if button_pressed(shopButton) == True:                                                          #if shop button pressed than set up the shop and call its function
                money_text = msgfont.render(str(total_money), 1, black)
                screen.blit(shop_screen_bg, screen_rect)
                screen.blit(money_text, (100, 526))
                display.flip()
                shopScreen()
                update_screen_details(False)
                discard_on = False

            #to discard Pokamans
            #to turn on discarding
            if button_pressed(discardButton) == True and discard_on == False:                               #only do this if discard_on condition is currently false
                screen.blit(discard_button_on, (312, 417))
                display.flip()
                discard_on = True                                                                           #set this to True (used as a condition to perform actions)
                time.wait(200)                  #to prevent quick double click
            elif button_pressed(discardButton) == True and discard_on == True:                              #to turn off discarding
                screen.blit(discard_button_off, (312, 417))
                display.flip()
                discard_on = False
                time.wait(200)

            #to change main Pokaman
            if button_pressed(swap1) == True:                                                               #if the first box is pressed than continue
                if discard_on == True and len(my_pokaman) >= 2:                                             #if this button is pressed and discard is too before hand then it will delete the pokaman from the team.
                                                                                                            #Also only do this if you have at least 2 pokaman (to prevent crashing)
                    del my_pokaman[1]                                                                       #remove this pokaman from your team
                    update_screen_details(True)                                                             #update the screen
                elif len(my_pokaman) >= 2:
                    my_pokaman[0], my_pokaman[1] = my_pokaman[1], my_pokaman[0]                             #swap the pokaman that is the current_pokaman
                    update_screen_details(False)
                display.flip()

            if button_pressed(swap2) == True:                                                               #same as above except with the second pokaman in the boxes
                if discard_on == True and len(my_pokaman) >= 3:                                             #only do this if you actually have 3 pokaman (to prevent crashing)
                    del my_pokaman[2]
                    update_screen_details(True)
                elif len(my_pokaman) >= 3:
                    my_pokaman[0], my_pokaman[2] = my_pokaman[2], my_pokaman[0]                             #same as previous swap but with the third pokaman on the team
                    update_screen_details(False)
                display.flip()



#       WELCOME/OPENING SCREENS FUNCTIONS       #

def set_main():
    screen.blit(main_bg, screen_rect)
    display.flip()

def new_game():
    new_game_breaker = False
    global new_game_choice_made
    global running
    screenSwapAnimation(newgame_choicescreen)
    screen.blit(newgame_choicescreen, screen_rect)
    display.flip()

    while new_game_choice_made == False:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                new_game_choice_made = True                                                                 #not actually choice made but set so it can exit the loop
            if new_game_choice_made == False:
                if button_pressed(gratachu_button) == True:
                    new_game_choice_made = True
                    screenSwapAnimation(gratachu_choice_screen)
                    my_pokaman.append(list(gratachu))                                                       #call list() to create a new copy of it instead of potentially referencing the same objects (or other lists) contained in this list
                    my_pokaman[0][6] = list(gratachu[6])                                                    #call list here to create a new copy of the moves list inside the pokaman template list above
                    display.flip()
                if button_pressed(watachu_button) == True:
                    new_game_choice_made = True
                    screenSwapAnimation(watachu_choice_screen)
                    my_pokaman.append(list(watachu))
                    my_pokaman[0][6] = list(watachu[6])
                    display.flip()
                if button_pressed(firachu_button) == True:
                    new_game_choice_made = True
                    screenSwapAnimation(firachu_choice_screen)
                    my_pokaman.append(list(firachu))
                    my_pokaman[0][6] = list(firachu[6])
                    display.flip()

    while running:
        if click_screen() == True:                                                                          #proceed to next part of game when screen is clicked
            main_battle()
            break

def opening_screen():
    global running
    global openingmenubuttons_enabled
    global new_game_screen_passed

    mixer.music.load("Resources/Audio/MainScreenMusic.wav")                                                 #load the main screen music
    mixer.music.play(-1)                                                                                    #loop the music infinitely

    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
            if openingmenubuttons_enabled == True:                                                          #only allow the buttons to do something if this condition if True
                if button_pressed(new_game_button) == True:
                    openingmenubuttons_enabled = False                                                      #after clicking set the condition to False
                    new_game()
        if openingmenubuttons_enabled == False:                                                             #break out of this loop when the button condition is False (so after a button is clicked)
            break


#       MAINLOOP FUNCTION OF THE GAME       #

def mainloop():
    global running
    global openingmenubuttons_enabled
    running = True                                                                                          #controls whether or not the program runs (also used to exit smoothly)
    set_main()
    opening_screen()

    while running:
        main_menu()

 # # # # # # # #
#   MAIN CODE   #
 # # # # # # # #

mainloop()                                                                                                  #call the main loop and get the game started!
quit()