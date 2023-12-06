from functools import reduce


with open('day02.txt', 'r') as input_file:
    input_txt = input_file.read()


games = {}


for line in input_txt.split("\n"):
    if not line:
        continue
    game_str, cube_str = line.split(": ")
    game_id = game_str.split(" ")[1]
    for cube_set in cube_str.split("; "):
        for cube_info in cube_set.split(", "):
            count, color = cube_info.split(" ")
            if not game_id in games:
                games[game_id] = {"red": 0, "green": 0, "blue": 0}
            games[game_id][color] = max(games[game_id][color], int(count))


def game_filter(game_id):
    return (
        games[game_id]["red"] <= 12 and
        games[game_id]["green"] <= 13 and
        games[game_id]["blue"] <= 14
    )


print(reduce(lambda a, c: a + int(c), filter(game_filter, games.keys()), 0))
