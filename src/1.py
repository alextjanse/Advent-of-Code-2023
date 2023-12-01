input = open('./src/input/1.in').read().split('\n')

def isNumerical(c):
    return 48 <= ord(c) and ord(c) <= 57

def part_1(input):
    result = 0

    for line in input:
        trimmed = line

        while not isNumerical(trimmed[0]):
            trimmed = trimmed[1:]

        while not isNumerical(trimmed[-1]):
            trimmed = trimmed[:-1]

        result += int(trimmed[0] + trimmed[-1])

    print(result)

def isSpelledNumber(s: str, atStart):
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    for (digit, v) in digits.items():
        if (atStart and s.startswith(digit)) or (not atStart and s.endswith(digit)): return v
    
    return None

def part_2(input):
    result = 0

    for line in input:
        trimmed = line

        temp = isSpelledNumber(trimmed, True)
        while temp is None and not isNumerical(trimmed[0]):
            trimmed = trimmed[1:]
            temp = isSpelledNumber(trimmed, True)

        first = temp if temp is not None else int(trimmed[0])

        temp = isSpelledNumber(trimmed, False)
        while temp is None and not isNumerical(trimmed[-1]):
            trimmed = trimmed[:-1]
            temp = isSpelledNumber(trimmed, False)
        
        second = temp if temp is not None else int(trimmed[-1])

        result += 10 * first + second

    print(result)

part_1(input)
part_2(input)