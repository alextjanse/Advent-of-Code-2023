from typing import List

input = open('input/2.in').read().split('\n')

def part_1(input: List[str]):
    result = 0

    for line in input:
        id, *line = line.split(': ')
        id = int(id[5:])
        line = line[0]
        sets = line.split('; ')
        
        colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for set in sets:
            items = set.split(', ')
            
            for item in items:
                [amount, color] = item.split(' ')
                colors[color] = max(colors[color], int(amount))

        if colors['red'] <= 12 and colors['green'] <= 13 and colors['blue'] <= 14:
            result += id

    return result        

def part_2(input: List[str]):
    result = 0

    for line in input:
        line = line.split(': ')[1]
        sets = line.split('; ')
        
        colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for set in sets:
            items = set.split(', ')
            
            for item in items:
                [amount, color] = item.split(' ')
                colors[color] = max(colors[color], int(amount))

        result += colors['red'] * colors['green'] * colors['blue']

    return result

print(part_1(input))

print(part_2(input))