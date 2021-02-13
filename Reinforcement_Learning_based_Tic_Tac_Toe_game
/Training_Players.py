"""
Date:8/01/2021
Name:Sandeep Padhi
Id:MCS20006

Run following program to train the players.
Player1:Attacker
Player2:Defender
"""
import numpy as np
import random
#import defaultdict
from collections import defaultdict
import pickle
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

def getPosition(Player,Positions,P1,P2,board):
    #val=random.random()
    exp=np.random.uniform(0, 1)
    P=None
    action=0
    valueaction={}
    val=0
    if Player==1:
        P=P1
    else:
        P=P2
    #explore
    if 0.4<exp<0.8:
        #i=random.randint(0,len(Positions)-1)
        idx = np.random.choice(len(Positions))
        action=idx
    else:
        action=0
        val=-10000
        for i in range(len(Positions)):
            boardcopy=[[board[x][y] for x in range(3)] for y in range(3)]
            (x,y)=Positions[i]
            boardcopy[x][y]=Player
            
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
    boardhash=getBoardHash(board)
    P.states.append(boardhash)

def IsWinner(board,Player,P1,P2,Positions):
    
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
        #print("Tie")
        return True
    return False
    
def giveReward(R1,R2,P1,P2):
    lr=0.2
    g=1
    decay=0.9
    while(len(P1.states)):
        st=P1.states[-1]
        if st not in P1.state_values:
            P1.state_values[st]=0
        P1.state_values[st]+=lr*(g*R1-P1.state_values[st])
        P1.states.pop()
        g*=decay
        R1=P1.state_values[st]
    
    g=1
    decay=0.1
    while(len(P2.states)):
        st=P2.states[-1]
        if st not in P2.state_values:
            P2.state_values[st]=0
        P2.state_values[st]+=lr*(g*R2-P2.state_values[st])
        P2.states.pop()
        g*=decay
        R2=P2.state_values[st]
    
    
        
        
lr=0.3
gamma=0.8
P1=Players(lr,gamma)
P2=Players(lr,gamma)


Rounds=100000
while(Rounds):
    if Rounds%1000==0:
        print("Rounds:{}".format(Rounds))
    #if Rounds&1:
    #    P1,P2=P2,P1
    Player=1
    board=[[0 for _ in range(3)] for _ in  range(3)]
    Positions=getAvailablePositions(board)
    i=0
    while(True):
        i+=1
        pos=getPosition(Player,Positions,P1,P2,board)
        updateBoard(pos,Player,P1,P2,board)
        if IsWinner(board,Player,P1,P2,Positions):
            break
        Player=-Player

    
    R1,R2=0,0
    if len(Positions)==0:
        R1,R2=0.0,0.5
    elif Player==1:
        #print("P1 wins")
        R1=2
        R2=-1
        P1.times+=1
    else:
        #print("P2 wins")
        R2=2
        R1=-1
        P2.times+=1
        
    giveReward(R1,R2,P1,P2)
    Rounds-=1

with open('Player1','wb') as db:
        pickle.dump(P1,db)


with open('Player2','wb') as db:
        pickle.dump(P2,db)

        
print("P1.times:{}".format(P1.times))
print("len of states:{}".format(len(P1.state_values)))
#print("P1.state_values:{}".format(P1.state_values))
print()
print()
print("P2.times:{}".format(P2.times))
#print("P1.state_values:{}".format(P1.state_values))





    