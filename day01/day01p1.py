from functools import reduce


with open('day01.txt', 'r') as input_file:
    input_txt = input_file.read()


values = []


for line in input_txt.split("\n"):
    if not line:
        continue
    d0, d1 = (None, None)
    for char in line:
        try:
            _int = int(char)
            if d0 is None:
                d0 = _int
                d1 = _int
            else:
                d1 = _int
        except Exception as e:
            pass
    if d0 is None or d1 is None:
        raise ValueError("Expected int")
    values.append((d0, d1))


print(reduce(lambda acc, cur: acc + int(f"{cur[0]}{cur[1]}"), values, 0))
