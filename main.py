import json


def main_function():
    file_path = "../HearthstonePackTracker-Backend/FullPackHistory.json"
    json_data = read_json_file(file_path)

    runs = get_pack_histories_from_json_data(json_data)


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
