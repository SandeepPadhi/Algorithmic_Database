"""
Date:8/02/2021
Name:Sandeep Padhi
MCS20006

Run below program to play game with computer.

There are around 20000 states in Tic-Tac-Toe game as there are 3^9 states.
"""
import numpy as np
import random
#import defaultdict
from collections import defaultdict
import pickle
import time
#from os import system
#clear = lambda: system('clear')



class Players:
    def __init__(self,lr,gamma):
        self.states=[]
        self.gamma=gamma
        self.lr=lr
        self.state_values={}
        self.winner=False
        self.times=0
        #self.state_values["000000000"]=0
def getAvailablePositions(board):
    Position=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                Position.append((i,j))
    return Position

def getBoardHash(board):
    Hash=""
    for i in range(len(board)):
        for j in range(len(board[0])):
            Hash+=str(board[i][j])
    return Hash   

def getPosition(Positions,P2,board,Player):
    #val=random.random()
    exp=np.random.uniform(0, 1)
    P=P2
    action=0
    valueaction={}
    val=0
    #explore
    if False:
        #i=random.randint(0,len(Positions)-1)
        idx = np.random.choice(len(Positions))
        action=idx
    else:
        #row check
        for i in range(3):
            R=board[i]
            if R[0]*R[2]==1 and board[i][1]==0:
                pos=(i,1)
                Positions.remove(pos)
                return pos
            for j in range(1,3):
                if R[j-1]*R[j]==1:
                        if j==1 and  board[i][2]==0:
                                pos=(i,2)
                                Positions.remove(pos)
                                return pos
                        elif board[i][0]==0:
                                pos=(i,0)
                                Positions.remove(pos)
                                return pos
        
        #Cols check
        board=list(zip(*board))
        for i in range(3):
            R=board[i]
            if R[0]*R[2]==1 and board[i][1]==0:
                pos=(1,i)
                Positions.remove(pos)
                return pos


            for j in range(1,3):
                if R[j-1]*R[j]==1:
                        if board[i][2]==0:
                            pos=(2,i)
                            Positions.remove(pos)
                            return pos
                        elif board[i][0]==2:
                                pos(0,i)
                                Positions.remove(pos)
                                return pos
        board=list(zip(*board))

        #Diag check-topleft to down-right
        if board[0][0]*board[2][2]==1 and board[1][1]==0:
            pos=(1,1)
            Positions.remove(pos)
            return pos
        

        for i in range(1,3):
            if board[i][i]*board[i-1][i-1]==1:
                if board[2][2]==0:
                    pos=(2,2)
                    Positions.remove(pos)
                    return pos
                elif board[0][0]==0:
                    pos=(0,0)
                    Positions.remove(pos)
                    return pos
        
        if board[0][2]*board[2][0]==1 and board[1][1]==0:
            pos=(1,1)
            Positions.remove(pos)
            return pos

        #Diag check-topright to down-left
        for i in range(1,3):
            if board[i][3-i]*board[i][2-i]==1:
                if board[0][2]==0:
                    pos=(0,2)
                    Positions.remove(pos)
                    return pos
                elif board[2][0]==0:
                    pos=(2,0)
                    Positions.remove(pos)
                    return pos
                    
        

        action=0
        val=-10000
        for i in range(len(Positions)):
            boardcopy=[[board[x][y] for x in range(3)] for y in range(3)]
            (x,y)=Positions[i]
            boardcopy[x][y]=1
            
            boardhash=getBoardHash(boardcopy)
            if boardhash not in P.state_values:
                P.state_values[boardhash]=0
            v=P.state_values[boardhash]
            if v>=val:
                val=v
                action=i
                if v not in valueaction:
                    valueaction[v]=[]
                valueaction[v].append(action)
        Actions=valueaction[val]
        action_index=random.randint(0,len(Actions)-1)
        action=Actions[action_index]
    pos=Positions[action]
    Positions.pop(action)
    return pos
         
def updateBoard(pos,Player,P1,P2,board):
    P=None
    if Player==1:
        P=P1
    else:
        P=P2
    x,y=pos
    board[x][y]=Player
    #boardhash=getBoardHash(board)
    #P.states.append(boardhash)

def IsWinner(board,Player,Positions):
    
    for i in range(3):
        if sum(board[i])==3*Player:
            return True
        if sum(board[j][i] for j in range(3))==3*Player:
            return True
    S1=0
    S2=0
    for i in range(3):
        S1+=board[i][i]
        S2+=board[i][2-i]
    if S1==3*Player or S2==3*Player:
        return True
    
    if len(Positions)==0:
        print("Tie")
        return True
    return False
    
def giveReward(R1,R2,P1,P2):
    lr=0.3
    g=0.2
    while(len(P1.states)):
        st=P1.states[-1]
        if st not in P1.state_values:
            P1.state_values[st]=0
        P1.state_values[st]+=lr*(g*R1-P1.state_values[st])
        P1.states.pop()
        R1=P1.state_values[st]
    
    while(len(P2.states)):
        st=P2.states[-1]
        if st not in P2.state_values:
            P2.state_values[st]=0
        P2.state_values[st]+=lr*(g*R2-P2.state_values[st])
        P2.states.pop()
        R2=P2.state_values[st]
    
    
def drawBoard(board):
    print("Board:")
    print("-----------------")
    print("| {}    {}     {}|".format(board[0][0],board[0][1],board[0][2]))
    print("| {}    {}     {}|".format(board[1][0],board[1][1],board[1][2]))   
    print("| {}    {}     {}|".format(board[2][0],board[2][1],board[2][2]))   
    print("------------------")

        
lr=0.3
gamma=0.2
P1=None
P2=None
Turn=True
Player=1

print("Lets Toss")
for i in range(4):
    print("...")
    time.sleep(1)
Toss=random.uniform(0,1)
win=""
if Toss<0.5:
    print("You Play first")
    with open('Player2','rb') as db:
        P2=pickle.load(db)
        Turn=True
        win="You"
else:
    print("Computer Play first")
    with open('Player1','rb') as db:
        P2=pickle.load(db)
        Turn=False
        win="Computer"
  


Rounds=1
while(Rounds):
    print("Rounds:{}".format(Rounds))
    board=[[0 for _ in range(3)] for _ in  range(3)]
    Positions=getAvailablePositions(board)
    print("Positions:{}".format(Positions))
    i=0

    while(True):
        pos=None
        drawBoard(board)
        #print("board:{}".format(board))
        if Turn:
            pos=tuple(map(int,input("Your Turn:Enter pos->").split()))
            print("pos:{}".format(pos))
            Positions.remove(pos)
        else:
            print("Computer's Turn")
            print("Thinking..",end="")
            for i in range(4):
                print("..")
                time.sleep(1)
            
            pos=getPosition(Positions,P2,board,Player)
            print("pos:{}".format(pos))
        x,y=pos[0],pos[1]
        board[x][y]=Player
            
        i+=1
        #updateBoard(pos,Player,P1,P2,board)
        if IsWinner(board,Player,Positions):
            break
        Player=-Player
        Turn=not Turn
        #clear()


    #print("i:{}".format(i))
    
    if len(Positions)==0:
        print("Tie")
    elif win=='Computer':
        if Player==1:
            print("Computer wins")
        else:
            print("You wins")
    else:
        if Player==1:
                print("You wins")
        else:
            print("Computer wins")   
  
    Rounds-=1

print("Game Ends")