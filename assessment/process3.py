import pandas as pd
import os
import json

def extract_toll_info(json_folder, output_dir):
    # Iterate through all JSON files in the input folder
    for file_name in os.listdir(json_folder):
        if file_name.endswith(".json"):
            try:
                # Load JSON file into a Python object
                with open(os.path.join(json_folder, file_name), 'r') as file:
                    data = json.load(file)

                # Extract relevant toll information from the JSON data
                # and store it in a DataFrame
                # ...

                # Append the DataFrame to the final CSV file
                with open(os.path.join(output_dir, "transformed_data.csv"), 'a') as outfile:
                    transformed_data.to_csv(outfile, header=False, index=False)
            except Exception as e:
                print(f"Error extracting toll information from {file_name}: {e}")