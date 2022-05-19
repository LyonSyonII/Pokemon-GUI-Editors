from pathlib import Path
from copy import deepcopy
import rtoml as toml


parse = toml.load(Path("moves.toml.bytes"))
moves = parse["Moves"]
move = moves["Tackle"]

for i in range(100000):
    copy = deepcopy(move)
    if i % 1000 != 0:
        continue

    copy["name"] = f"Tackle_{i}"
    moves[f"Tackle_{i}"] = copy

with open("moves.toml.bytes", "w") as f:
    f.truncate(0)
    toml.dump(parse, f, pretty=True)
    f.close()
