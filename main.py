import matplotlib.pyplot as plt
import sys
import json


def main_function():
    file_path = "../HearthstonePackTracker-Backend/FullPackHistory.json"
    json_data = read_json_file(file_path)

    runs_dict = get_pack_histories_from_json_data(json_data)

    # pack_type = "Classic"
    pack_type = sys.argv[1]

    plot_pack_history(pack_type, runs_dict)


def plot_pack_history(pack_type, runs_dict):
    runs = runs_dict[pack_type]

    plt.figure(figsize=(8, 6), dpi=100)

    plt.scatter(range(1, len(runs) + 1), runs)

    plt.xticks(range(1, len(runs) + 1))
    plt.yticks(range(0, 41, 5))

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for i, txt in enumerate(runs):
        plt.annotate(txt, (i + 1, runs[i]), textcoords="offset points", xytext=(0, 5), ha='center')

    plt.xlabel('Runs')
    plt.ylabel('Opened packs')
    plt.title(pack_type)

    # plt.show()
    save_path = "/home/kt/Projects/HearthstonePackTracker-Python/plots/" + pack_type + ".png"
    plt.savefig(save_path, format='png', dpi=100, bbox_inches='tight')


def get_pack_histories_from_json_data(json_data):
    runs = dict()
    for (pack_type, pack_type_data) in json_data["packHistories"].items():
        for (key, value) in pack_type_data.items():
            if isinstance(value, list):
                runs[pack_type] = value
    return runs


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{file_path}'. {e}")
        return None
    except Exception as e:
        print(f"Error reading file '{file_path}'. {e}")
        return None


if __name__ == '__main__':
    main_function()
