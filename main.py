#Maybe this is not the clearest code, but it is grown from simple player vs. player mode.
#This project is not so important to make it perfect, but most of iterations are built in functions
#Good Architecture of the code is shown in the last "startgame" function
#I have not used Classes here - only existing objects and functions
#AI is primitive and unsofisticated but invincible in "hard" mode

from IPython.display import clear_output
import random
board=[" "," "," "," "," "," "," "," "," ",]
nums=[1,2,3,4,5,6,7,8,9]

#Drawing an empty Board...

def b_d():
    print "   " + "|" + "   " + "|" + "   " 
    print " " +str(board[0]) + " " + "|" + " " +str(board[1]) + " " + "|" + " " +str(board[2]) + " " 
    print " " +str(nums[0]) + " " + "|" + " " +str(nums[1]) + " " + "|" + " " +str(nums[2]) + " " 
    print "-----------"
    print "   " + "|" + "   " + "|" + "   " 
    print " " +str(board[3]) + " " + "|" + " " +str(board[4]) + " " + "|" + " " +str(board[5]) + " " 
    print " " +str(nums[3]) + " " + "|" + " " +str(nums[4]) + " " + "|" + " " +str(nums[5]) + " " 
    print "-----------"
    print "   " + "|" + "   " + "|" + "   " 
    print " " +str(board[6]) + " " + "|" + " " +str(board[7]) + " " + "|" + " " +str(board[8]) + " " 
    print " " +str(nums[6]) + " " + "|" + " " +str(nums[7]) + " " + "|" + " " +str(nums[8]) + " " 

#Declare rows, that can win 
    
w1=[]
w2=[]
w3=[]
w4=[]
w5=[]
w6=[]
w7=[]
w8=[]
    
    
def game_over():
    '''
    Here are all winning combinations
    '''
    if board[0]==board[1]==board[2]!=" " or \
    board[3]==board[4]==board[5]!=" " or \
    board[6]==board[7]==board[8]!=" " or \
    board[0]==board[4]==board[8]!=" " or \
    board[2]==board[4]==board[6]!=" " or \
    board[0]==board[3]==board[6]!=" " or \
    board[1]==board[4]==board[7]!=" " or \
    board[2]==board[5]==board[8]!=" ":
        return True
    else:
        False

      
        
def end_game(a):
    '''
    This should be called, when the game hits winning raw
    '''
    global board
    print "Game over! {} wins!".format(a)
    board=[" "," "," "," "," "," "," "," "," ",]

    
#All inputs will return a non-fatal error and ask to input again, if player won't follow the instructions

#Player cannot type number of places, that are already matched with a sign
    
def player_turn(a):
    '''
    This is how we iteracting with human player
    '''
    global board
    i=raw_input("Player {} is on: ".format(a))
    while ["1","2","3","4","5","6","7","8","9"].count(i)==0 or board[int(i)-1]!=" ":
        i=raw_input("Player {0}, once again, type the number \
between 1 and 9, and use only free spaces! Player {0} is on: ".format(a))       
    board.pop(int(i)-1)
    board.insert(int(i)-1,a)
    clear_output()
    b_d()
    rewrite()

def players():
    '''
    These are adjustments for the game with number of players and dificulty level
    '''
    global p1
    global p2
    global level
    i=raw_input("How many players? 1 or 2? :")
    while ["1","2"].count(i)==0 :
        i=raw_input("Please, type only 1 or 2! How many players? :")
    if int(i)==2:
        p1="human"
        p2="human"
    else:
        level=raw_input('Choose Dificulty Level. Please, type 1 for "easy", 2 for "medium" or 3 for "hard" :')
        while ["1","2","3"].count(level)==0 :
            level=raw_input('Please, type only 1, 2 or 3! Please, type 1 for "easy", 2 for "medium" or 3 for "hard" :')
        a=raw_input('Choose your sign: "X" or "O"? Please, type 1 for "X" or 2 for "O" :')
        while ["1","2"].count(a)==0 :
            a=raw_input('Please, type only 1 or 2! What is your sign? :')
        if a=="1":
            p1="human"
            p2="AI"
        else:
            p1="AI"
            p2="human"
            
