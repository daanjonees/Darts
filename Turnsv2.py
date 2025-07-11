def make_player(name,starting_score):
    return {'name': name,
            'score': starting_score}

def can_checkout(rem):
    return bool((rem <= 170 and rem not in (169, 168, 166, 165, 163, 162, 159)) or rem > 180)

def scoring_input(scr):
    return bool(0 <= scr <= 180)

def throwing_input(thr):
    return bool(1 <= thr <= 2)

def player_numbers(playnum):
    return bool(1 <= playnum <= 2)

print('Welcome to Daniels dart game!')

print('What game would you like to play?') #Defines the starting scores 
remaining = int(input())

num_players = int(input("How many players are playing?"))
game_players = []

while player_numbers(num_players) is False:
    print('Please input either 1 or 2 players.')
    num_players = int(input())

if num_players == 1: #need to add in condition to begin again for 1 or 2 players not playing.
    singleplayer = 'y'
elif num_players == 2:
    singleplayer = 'n'
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
        remaining = player1_starting_score
        remaining = player2_starting_score    