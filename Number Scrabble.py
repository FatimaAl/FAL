player1=[]
player2=[]
noftries=0
print("Enter your name player1:")
name1=input()
print("Enter your name player2:")
name2=input()
lst={1,2,3,4,5,6,7,8,9}
print (lst)

while noftries<9:
    if noftries<9:
        print(name1,"Enter a number from the list:")
        x=int(input())
        player1.append(x)
        noftries+=1
        lst.remove(x)
        print (lst)
    if noftries<9:
        print(name2,"Enter a number from the list:")
        y=int(input())
        player2.append(y)
        noftries+=1
        lst.remove(y)
        print(lst)
print(player1)
print (player2)
if (player1[1] + player1[2] + player1[3]==15) or (player1[2] + player1[3] + player1[4] ==15) or (player1[1] + player1[3] + player1[4] ==15) or (player1[1] + player1[2] + player1[4] ==15):
          print (name1,"win") 
elif (player2[1] + player2[2] + player2[3] ==15):
       print (name2,"win")
elif ((player1[1] + player1[2] + player1[3] ==15) or (player1[2] + player1[3] + player1[4] ==15) or (player1[1] + player1[3] + player1[4] ==15) or (player1[1] + player1[2] + player1[4] ==15)) and(player2[1] + player2[2] + player2[3] ==15):
     
       print("the game is draw")
          
else :
          print ("the game is draw")
        
