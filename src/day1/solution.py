from collections import Counter

def read_input() -> tuple[list[int], list[int]]:
    with open("src/day1/input.txt", "r") as f:
        (left_list, right_list) = zip(*[map(int, line.split()) for line in f])
        return(list(left_list), list(right_list))
    
def compute_distances(l1: list[int], l2: list[int]) -> list[int]:
    return [abs(x1 - x2) for (x1, x2) in zip(l1, l2)]

def part1() -> int:
    (list1, list2) = read_input()
    list1.sort()
    list2.sort()
    return sum(compute_distances(list1, list2))

def part2() -> int:
    (listl, listr) = read_input()
    return sum([(n * (Counter(listr).get(n, 0))) for n in listl])

def main() -> None:
    print (f"SOLUTIONS\nPart 1: {part1()}\nPart 2: {part2()}")

if __name__ == '__main__':
    main()