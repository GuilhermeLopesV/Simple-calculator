import json

def save_data(results):
    data = {
        'history': results,
    }
    with open("history.json", "w") as arquivo:
        json.dump(data, arquivo, indent=4)

def load_data():
    try:
        with open("history.json", "r") as arquivo:
            data = json.load(arquivo)
        return data["history"]
    except FileNotFoundError:
        return [], []