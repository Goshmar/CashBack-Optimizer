''' CALCULATING PAYOUTS FROM BONUS AMOUNT, "OPEN" BANK '''
import itertools

# Constants
goal = 5844.04
bills = sorted([1698, 2299, 2290, 2419, 2203.24, 3440, 2849.8, 4100, 4975, 4964])

print("Goal:", goal)
print("Bills:", bills)

# Initialize variables
best, delta_total = [], goal
min_size, min_comb_sum = 0, 0

# Find the minimum size of combinations
while min_comb_sum + bills[min_size] <= goal:
    min_comb_sum += bills[min_size]
    min_size += 1

# Find the best combination
for size in range(1, min_size + 1):
    for comb in itertools.permutations(bills, size):
        remaining_balance = goal - sum(comb)
        if 0 <= remaining_balance < delta_total:
            best = list(comb)
            delta_total = remaining_balance

print("Best:", sum(best), "-->", best)
print("Balance (Goal - Best):", round(delta_total, 2))
