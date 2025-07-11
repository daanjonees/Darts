player1 = 'Dan'
player2 = 'John'
player1status = True
player2status = True

starting_score = int(input("What is the starting score?"))
player1score = starting_score
player2score = starting_score

starting_player = int(input('Who will be be playing first, player 1 or 2?'))
if starting_player == 1:
    player1status = True
    player2status = False
elif starting_player == 2:
    player1status = False
    player2status = True
elif starting_player != 1 or 2:
    print('There can only be 2 players')

print(player1status)
print(player1status)




#while player1status == True:
#    score = int(input(print('What score did you get?')))
#    starting_score - score = 