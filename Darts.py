def can_checkout(rem):
    return bool((2 <= rem <= 170 and rem not in (169, 168, 166, 165, 163, 162, 159)))

def scoring_input(scr):
    return bool(scr <= 180 )

keep_going = 'y'

while keep_going == 'y':
    print('Welcome to Daniels dart game!')
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
        if cc is False:
            print("You can't checkout")
            remaining = remaining + score
        print(str(remaining) + ' Remaining')
    print('You have checked out! If you want to play again please input "y".')
    keep_going = input()
    