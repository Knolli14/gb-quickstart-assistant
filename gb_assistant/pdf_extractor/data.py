import os
import json

from gb_assistant.params import LOCAL_DATA_PATH


# to be fixed: json file should be overwritten. appends atm
def save_games_list(games_list):
    ''' Saves the extracetd games_list locally as json file'''

    games_dict = {"games": games_list}
    games_list_json = json.dumps(games_dict, indent=4)

    save_path = os.path.join(LOCAL_DATA_PATH, "games_list.json")
    with open(save_path, "w") as output:
        output.write(games_list_json)

    print("Dict of all games saved locally:", save_path)


def load_games_list():
    ''' Load the games_list dictionary '''

    with open(os.path.join(LOCAL_DATA_PATH, "games_list.json"), 'r') as file:
        data = json.load(file)

    print("Loaded 'games_list.json' !")
    print("Number of games:", len(data["games"]))
    return data


def save_pdf(content, title):
    ''' Save PDF of a boardgame'''

    filename = os.path.join(LOCAL_DATA_PATH, title+".pdf")

    with open(filename, "wb") as f:
        f.write(content)

    print("Downloaded", title, " rulebook!")


def load_json(file_path): #file path of JSON file to be processed needs to be given
    """Opens JSON file and loads its content into a Python dictionary."""
    try:
        with open(file_path, 'r') as json_file: #opens JSON file, given with file_path where the file is stored
            data = json.load(json_file) #loads the JSON file into a Python dictonary
        return data #returns a Python dictonary of the JSON file
    except Exception as e: #in case JSON file cannot be read, will throw an error
        print(f"Error reading JSON file: {e}")
        return None
