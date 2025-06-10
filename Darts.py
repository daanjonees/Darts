def make_player(name):
    return {'name': name}

def can_checkout(rem):
    return bool((rem <= 170 and rem not in (169, 168, 166, 165, 163, 162, 159)) or rem > 180)

def scoring_input(scr):
    return bool(0 <= scr <= 180)

keep_going = 'y'

print('Welcome to Daniels dart game!')

num_players = int(input("How many players are playing? "))
current_player = 0
game_players = []
for x in range(num_players):
    player_name = input('Player ' + str(current_player + 1) + ' name? ')
    game_players.append(make_player(player_name))

while keep_going == 'y': #Begins the game loop
    print('What game would you like to play?')
    remaining = int(input())

    while remaining > 0: 
        print('What score did you get?')
        score = int(input())

        while scoring_input(score) is False:
            print('The score entered is > 180, please input a new score')
            score = int(input())
        remaining = remaining - score 
        cc = can_checkout(remaining)

        while remaining == 1:
            print('You have gone bust!')
            remaining = remaining + score

        if cc is False:
            print("You can't checkout")
        print(str(remaining) + ' Remaining')
    print('You have checked out! If you want to play again please input "y".')
    keep_going = input()
    