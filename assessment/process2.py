import os
import requests
from dotenv import load_dotenv

def upload_to_api(csv_folder, output_dir):
    # Load API key and URL from .env file
    load_dotenv()
    api_key = os.getenv("qB2fg7HGb3qNn7BT2TpDd62nd4T2Q34d")
    api_url = os.getenv("https://apis.tollguru.com/toll/v2/gps-tracks-csv-upload")

    
    for file_name in os.listdir(csv_folder):
        if file_name.endswith(".csv"):
            try:
                
                file_path = os.path.join(csv_folder, file_name)
                with open(file_path, 'rb') as file:
                    response = requests.post(
                        api_url, data=file, headers={'x-api-key': api_key, 'Content-Type': 'text/csv'}
                    )

               
                with open(os.path.join(output_dir, file_name.replace(".csv", ".json")), 'w') as outfile:
                    json.dump(response.json(), outfile)
            except Exception as e:
                print(f"Error uploading {file_name} to the TollGuru API: {e}")