def ai_l_turn(a):
    '''
    Ease mode of AI's turn. Simple random
    '''
    global board
    i=random.randint(0,8)
    while board[i]!=" ":
        i=random.randint(0,8)
    board.pop(i)
    board.insert(i,a)
    clear_output()
    b_d()

def rewrite():
    '''
    rewriting current stage of winning rows
    '''
    global w1
    global w2
    global w3
    global w4
    global w5
    global w6
    global w7
    global w8
    w1=[board[0],board[1],board[2]]
    w2=[board[3],board[4],board[5]]
    w3=[board[6],board[7],board[8]]
    w4=[board[0],board[4],board[8]]
    w5=[board[2],board[4],board[6]]
    w6=[board[0],board[3],board[6]]
    w7=[board[1],board[4],board[7]]
    w8=[board[2],board[5],board[8]]
    
#Great part of next two functions are similar to each other. Initially AI was not very clever - it could
#only try to win in this turn or not let the human player to win in next turn.
#Afterthat I copied AI's function and added some combinations, that make "hard" AI invincible
    
def ai_h_turn(a):
    '''
    Hard mode of AI's turn. You won't win, computer has a chance against weak player
    '''
    global board
    if a=="X":
        b="O"
    else: 
        b="X"
    
    if w1.count(a)==2 and w1.count(" ")==1:
        i=w1.index(" ")
    elif w2.count(a)==2 and w2.count(" ")==1:
        i=w2.index(" ")+3
    elif w3.count(a)==2 and w3.count(" ")==1:
        i=w3.index(" ")+6
    elif w4.count(a)==2 and w4.count(" ")==1:
        if w4.index(" ")==0:
            i=0
        elif w4.index(" ")==1:
            i=4
        else :
            i=8
    elif w5.count(a)==2 and w5.count(" ")==1:
        if w5.index(" ")==0:
            i=2
        elif w5.index(" ")==1:
            i=4
        else :
            i=6
    elif w6.count(a)==2 and w6.count(" ")==1:
        if w6.index(" ")==0:
            i=0
        elif w6.index(" ")==1:
            i=3
        else :
            i=6
    elif w7.count(a)==2 and w7.count(" ")==1:
        if w7.index(" ")==0:
            i=1
        elif w7.index(" ")==1:
            i=4
        else :
            i=7
    elif w8.count(a)==2 and w8.count(" ")==1:
        if w8.index(" ")==0:
            i=2
        elif w8.index(" ")==1:
            i=5
        else :
            i=8
    elif w1.count(b)==2 and w1.count(" ")==1:
        i=w1.index(" ")
    elif w2.count(b)==2 and w2.count(" ")==1:
        i=w2.index(" ")+3
    elif w3.count(b)==2 and w3.count(" ")==1:
        i=w3.index(" ")+6
    elif w4.count(b)==2 and w4.count(" ")==1:
        if w4.index(" ")==0:
            i=0
        elif w4.index(" ")==1:
            i=4
        else :
            i=8
    elif w5.count(b)==2 and w5.count(" ")==1:
        if w5.index(" ")==0:
            i=2
        elif w5.index(" ")==1:
            i=4
        else :
            i=6
    elif w6.count(b)==2 and w6.count(" ")==1:
        if w6.index(" ")==0:
            i=0
        elif w6.index(" ")==1:
            i=3
        else :
            i=6
    elif w7.count(b)==2 and w7.count(" ")==1:
        if w7.index(" ")==0:
            i=1
        elif w7.index(" ")==1:
            i=4
        else :
            i=7
    elif w8.count(b)==2 and w8.count(" ")==1:
        if w8.index(" ")==0:
            i=2
        elif w8.index(" ")==1:
            i=5
        else :
            i=8
    elif board.count(" ")==9:
        i=4
    elif board.count(" ")==8:
        if board[4]==" ":
            i=4
        else:
            i=0
    elif board.count(" ")==6 and (w2.count(" ")==0 or w7.count(" ")==0): 
        i=0
    elif board[1]==board[3]==b and board[0]==" ":
        i=0
    elif board[1]==board[5]==b and board[2]==" ":
        i=2
    elif board[3]==board[7]==b and board[6]==" ":
        i=6
    elif board[7]==board[5]==b and board[8]==" ":
        i=8        
    else: 
        if w2.count(" ")==2:
            i=3
        elif w7.count(" ")==2:
            i=1
        else:
            i=board.index(" ")
          
    board.pop(i)
    board.insert(i,a)
    clear_output()
    b_d()
    rewrite()




