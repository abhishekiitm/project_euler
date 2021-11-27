
pentagonals = [1]
n = 1
pentagonals_set = set([1])

possible_satisfy = {}

condition = True
while condition:
    next_pentagonal = pentagonals[-1] + 3*n+1
    if next_pentagonal in possible_satisfy:
        print("found")
        print(f"D is {next_pentagonal - 2*possible_satisfy[next_pentagonal]}")
        break
    pentagonals.append(next_pentagonal)
    pentagonals_set.add(next_pentagonal)
    idx = n-1
    while pentagonals[idx] >= 3*n+1:
        if next_pentagonal - pentagonals[idx] in pentagonals_set:
            possible_satisfy[next_pentagonal + pentagonals[idx]] = pentagonals[idx]
        idx -= 1


    n+=1
