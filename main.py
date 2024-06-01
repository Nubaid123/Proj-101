import random
p = str(input("Do you want to roll a dice? Y or N "))
while p=='Y':
    no=random.randint(1,6)
    if no == 1:
        print("[-------]")
        print("[       ]")
        print("[   0   ]")
        print("[       ]")
        print("[-------]")
    elif no == 2:
        print("[-------]")
        print("[ 0     ]")
        print("[       ]")
        print("[     0 ]")
        print("[-------]")
    elif no == 3:
        print("[-------]")
        print("[ 0     ]")
        print("[   0   ]")
        print("[     0 ]")
        print("[-------]")
    elif no == 4:
        print("[-------]")
        print("[ 0   0 ]")
        print("[       ]")
        print("[ 0   0 ]")
        print("[-------]")
    elif no == 5:
        print("[-------]")
        print("[ 0   0 ]")
        print("[   0   ]")
        print("[ 0   0 ]")
        print("[-------]")
    else:
        print("[-------]")
        print("[ 0   0 ]")
        print("[ 0   0 ]")
        print("[ 0   0 ]")
        print("[-------]")
    e=str(input("Do you want to roll again? Y or N "))
    if e=='Y':
        p='Y'
    else:
        p='N'
if p == 'N':
    print("Alright")