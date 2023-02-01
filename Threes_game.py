
"""
Created on Wed Feb  1 09:09:40 2023

@author: mohamad elyasi

mail: elyasi.mohamad@gmail.com
"""
import copy
import math

def isMergeable(a,b):
    if(a==b and a!=1 and a!=2 and a!=0 ):
        return True
    elif (a+b)==3:
        return True
    else:
        return False
    
def goUp(state,n):
    M=copy.deepcopy(state)
    for i in range(n-1):
        for j in range(n):
            if isMergeable(M[i][j], M[i+1][j]):
                M[i][j]=M[i][j]+M[i+1][j]
                M[i+1][j]=0
            elif M[i][j]==0 and M[i+1][j]!=0:
                M[i][j]=M[i+1][j]
                M[i+1][j]=0
            else:
                continue
    return M    
def goDown(state,n):
    M=copy.deepcopy(state)
    for i in range(n-1)[::-1]:
        for j in range(n):
            if isMergeable(M[i][j], M[i+1][j]):
                M[i+1][j]=M[i][j]+M[i+1][j]
                M[i][j]=0
            elif M[i+1][j]==0 and M[i][j]!=0:
                M[i+1][j]=M[i][j]
                M[i][j]=0
            else:
                continue
    return M     

def goLeft(state,n):
    M=copy.deepcopy(state)
    for j in range(n-1):
        for i in range(n):
            if isMergeable(M[i][j], M[i][j+1]):
                M[i][j]=M[i][j]+M[i][j+1]
                M[i][j+1]=0
            elif M[i][j]==0 and M[i][j+1]!=0:
                M[i][j]=M[i][j+1]
                M[i][j+1]=0
            else:
                continue
    return M     

def goRight(state,n):
    M=copy.deepcopy(state)
    for j in range(n-1)[::-1]:
        for i in range(n):
            if isMergeable(M[i][j], M[i][j+1]):
                M[i][j+1]=M[i][j]+M[i][j+1]
                M[i][j]=0
            elif M[i][j+1]==0 and M[i][j]!=0:
                M[i][j+1]=M[i][j]
                M[i][j]=0
            else:
                continue
    return M
def number_of_empty_cells(M,n,move):
    count=0
    if move=='U':
        for i in range(n):
            if(M[n-1][i]==0):
                count+=1
    elif move=='D':
        for i in range(n):
            if(M[0][i]==0):
                count+=1
    elif move=='R':
        for i in range(n):
            if(M[i][0]==0):
                count+=1
    elif move=='L':
        for i in range(n):
            if(M[i][n-1]==0):
                count+=1
    return count
        
def insert_new_item(state,n,item,move):
    M=copy.deepcopy(state)
    m=number_of_empty_cells(M,n,move)
    if m==0:
        return M
    if move=='U':
        k=0
        for i in range(n):
            if(M[n-1][i]==0):
                if((item[0]%m)==k):
                    M[n-1][i]=item[1]
                    return M
                else:
                    k+=1

    elif move=='D':
        k=0
        for i in range(n):
            if(M[0][i]==0):
                if((item[0]%m)==k):
                    M[0][i]=item[1]
                    return M
                else:
                    k+=1
    elif move=='R':
        k=0
        for i in range(n):
            if(M[i][0]==0):
                if((item[0]%m)==k):
                    M[i][0]=item[1]
                    return M
                else:
                    k+=1
    elif move=='L':
        k=0
        for i in range(n):
            if(M[i][n-1]==0):
                if((item[0]%m)==k):
                    M[i][n-1]=item[1]
                    return M
                else:
                    k+=1
    
def score_calculate(M,n):
   score=0 
   for i in range(n):
       for j in range(n):
           if(M[i][j]!=0 and M[i][j]!=1 and M[i][j]!=2):
               x=M[i][j]/3
               k=math.log2(x)
               score+=3**(k+1)
   return score

def exist_motion(M,n):
       state=copy.deepcopy(M)
       new_state=goUp(state, n)
       if(new_state!=state):
           return True    
       new_state=goDown(state, n)
       if(new_state!=state):
           return True 
       new_state=goRight(state, n)
       if(new_state!=state):
           return True 
       new_state=goLeft(state, n)
       if(new_state!=state):
           return True
       return False
    
     
# n=int(input())
# start_state=[[0]*n]*n
# for i in range(n):
#     start_state[i]=[int(x) for x in input().split()]
# movements=input()
# new_numbers=[[0,0]]*len(movements)
# for i in range(len(movements)):
#     new_numbers[i]=[int(x) for x in input().split()]

n=4
start_state=[[0,1,1,3],[2,0,0,3],[0,1,0,1],[3,2,0,0]]
movements='DDLUULDRLL'
new_numbers=[[0,1],[3,2],[2,2],[3,3],[1,2],[3,1],[0,2],[3,1],[3,1],[2,3]]

# start_state=[[0,1,1,3],[0,0,1,3],[0,0,1,1],[0,0,3,2]]
# movements='RRRD'
# new_numbers=[[3,2],[0,2],[1,2],[2,3]]

state= copy.deepcopy(start_state)
for i in range(len(movements)):
    if movements[i]=='U':
       new_state=goUp(state, n)
       if(new_state!=state):
           state=insert_new_item(new_state,n,new_numbers[i],'U')
    elif movements[i]=='D':
       new_state=goDown(state, n)
       if(new_state!=state):
           state=insert_new_item(new_state,n,new_numbers[i],'D')
    elif movements[i]=='R':
       new_state=goRight(state, n)
       if(new_state!=state):
           state=insert_new_item(new_state,n,new_numbers[i],'R')
    elif movements[i]=='L':
       new_state=goLeft(state, n)
       if(new_state!=state):
           state=insert_new_item(new_state,n,new_numbers[i],'L')
score=score_calculate(state, n)

for i in range(n):
    for j in range(n):
        print(state[i][j],end='\t')
    print('\n')
if exist_motion(state, n):
    print("The partial score is {}.".format(int(score)))
else:
    print("The final score is {}.".format(int(score)))
