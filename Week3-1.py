game=input('Numbers from 1 to 10')
print (game)
num =int(input('Guess the number:'))
sol=3
while   num!=sol :
    num =int(input('Guess the number:'))
    if num ==sol:
        print('Great! you did it')
        break
