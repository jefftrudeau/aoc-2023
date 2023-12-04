from functools import reduce


with open('day01.txt', 'r') as input_file:
    input_txt = input_file.read()


values = []


search_map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}


for line in input_txt.split("\n"):
    if not line:
        continue
    d0, d1 = (None, None)
    i0, i1 = (None, None)
    for k, v in search_map.items():
        try:
            i = line.index(k)
            _int = int(v)
            if i0 is None or i < i0:
                i0, d0 = i, _int
                i1, d1 = i, _int
            else:
                i1, d1 = i, _int
        except:
            pass
    for k, v in search_map.items():
        try:
            i = line.rindex(k)
            _int = int(v)
            if i > i1:
                i1, d1 = i, _int
        except:
            pass
    if d0 is None or d1 is None:
        raise ValueError("Expected int")
    values.append((d0, d1))


print(reduce(lambda acc, cur: acc + int(f"{cur[0]}{cur[1]}"), values, 0))
