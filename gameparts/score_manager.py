def save_score(name, score):
    with open("scores.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}: {score}\n")


def load_scores():
    try:
        with open("scores.txt", "r", encoding="utf-8") as file:
            return file.readlines()

    except FileNotFoundError:
        return []
