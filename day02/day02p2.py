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


def game_power(game_id):
    return (
        games[game_id]["red"] *
        games[game_id]["green"] *
        games[game_id]["blue"]
    )


print(
    reduce(
        lambda a, c: a + int(c), map(game_power, games.keys()),
        0
    )
)
