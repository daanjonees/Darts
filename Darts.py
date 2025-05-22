print('Welcome to Daniels dart game!')

remaining = 501
while remaining > 0:
    print('What score did you get?')
    score = int(input())
    remaining = remaining - score 
    print(str(remaining) + ' Remaining')
print('You have chekced out!')
