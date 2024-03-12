#######################-GLOBAL VARIABLES-###########################
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #2D list that acts as a cartesian grid

#turn - keeps track of which player's turn it is
#player 1 - 1
#player 2 - 2
turn = 1

#Game Modes
#0 - Game Instructions menu
#1 - game started 
#2 - game over
mode = 0

#Scores - keeps track of each players scores based off their corresponding symbol
#player 1 - x
#player 2 - o
score_x = 0
score_o = 0

#Rounds - keeps track of the current round (up to four rounds)
rounds = 0

#######################-PROCESSING FUNCTIONS-#######################
def setup():
    size(800, 600)
    stroke(255)
    strokeWeight(4)
    frameRate(2.5) #framerate is changed to cause the 'game over' sign to blink at then end of the game
           
def draw():
    global mode, score_x, score_o, turn, rounds
    
    if mode == 0: #If the mode is set to Game Intructions menu
        menu_screen() 

    elif mode == 1: #if mode is set to the tic tac toe gameboard
        
        background(122, 156, 250) #purple
        noFill()
        draw_background()
        draw_gameboard()
        score_board()
        
        #check for winner
        if find_winners() != 0:
            #turn = 1, then player 2 has won since the turns update after each move
            #turn = 2, then player 1 has won for the same reason^^
            
            if turn == 1:
                print("Player #2 wins!!") 
                text("Winner: Player 2", 700, 100)
                score_o += 1 #Adds 1 to player 2 score
                print(score_o)
           
            elif turn == 2:
                print("Player #1 wins!!")
                text("Winner: Player 1", 700, 100)
                score_x += 1 #Adds 1 to player 1 score
                print(score_x)
            
            mode = 2 #Changes mode to 2 (game over screen) once a winner has been decided
        
            
    elif mode == 2: #if mode is set to the end/game over screen
        background(0)
        fill(242, 178, 48) #Yellow/orange color
        textSize(65)
        
        #Displays who won on the screen
        if turn == 1: #player 2 wins
            text("PLAYER 2 WINS!", 400, 225)
            
        elif turn == 2: #player 1 wins
            text("PLAYER 1 WINS!", 400, 225)
            
        fill(204, 14, 14) #red
        textSize(75)
        if frameCount % 2 == 0: #causes 'game over' to blink 
            text("GAME OVER", 400, 300)
        fill(255)
        textSize(20)
        
        #Give user furthur instructions on where they can go next
        text("To play again, click on the screen", 400, 370)
        text("To go back to the instructions, press 'r' on you keyboard", 400, 390)
        
           
def keyPressed():
    global mode, rounds
    
    #Intro Screen (mode 0)
    if key == ENTER:
        background(225)
        mode = 1
        return
    
    #Intro screen (mode 0)
    if key == 1:
        rounds = 1
    elif key == 2:
        rounds = 2
    elif key == 3:
        rounds = 3
    elif key == 4:
        rounds = 4
        
    #Game over screen (mode 2)
    if key == "r":
        #reset all variables to zero
        turn = 0
        rounds = 0
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        mode = 0 #Changes mode to 0 (intro screen)
    
    

def mousePressed():
    global turn, grid, mode
    #println( [mouseX/200, mouseY/200] )
    
    if mode == 1:
        #check that user clicks on gameboard
        if mouseX < 600:
            #integer division by 200
            if grid[mouseY/200][mouseX/200] == 0:
                grid[mouseY/200][mouseX/200] = turn
                next_turn()
                
    #user is sent back to tic tac toe screen if they click anywhere on the game over screen
    elif mode == 2:
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        mode = 1
        
        
        
#######################-LOGIC/CREATED FUNCTIONS-############################
    
def menu_screen():
    background(111, 188, 247)
    
    #title
    fill(255)
    textSize(50)
    textAlign(CENTER, CENTER)
    text("Tic Tac Toe", width / 2, 75)
    textSize(30)
    text("Game creator: Aisha Samnani", width / 2, 125)
    
    #Instructions for game
    textSize(20)
    text("Intructions:", width / 2, 175)
    textSize(15)
    text("This is a simple game of two-player tic, tac, toe:", width / 2, 200)
    text("Player 1: x \nPlayer 2: o", width / 2, 235)
    text("Players will take turns marking a cell with their symbol by clicking inside the cell with their mouse.", width / 2, 265)
    text("The first player to get three of their symbols in a row wins the game!!", width / 2, 285)
    
    text("Specify the number of rounds (up to 4) you would like to play by pressing a number on your keyboard", width / 2, 335)
    text("To start the game, press 'ENTER' on your keyboard.", width / 2, 355)

    
def find_winners():
    global grid
    #check for winner
    #returns the player number of the winner
    #int 1 or 2
    #returns 0 if there is no winner
    for y in range(3):
        if grid[0][0] == grid[0][1] == grid[0][2] != 0:
            return grid[y][0]
        elif grid[1][0] == grid[1][1] == grid[1][2] != 0:
            return grid[y][0]
        elif grid[2][0] == grid[2][1] == grid[2][2] != 0:
            return grid[y][0]
        elif grid[0][0] == grid[1][0] == grid[2][0] != 0:
            return grid[y][0]
        elif grid[0][1] == grid[1][1] == grid[2][1] != 0:
            return grid[y][0]
        elif grid[0][2] == grid[1][2] == grid[2][2] != 0:
            return grid[y][0]
        elif grid[0][0] == grid[1][1] == grid[2][2] != 0:
            return grid[y][0]
        elif grid[0][2] == grid[1][1] == grid[2][0] != 0:
            return grid[y][0]
   
        return 0

                                                                                  
def draw_gameboard():
    global grid
    #draw gameboard based on list
    
    #loop through rows   
    for y in range(3):
        
        #loop through coloumn
        for x in range(3):
            #check for 1 -> x, 2 -> o
            
            #Draws an o
            if grid[y][x] == 2:
                ellipse((x * 200) + 100, (y * 200) + 100, 100, 100)
                
            #Drdws an x
            if grid[y][x] == 1:
                line(0 + 200*x, 0 + 200*y, 200 + 200*x, 200 + 200*y)
                line(200 + 200*x, 0 + 200*y, 0 + 200*x, 200 + 200*y)
                                
                                                                                                                                                  
def draw_background():
    
    #draws game board
    for y in range(3):
        for x in range(3):
            rect(200 * x, 200 * y, 200, 200)                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                

def next_turn():
    global turn
    #alternates turns
    if turn == 1:
        turn = 2
    else:
        turn = 1
        

def score_board():
    #Displays current round on the screen
    textSize(15)
    text("Round: 1", 700, 25)
    
    #Displays score board
    text("Scores", 700, 85)
    line(650, 100, 750, 100)
    line(700, 100, 700, 175)
    text("x", 675, 110)
    text("o", 725, 110)
    text("l", 675, 150)
    
