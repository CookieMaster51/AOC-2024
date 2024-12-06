import copy

ordering = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""
ordering = ordering.split("\n")
data = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

allow, restricted = [], []

for index, oline in enumerate(ordering):
    oline = oline.split("|")
    allow.append(oline[0])

allow = set(allow)

fuck_python = []

for i in range(len(allow)):
    fuck_python.append([])

restrictions = dict(zip(allow, fuck_python))


for index, oline in enumerate(ordering):
    oline = oline.split("|")
    restrictions[oline[0]].append(oline[1])

print(restrictions)

data = data.split("\n")

for dline in data:
    valid = True
    cant_have = []
    dline = dline.split(",")
    for index in range(len(dline)-1, 0, -1):
        element = dline[index]
        if element in cant_have:
            valid = False
        if element in restrictions.keys():
            cant_have += restrictions[element]
            
    if valid:
        print(dline)