def ai_m_turn(a):
    '''
    Medium mode of AI's turn. Computer tries to win in 1 turn or not give you a chance
    to win in your next turn. Otherwise - random
    '''
    global board
    if a=="X":
        b="O"
    else: 
        b="X"
    
    if w1.count(a)==2 and w1.count(" ")==1:
        i=w1.index(" ")
    elif w2.count(a)==2 and w2.count(" ")==1:
        i=w2.index(" ")+3
    elif w3.count(a)==2 and w3.count(" ")==1:
        i=w3.index(" ")+6
    elif w4.count(a)==2 and w4.count(" ")==1:
        if w4.index(" ")==0:
            i=0
        elif w4.index(" ")==1:
            i=4
        else :
            i=8
    elif w5.count(a)==2 and w5.count(" ")==1:
        if w5.index(" ")==0:
            i=2
        elif w5.index(" ")==1:
            i=4
        else :
            i=6
    elif w6.count(a)==2 and w6.count(" ")==1:
        if w6.index(" ")==0:
            i=0
        elif w6.index(" ")==1:
            i=3
        else :
            i=6
    elif w7.count(a)==2 and w7.count(" ")==1:
        if w7.index(" ")==0:
            i=1
        elif w7.index(" ")==1:
            i=4
        else :
            i=7
    elif w8.count(a)==2 and w8.count(" ")==1:
        if w8.index(" ")==0:
            i=2
        elif w8.index(" ")==1:
            i=5
        else :
            i=8
    elif w1.count(b)==2 and w1.count(" ")==1:
        i=w1.index(" ")
    elif w2.count(b)==2 and w2.count(" ")==1:
        i=w2.index(" ")+3
    elif w3.count(b)==2 and w3.count(" ")==1:
        i=w3.index(" ")+6
    elif w4.count(b)==2 and w4.count(" ")==1:
        if w4.index(" ")==0:
            i=0
        elif w4.index(" ")==1:
            i=4
        else :
            i=8
    elif w5.count(b)==2 and w5.count(" ")==1:
        if w5.index(" ")==0:
            i=2
        elif w5.index(" ")==1:
            i=4
        else :
            i=6
    elif w6.count(b)==2 and w6.count(" ")==1:
        if w6.index(" ")==0:
            i=0
        elif w6.index(" ")==1:
            i=3
        else :
            i=6
    elif w7.count(b)==2 and w7.count(" ")==1:
        if w7.index(" ")==0:
            i=1
        elif w7.index(" ")==1:
            i=4
        else :
            i=7
    elif w8.count(b)==2 and w8.count(" ")==1:
        if w8.index(" ")==0:
            i=2
        elif w8.index(" ")==1:
            i=5
        else :
            i=8
    
    else :
        i=random.randint(0,8)
        while board[i]!=" ":
            i=random.randint(0,8)
    board.pop(i)
    board.insert(i,a)
    clear_output()
    b_d()
    rewrite()



def next_turn(x,y):
    '''
    Looks in adjustments and start next turn for other player according to initial game adjustments
    '''
    if x=="human":
        player_turn(y)
    elif x!="human" and level=="3":
        ai_h_turn(y)
    elif x!="human" and level=="2":
        ai_m_turn(y)
    else:
        ai_l_turn(y)
    
def start_game():
    '''
    starts the game, makes sure, that there is no winning combination, defines the winner, ends game
    '''
    rewrite()
    players()
    global board
    b_d()
    while not game_over():
        next_turn(p1,"X")
        if game_over():
            end_game("X")
            break
        else:
            if not board.count(" ")==0:
                next_turn(p2,"O")
                if game_over():
                    end_game("O")
                    break
            else:
                end_game("Draw! Nobody")
                break

#For start playing type: start_game()
