import json

FILENAME = "input.json"

def task() -> float:
    """ Ищет сумму произведений двух значений в каждом словаре."""
    with open(FILENAME) as f:
        data = json.load(f)
    return sum([std["score"] * std["weight"] for std in data])


print(f"{task():.3f}")
