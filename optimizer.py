from itertools import combinations

SALARY_CAP = 50000

def optimize_lineup(players):

    best_score = 0
    best_lineup = None

    for combo in combinations(players, 9):

        salary = sum(p["Salary"] for p in combo)
        if salary > SALARY_CAP:
            continue

        score = sum(p["DFS_PROJ"] for p in combo)

        if score > best_score:
            best_score = score
            best_lineup = combo

    return best_lineup, best_score
