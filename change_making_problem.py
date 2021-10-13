def get_change(change, nominals):
    nominals.sort(reverse=True)
    change_nominals = []
    while change:
        for nominal in nominals:
            if change - nominal >= 0:
                change -= nominal
                change_nominals.append(nominal)
                break
    
    return change_nominals


print(get_change(30011, [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 200000, 50000]))
