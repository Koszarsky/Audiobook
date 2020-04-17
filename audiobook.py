def timeRemaining (hours,mintues,speed):
    hoursToMin = hours * 60
    hoursPlusMin = hoursToMin + mintues
    speedAlteredTotal = hoursPlusMin / speed
    speedAlteredTotal = int(round(speedAlteredTotal))
    speedAlteredMin = speedAlteredTotal % 60
    speedAlteredHours = (speedAlteredTotal - speedAlteredMin)/60
    print('At your current speed of ' + str(listenSpeed) + ' you will finish your book in ' + str(speedAlteredHours) + ' hours and ' + str(speedAlteredMin) + ' mintues')

print('Welcome!  \nThis program will tell you how much time your have \nleft in your audiobook if you listen to it at a modified speed.')
print('First, tell me how many hours you have left in your book')
hoursLeft = int(input())
print('Great, now can you tell me how many mintues are left?')
minLeft = int(input())
print('Lastly, I need to know what speed you are listening at')
listenSpeed = float(input())

timeRemaining(hoursLeft,minLeft,listenSpeed)
