import os
import json
#TODO:
#Save output_directory as param
def save_in_memory_data_as_json(input_data, output_directory):
    """
    Save in-memory list of dictionaries as JSON files.

    Parameters:
        input_data (list): List of dictionaries containing "file_name", "chunk_id", and "text".
        output_directory (str): Directory to save JSON files.
    """
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    for data in input_data:
        # Extract necessary fields
        file_name = data.get("file_name", f"document_{data.get('chunk_id', 1)}.json")
        chunk_id = data.get("chunk_id", 1)
        text = data.get("text", "")

        # Construct JSON structure
        json_data = {
            "file_name": file_name,
            "chunk_id": chunk_id,
            "text": text,
        }

        # Define the output file path
        output_path = os.path.join(output_directory, f"{os.path.splitext(file_name)[0]}_{chunk_id}.json")

        # Save JSON file
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4)

        print(f"Saved JSON: {output_path}")

if __name__=="__main__":



    output_directory = "./output_chunks"
    input_data = [
        {"file_name": "file_name",
        "chunk_id": 3,
        "text": "text",},
        {"file_name": "file_named",
        "chunk_id": 4,
        "text": "textss",}
    ]
    save_in_memory_data_as_json(input_data, output_directory)
