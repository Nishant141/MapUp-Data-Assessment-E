import pandas as pd
import os
from datetime import datetime, timedelta

def extract_trips(file_path, output_dir):
    
    data = pd.read_parquet(file_path)

    
    for unit, group_data in data.groupby("unit"):
        try:
            
            group_data.sort_values(by="timestamp", inplace=True)

            
            group_data["trip_id"] = (
                group_data["timestamp"].diff() > pd.Timedelta(hours=7)
            ).cumsum()

            
            unit_dir = os.path.join(output_dir, unit)
            if not os.path.exists(unit_dir):
                os.makedirs(unit_dir)


            for trip_id, trip_data in group_data.groupby("trip_id"):
                trip_data.to_csv(
                    os.path.join(unit_dir, f"{unit}_{trip_id}.csv"), index=False
                )
        except Exception as e:
            print(f"Error extracting trips for unit {unit}: {e}")