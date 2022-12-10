# The Prisoner Puzzle

import random

def run_sim(n_prisoners):
    li_slip = []

    for i in range(1, n_prisoners+1):
        li_slip.append(i)

    random.shuffle(li_slip)

    success_count = 0

    for prisoner_num in range(n_prisoners):
        tries = 0
        token_destination = li_slip[prisoner_num]
        done = False
        success = False
        while done == False:
            if tries == n_prisoners//2:
                done = True
                success = False
                
            elif token_destination == prisoner_num+1:
                done = True
                success = True
                    
            else:
                tries += 1
                token_destination = li_slip[token_destination-1]
                        
        if success == True:
            success_count += 1

    return success_count

n_prisoners = 100
iterations = 1000
free = 0

for a in range(iterations):
    result = run_sim(n_prisoners)
    if result == n_prisoners:
        free += 1

print("P(Success) ≈", free/iterations * 100)
