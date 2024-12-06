data = """3   4
4   3
2   5
1   3
3   9
3   3"""


def part2(data):
    data = data.split()
    data = list(map(int, data))

    left = [data[i] for i in range(0, int(len(data)), 2)]
    right = [data[i] for i in range(1, int(len(data)), 2)]

    left.sort()
    right.sort()
    total = 0
    for element in left:
        number = 0
        for element_right in right:
            if element_right == element:
                number += 1
            if element_right > element:
                break
        total += element * number

    print(total)

part2(data)

def part1():
    data = data.split()

    data = list(map(int, data))

    left = [data[i] for i in range(0, int(len(data)), 2)]
    right = [data[i] for i in range(1, int(len(data)), 2)]

    left.sort()
    right.sort()

    print(left, right)

    total = 0

    for i in range(0, len(left)):
        difference = abs(left[i] - right[i])
        print(difference)
        total += difference

    print(total)
