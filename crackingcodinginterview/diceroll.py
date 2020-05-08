# ouput = []
call = 0
def diceRollHelper(dice,chosen):
    call +=1 
    if dice ==0:
        print(chosen)
    else:
        #choose
        #explore
        #unchoose
        for i in range(1,7):
            chosen.append(i)
            diceRollHelper(dice-1,chosen)
            chosen.pop()

def diceRoll(dice): 
    call=0
    chosen = []
    diceRollHelper(dice,chosen)
diceRoll(2)
print(call)
