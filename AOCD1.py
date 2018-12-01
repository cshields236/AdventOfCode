import itertools
frequency = 0
with open("input.txt", "r") as f:
        l = f.read().splitlines()
def part1():
    for num in l:
        frequency += int(num)

def part2():
    seen = set([0])
    for num in itertools.cycle(l):
        frequency += int(num)
        if frequency in seen:
            print(frequency); 
        seen.add(frequency)