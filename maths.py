from itertools import permutations

combs = list(permutations(["m", "m", "f", "f", "a", "b", "c", "d", "e", "j"], 10))

# print(combs)

print(len(combs))

num = 0

for comb in combs:
    if not any(comb[i] == comb[i+1] for i in range(len(comb)-1)):
        num += 1

print(num)