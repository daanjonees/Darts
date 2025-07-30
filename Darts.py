class Players:
    def __init__(self, name, score):
     self.name = name
     self.score = score

def can_checkout(rem):
    return bool((rem <= 170 and rem not in (169, 168, 166, 165, 163, 162, 159)) or rem > 180)

def scoring_input(scr):
    return bool(0 <= scr <= 180)

def throwing_input(thr):
    return bool(1 <= thr <= 2)

def player_numbers(playnum):
    return bool(1 <= playnum <= 2)

print('Welcome to Daniels dart game!')

print('What game would you like to play?') 
remaining = int(input())

print("How many players are playing?")
num_players = int(input())

if num_players == 1:
    singleplayer = 'y'
    print('What is your name?')
    P1name = input()
    P1 = Players(P1name, remaining)

elif num_players == 2:
    singleplayer = 'n'
    print('What is the name of player 1?')
    P1name = input()
    P1 = Players(P1name, remaining)

    print('What is the name of player 2?')
    P2name = input()
    P2 = Players(P2name, remaining)

    print('Who will be throwing first? Player 1 or 2?')
    throw_first = int(input())
    
    while throwing_input(throw_first) is False:
        print('Please confirm either player 1 or 2.')
        throw_first = int(input())
    
    if throw_first == 1:
        player1_status = True
        player2_status = False
    elif throw_first == 2:
        player1_status = False
        player2_status = True


while singleplayer == 'y': #Begins the game loop currently this holds the main game loop for the game to begin, need to re-arrange. 

    while P1.score > 0: 
            
        print('Remaining score : ' + str(P1.score))
        print('What score did you get?')
        score = int(input())

        while scoring_input(score) is False:
            print('The score entered is > 180, please input a new score')
            score = int(input())

        P1.score = P1.score - score 
        cc = can_checkout(P1.score)

        while P1.score == 1:
            print('You have gone bust')
            P1.score = P1.score + score

        if cc is False:
            print('Checkout is possible:') #need to work out why this isn't working.
    singleplayer == 'n'
    print('You have checked out')    #need to fix an infinite loop here.



while singleplayer == 'n': 

    if player1_status == True:
    
        if P1.score > 0:         
            print('Remaining score : ' + str(P1.score))
            print('What score did you get?')
            score = int(input())

            if scoring_input(score) is False:
                print('The score entered is > 180, please input a new score')
                score = int(input())

            P1.score = P1.score - score 
            cc = can_checkout(P1.score)

            if P1.score == 1:
                print('You have gone bust')
                P1.score = P1.score + score

            if cc is False:
                print('Checkout is possible:') #need to work out why this isn't working.
        print('You have checked out')    #need to fix an infinite loop here.

        if P1.score > 0:
                    print("P2's turn")
                    player1_status = False
                    player2_status = True 
        else: print(str(P2.name) + 'turn to throw.')         
    
    elif player2_status == True:
    
        if P2.score > 0: 
                
            print('Remaining score : ' + str(P2.score))
            print('What score did you get?')
            score = int(input())
    
            if scoring_input(score) is False:
                print('The score entered is > 180, please input a new score')
                score = int(input())

            P2.score = P2.score - score 
            cc = can_checkout(P1.score)

            if P2.score == 1:
                print('You have gone bust')
                P2.score = P2.score + score

            if cc is False:
                print('Checkout is possible:') #need to work out why this isn't working.
        print('You have checked out')    #need to fix an infinite loop here.

        if P2.score > 0:
                    print("P1's turn")
                    player1_status = True
                    player2_status = False 
        else: print(str(P1.name) + 'turn to throw.')       