def read_input() -> list[list[int]]:
    with open("input.txt", "r") as f:
        return [list(map(int,line.split())) for line in f]

def is_safe(levels: list[int]) -> bool:
    is_increasing: bool = levels[1] - levels[0] > 0
    for i in range(len(levels) - 1):
        diff: int = abs(levels[i + 1] - levels[i])
        if diff > 3 or diff < 1 or (levels[i + 1] - levels[i] > 0) != is_increasing:
            return False
    return True

def part1() -> int:
    return sum(is_safe(level) for level in read_input())

def part2() -> int:
    safe_count: int = 0
    for level in read_input():
        for i in range(len(level)):
            if is_safe(level[:i] + level[i + 1:]):
                safe_count += 1
                break
    return safe_count

def main() -> None:
    print (f"SOLUTIONS\nPart 1: {part1()}\nPart 2: {part2()}")

if __name__ == '__main__':
    main()