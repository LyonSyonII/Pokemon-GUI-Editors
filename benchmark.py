import rtoml as toml


moves = toml.load("moves.toml.bytes")
move = moves["Moves"]["Tackle"]

for i in range(100000):
    copy = move.copy()
    copy["name"] = f"Tackle{i}"
    moves.update(move)
