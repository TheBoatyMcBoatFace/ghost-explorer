# pke/app/ecu_transfer.py
import csv
import os

async def write_to_csv(data, schema, category):
    if data is None:
        print("Warning: No data to write.")
        return


    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'output'))
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, f'{category}.csv')

    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=schema)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data written to: {file_path}")
