musclePain = False
fever = False
weakness = False

if musclePain and fever and weakness:
    print('suspicion of influenza')
elif not (musclePain and fever) and weakness:
    print('Just take a rest!')
else:
    print('You may be cold')

isMan = True
if (musclePain and fever and weakness) or isMan and (musclePain or fever or weakness):
    print('GRYPA!')
elif not(musclePain and fever) and weakness:
    print('Just take a rest')
else:
    print('You may be cold')

isCheckCompleted = True
print('CHECK IS COMPLETED' if isCheckCompleted else 'CHECK NOT DONE YET!')
