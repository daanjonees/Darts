while 1:
    print('Welcome to Daniels dart game!')
    remaining = 501
    while remaining > 0:
        print('What score did you get?')
        score = int(input())
        remaining = remaining - score 
        print(str(remaining) + ' Remaining')
    print('You have checked out! Do you want to play again?')
    keep_going = input()
    if keep_going != "y":
        break